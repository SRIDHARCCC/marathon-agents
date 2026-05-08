"""A2A Agent Card for Marathon Planner Agent."""

from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from vertexai.preview.reasoning_engines.templates.a2a import create_agent_card


def create_marathon_planner_card() -> AgentCard:
    skill = AgentSkill(
        id="plan_marathon",
        name="Plan City Marathon",
        description=(
            "Design a comprehensive city marathon plan by coordinating with "
            "specialist agents. Evaluates plan quality and returns an actionable plan."
        ),
        tags=["marathon", "planning", "orchestration", "multi-agent"],
        examples=[
            "Plan a scenic marathon through Las Vegas for 30,000 runners",
            "Design a charity marathon in Austin for October 2026",
        ],
    )

    card = create_agent_card(
        agent_name="planner_agent",
        description=(
            "Marathon Planner Agent — Lead Orchestrator that designs city marathon "
            "plans. Coordinates specialist agents via A2A. Evaluates plans with "
            "Vertex AI Eval. Powered by Gemini 3 Flash Preview."
        ),
        skills=[skill],
    )

    if card.capabilities is None:
        card.capabilities = AgentCapabilities(streaming=True)
    else:
        card.capabilities.streaming = True

    return card