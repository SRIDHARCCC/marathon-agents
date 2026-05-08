"""Local A2A server for the Marathon Planner Agent.

Usage: uv run python -m src.planner_agent.runtime.local_server
"""

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"

import asyncio
import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import TransportProtocol
from google.adk import Runner
from google.adk.a2a.executor.a2a_agent_executor import A2aAgentExecutor, A2aAgentExecutorConfig
from google.adk.sessions import InMemorySessionService

AGENT_PORT = 8084


def create_marathon_planner_server():
    from ..agent import root_agent
    from .agent_card import create_marathon_planner_card

    runner = Runner(
        app_name=root_agent.name,
        agent=root_agent,
        session_service=InMemorySessionService(),
    )

    executor = A2aAgentExecutor(runner=runner, config=A2aAgentExecutorConfig())
    handler = DefaultRequestHandler(agent_executor=executor, task_store=InMemoryTaskStore())

    card = create_marathon_planner_card()
    card.url = f"http://localhost:{AGENT_PORT}"
    card.preferred_transport = TransportProtocol.jsonrpc

    return A2AStarletteApplication(agent_card=card, http_handler=handler)


async def run_server():
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project:
        raise ValueError("GOOGLE_CLOUD_PROJECT must be set. Check .env file.")

    print("=" * 60)
    print("Starting Marathon Planner Agent Local A2A Server")
    print(f"Project: {project}")
    print("=" * 60)

    app = create_marathon_planner_server()
    config = uvicorn.Config(app.build(), host="127.0.0.1", port=AGENT_PORT, log_level="info", loop="none")

    print(f"Planner A2A server: http://127.0.0.1:{AGENT_PORT}")
    print(f"Agent card: http://127.0.0.1:{AGENT_PORT}/.well-known/agent-card.json")
    print("Press Ctrl+C to stop")
    print("=" * 60)

    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(run_server())