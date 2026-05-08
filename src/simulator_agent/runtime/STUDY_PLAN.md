# `src/simulator_agent/runtime/` Directory Study Plan

This folder contains the execution context for deploying the Simulator Agent to Google Cloud using the A2A SDK.

## Files to Study:

1. **`agent_executor.py`**
   - **What it does:** Implements the `AgentExecutor` required to run this agent on Google Agent Engine.
   - **Key Concepts:** It receives A2A messages over the network (sent by the Planner Agent) and executes the Simulator's logic asynchronously, streaming back updates.

2. **`agent_card.py`**
   - **What it does:** The discovery document for the Simulator Agent. This file broadcasts the agent's capabilities so the remote Planner Agent can find and communicate with it.

3. **`local_server.py`**
   - **What it does:** Typically a local Uvicorn/FastAPI server for testing the agent locally before deployment.

## How to proceed:
Review `agent_executor.py` and `agent_card.py` to understand how the Agent Engine runs agents as scalable network services.
