# `src/simulator_agent/` Directory Study Plan

This folder encapsulates the **Simulator Agent**, a gatekeeper that ensures a generated marathon plan contains all the necessary data points required for a hypothetical simulation engine.

## Folder Structure to Study:

1. **`agent/`**: Contains the core logic, prompts, schemas, and tools for the Simulator Agent. This agent is simpler than the Planner; it relies on deterministic checks rather than LLM-as-a-judge evaluation.
2. **`runtime/`**: Contains the execution code that runs the agent on Google Cloud Agent Engine using the Agent-to-Agent (A2A) SDK.
3. **`services/`**: Contains utilities to manage conversation sessions and persist memories using Google ADK.
4. **`skills/`**: Contains dynamic Google ADK skills (like `review-marathon-plan`) that the agent can equip.

## How to proceed:
Start with `agent/prompts.py` to see the agent's instructions, then look closely at `agent/tools.py` to see how Python deterministic code is used to validate an LLM's output.
