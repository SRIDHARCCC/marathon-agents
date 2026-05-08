# `src/planner_agent/runtime/` Directory Study Plan

This folder bridges the gap between the AI agent definitions and the physical execution server. It provides the necessary hooks to run the agent on Google Cloud Agent Engine using the Agent-to-Agent (A2A) SDK.

## Files to Study:

1. **`agent_executor.py`**
   - **What it does:** Implements the `AgentExecutor` class required by the A2A SDK.
   - **Key Concepts:** It initializes the ADK `Runner` and handles incoming user requests in an asynchronous loop. It uses `TaskUpdater` and `EventQueue` to stream updates (like "Planning marathon...") back to the end user. It connects the user's session to the backend `SessionManager`.

2. **`agent_card.py`**
   - **What it does:** Defines the "Agent Card", which is metadata detailing the agent's identity, capabilities, and A2A API endpoint. This is how agents discover each other.

3. **`local_server.py`**
   - **What it does:** Usually a FastAPI or Uvicorn server script used to run the `AgentExecutor` locally for testing and debugging without deploying to Google Cloud.

## How to proceed:
Focus heavily on `agent_executor.py`. This file teaches you how to transition from a standalone Python script to a scalable, persistent, event-driven agent server.
