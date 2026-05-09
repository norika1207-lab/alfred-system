from __future__ import annotations

from .schemas import AlfredEvent, BrainDecision


IRREVERSIBLE_WORDS = {
    "send": "send",
    "email": "send",
    "publish": "publish",
    "post": "publish",
    "pay": "pay",
    "checkout": "pay",
    "buy": "pay",
    "sell": "trade",
    "trade": "trade",
    "merge": "merge",
    "delete": "delete",
    "submit": "submit",
}


def _detect_final_action(text: str) -> str:
    lowered = text.lower()
    for word, action in IRREVERSIBLE_WORDS.items():
        if word in lowered:
            return action
    return "none"


def _detect_intent(event: AlfredEvent) -> str:
    text = event.text.lower()
    if event.input_type in {"image", "photo"} or any(a.get("type") == "image" for a in event.attachments):
        return "image_ocr"
    if any(k in text for k in ["file", "document", "pdf", "drive", "找", "檔案", "文件"]):
        return "file_search"
    if any(k in text for k in ["calendar", "meeting", "會議", "行事曆", "schedule"]):
        return "calendar"
    if any(k in text for k in ["compare", "review", "research", "分析", "比較", "研究"]):
        return "research"
    return "general"


def decide(event: AlfredEvent) -> BrainDecision:
    """Reference Afu Brain style route decision.

    This is deliberately deterministic. Production systems can add local model
    classification, owner memory, RAG packs, or policy tables around this
    contract, but the output should stay inspectable.
    """

    intent = _detect_intent(event)
    final_action = _detect_final_action(event.text)

    if final_action != "none":
        return BrainDecision(
            request_id=event.request_id,
            owner_id=event.owner_id,
            intent=intent,
            mode=event.mode,
            risk="irreversible",
            route="parallel_claw_foreground" if intent == "research" else "afu_office",
            decision="ask",
            approval_required=True,
            capabilities=["prepare_only", "approval_gate"],
            blocked_final_action=final_action,
            reason=f"Detected final action boundary: {final_action}. Prepare work, but ask before execution.",
        )

    if intent == "file_search":
        return BrainDecision(
            request_id=event.request_id,
            owner_id=event.owner_id,
            intent=intent,
            mode=event.mode,
            risk="low",
            route="afu_file_memory",
            decision="allow",
            approval_required=False,
            capabilities=["afu.file.find", "afu.file.summarize"],
            reason="File request should use prepared local file memory before any cloud model.",
        )

    if intent == "image_ocr":
        return BrainDecision(
            request_id=event.request_id,
            owner_id=event.owner_id,
            intent=intent,
            mode=event.mode,
            risk="medium",
            route="afu_office",
            decision="prepare",
            approval_required=False,
            capabilities=["afu.ocr.extract", "afu.document.structure"],
            reason="Image/document extraction is preparation; no external final action detected.",
        )

    if intent in {"calendar", "research"}:
        return BrainDecision(
            request_id=event.request_id,
            owner_id=event.owner_id,
            intent=intent,
            mode="office" if event.mode == "unknown" else event.mode,
            risk="medium",
            route="parallel_claw_foreground" if intent == "research" else "afu_office",
            decision="prepare",
            approval_required=False,
            capabilities=["afu.office.context", "parallel_claw.foreground"],
            reason="Office/research task benefits from prepared work context and specialist lanes.",
        )

    return BrainDecision(
        request_id=event.request_id,
        owner_id=event.owner_id,
        intent=intent,
        mode=event.mode,
        risk="low",
        route="alfred_native",
        decision="allow",
        approval_required=False,
        capabilities=["alfred.reply"],
        reason="Low-risk general request.",
    )

