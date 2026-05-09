from __future__ import annotations

import json
import tempfile
from pathlib import Path

from .brain import decide
from .file_memory import FileMemory
from .parallel_claw import run_foreground
from .schemas import AlfredEvent
from .workers import daily_brief_stub, index_text_directory


def build_sample_workspace(root: Path) -> None:
    (root / "V121-land-file.txt").write_text(
        "台糖土地 屏東 V121. This file contains land parcel notes, meeting context, and a quote reference.",
        encoding="utf-8",
    )
    (root / "meeting-brief.md").write_text(
        "Tomorrow meeting: review V121 land file, compare quote terms, check follow-up owner.",
        encoding="utf-8",
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "workspace"
        root.mkdir()
        build_sample_workspace(root)

        memory = FileMemory(Path(tmp) / "alfred-file-memory.sqlite")
        worker = index_text_directory(root, memory)
        brief = daily_brief_stub()

        event = AlfredEvent(
            text="幫我找台糖土地屏東 V121 那份資料",
            channel="line",
            mode="office",
        )
        decision = decide(event)
        hits = memory.search(event.text, limit=3)

        parallel = None
        if decision.route == "parallel_claw_foreground":
            parallel = run_foreground(event, decision).to_dict()

        print(json.dumps({
            "workers": [worker.to_dict(), brief.to_dict()],
            "event": event.to_dict(),
            "brain_decision": decision.to_dict(),
            "file_hits": [hit.to_dict() for hit in hits],
            "parallel_run": parallel,
        }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

