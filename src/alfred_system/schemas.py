from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal
from uuid import uuid4

Decision = Literal["allow", "prepare", "ask", "block"]
Route = Literal[
    "alfred_native",
    "afu_file_memory",
    "afu_office",
    "parallel_claw_background",
    "parallel_claw_foreground",
    "rag_only",
    "ask_owner",
    "block",
]
Risk = Literal["low", "medium", "high", "irreversible"]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class AlfredEvent:
    text: str
    owner_id: str = "local-owner"
    channel: str = "cli"
    input_type: str = "text"
    request_id: str = field(default_factory=lambda: str(uuid4()))
    mode: str = "unknown"
    attachments: list[dict[str, Any]] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=now_iso)

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_version": 1,
            "request_id": self.request_id,
            "owner_id": self.owner_id,
            "channel": self.channel,
            "input_type": self.input_type,
            "text": self.text,
            "attachments": self.attachments,
            "timestamp": self.created_at,
            "context": {"mode": self.mode, **self.context},
        }


@dataclass
class BrainDecision:
    request_id: str
    owner_id: str
    intent: str
    mode: str
    risk: Risk
    route: Route
    decision: Decision
    approval_required: bool
    reason: str
    capabilities: list[str] = field(default_factory=list)
    memory_refs: list[str] = field(default_factory=list)
    blocked_final_action: str = "none"
    learning_update: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


@dataclass
class WorkerResult:
    worker: str
    status: str
    summary: str
    artifacts: list[dict[str, Any]] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


@dataclass
class ParallelRunResult:
    request_id: str
    status: str
    synthesis: str
    lane_results: list[WorkerResult]
    blocked_final_action: str = "none"
    approval_prompt: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "request_id": self.request_id,
            "status": self.status,
            "synthesis": self.synthesis,
            "lane_results": [r.to_dict() for r in self.lane_results],
            "blocked_final_action": self.blocked_final_action,
            "approval_prompt": self.approval_prompt,
        }

