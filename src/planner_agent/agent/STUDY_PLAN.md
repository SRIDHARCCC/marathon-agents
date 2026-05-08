# `src/planner_agent/agent/` Directory Study Plan

This folder is the heart of the Planner Agent. This agent acts as a city marathon event architect, gathering user constraints and assembling a marathon plan.

## Files to Study:

1. **`planner-instruction.md`**
   - **What it does:** The core system prompt for the Planner.
   - **Why it matters:** It strictly dictates the agent's persona, its deliverables, and its multi-step workflow (Plan -> Send to Evaluator -> Send to Simulator).

2. **`agent.py`**
   - **What it does:** Initializes the Google ADK `LlmAgent`.
   - **Why it matters:** Wires together the Vertex AI configurations, the prompts, tools, and output schemas to make the agent functional.

3. **`tools.py`**
   - **What it does:** Defines the tools the agent can use. 
   - **Key Concepts:** It dynamically loads ADK skills. Most importantly, it uses `SerializableRemoteA2aAgent` to create an HTTP network connection to the remote Simulation Agent via the A2A protocol.

4. **`schemas.py`**
   - **What it does:** Uses Pydantic to enforce a structured JSON schema (`MarathonPlan`).
   - **Why it matters:** Ensures the language model's output is consistently formatted for downstream systems.

5. **`auth.py`**
   - **What it does:** Handles Google Cloud authentication for the HTTP requests when using remote A2A tools.

6. **`config.py` & `prompts.py`**
   - **What it does:** Holds localized configuration (like the specific Vertex model name) and small prompt snippets.

## How to proceed:
Read `planner-instruction.md` first to understand *what* the agent wants to do. Then, read `agent.py` and `tools.py` to see *how* it does it in code.
