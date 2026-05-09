from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FileHit:
    path: str
    title: str
    summary: str
    score: float

    def to_dict(self) -> dict:
        return self.__dict__.copy()


class FileMemory:
    """Small SQLite reference for Afu-style prepared file memory."""

    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init(self) -> None:
        with self.connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    path TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    summary TEXT NOT NULL DEFAULT '',
                    indexed_at TEXT DEFAULT CURRENT_TIMESTAMP
                );
                CREATE VIRTUAL TABLE IF NOT EXISTS files_fts USING fts5(
                    path UNINDEXED,
                    title,
                    content,
                    summary
                );
                """
            )

    def upsert_file(self, path: str, title: str, content: str, summary: str = "") -> None:
        with self.connect() as conn:
            conn.execute(
                """
                INSERT INTO files(path,title,content,summary)
                VALUES(?,?,?,?)
                ON CONFLICT(path) DO UPDATE SET
                    title=excluded.title,
                    content=excluded.content,
                    summary=excluded.summary,
                    indexed_at=CURRENT_TIMESTAMP
                """,
                (path, title, content, summary),
            )
            conn.execute("DELETE FROM files_fts WHERE path=?", (path,))
            conn.execute(
                "INSERT INTO files_fts(path,title,content,summary) VALUES(?,?,?,?)",
                (path, title, content, summary),
            )

    def search(self, query: str, limit: int = 5) -> list[FileHit]:
        safe_query = " OR ".join(token for token in query.replace('"', " ").split() if token)
        if not safe_query:
            return []
        with self.connect() as conn:
            rows = conn.execute(
                """
                SELECT files.path, files.title, files.summary, bm25(files_fts) AS rank
                FROM files_fts
                JOIN files ON files.path = files_fts.path
                WHERE files_fts MATCH ?
                ORDER BY rank
                LIMIT ?
                """,
                (safe_query, limit),
            ).fetchall()
        return [
            FileHit(path=row[0], title=row[1], summary=row[2], score=float(-row[3]))
            for row in rows
        ]
