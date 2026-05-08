"""A2A Agent Card for Simulation Controller Agent."""

from a2a.types import AgentCard, AgentSkill
from vertexai.preview.reasoning_engines.templates.a2a import create_agent_card


def create_simulation_controller_card() -> AgentCard:
    skill = AgentSkill(
        id="review_marathon_plan",
        name="Review Marathon Plan",
        description="Review a marathon plan for simulation readiness.",
        tags=["simulation", "review", "approval", "marathon"],
    )
    return create_agent_card(
        agent_name="simulator_agent",
        description="Simulation Controller Agent - Reviews marathon plans for simulation readiness.",
        skills=[skill],
    )