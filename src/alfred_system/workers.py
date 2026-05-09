from __future__ import annotations

from pathlib import Path

from .file_memory import FileMemory
from .schemas import WorkerResult


def simple_summary(text: str, max_chars: int = 220) -> str:
    compact = " ".join(text.split())
    return compact[:max_chars] + ("..." if len(compact) > max_chars else "")


def index_text_directory(root: str | Path, memory: FileMemory) -> WorkerResult:
    """Reference background worker.

    Production Afu workers can materialize Google Drive, OCR PDFs/images, and
    use local models. This reference worker indexes local .txt/.md files to show
    the same contract without private integrations.
    """

    root = Path(root)
    indexed = 0
    artifacts = []
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in {".txt", ".md"} or not path.is_file():
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        summary = simple_summary(content)
        memory.upsert_file(str(path), path.name, content, summary)
        indexed += 1
        artifacts.append({"path": str(path), "title": path.name})
    return WorkerResult(
        worker="file_indexer",
        status="completed",
        summary=f"Indexed {indexed} text files into prepared file memory.",
        artifacts=artifacts,
        metrics={"indexed": indexed},
    )


def daily_brief_stub() -> WorkerResult:
    return WorkerResult(
        worker="daily_brief",
        status="completed",
        summary="Prepared a placeholder daily brief from calendar, files, and open promises.",
        artifacts=[],
        metrics={"source": "stub"},
    )

