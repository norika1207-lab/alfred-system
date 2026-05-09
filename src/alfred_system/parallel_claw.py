from __future__ import annotations

from .schemas import AlfredEvent, BrainDecision, ParallelRunResult, WorkerResult


def run_foreground(event: AlfredEvent, decision: BrainDecision) -> ParallelRunResult:
    """Reference foreground specialist execution.

    Real adapters can run different models/tools. This keeps the public contract
    small and inspectable.
    """

    lanes = [
        WorkerResult("research_lane", "completed", "Collected relevant context from prepared memory."),
        WorkerResult("risk_lane", "completed", f"Risk tier: {decision.risk}. Final action: {decision.blocked_final_action}."),
        WorkerResult("dissent_lane", "completed", "Checked for missing evidence and overconfident claims."),
        WorkerResult("synthesis_lane", "completed", "Prepared a short decision brief."),
    ]
    status = "needs_approval" if decision.approval_required else "completed"
    approval = ""
    if decision.approval_required:
        approval = f"Approve final action '{decision.blocked_final_action}'?"
    return ParallelRunResult(
        request_id=event.request_id,
        status=status,
        synthesis=f"Prepared work for: {event.text}",
        lane_results=lanes,
        blocked_final_action=decision.blocked_final_action,
        approval_prompt=approval,
    )

