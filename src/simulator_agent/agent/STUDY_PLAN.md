# `src/simulator_agent/agent/` Directory Study Plan

This folder contains the core logic for the **Simulation Controller Agent**, which is a strict gatekeeper checking for data completeness.

## Files to Study:

1. **`prompts.py`**
   - **What it does:** Contains the system instruction for the Simulator.
   - **Key Concepts:** It explicitly tells the agent *not* to evaluate quality, but to perform a fast "Simulation Prerequisite Check" confirming elements like distance, medical tents, and budgets are present.

2. **`tools.py`**
   - **What it does:** Contains the `check_plan_readiness` Python function.
   - **Key Concepts:** This is a great example of a deterministic tool. It uses Regex and standard keyword searching to tally up a "readiness score" based on the presence of mandatory keywords in the plan text.

3. **`agent.py`**
   - **What it does:** Initializes the Google ADK `LlmAgent` and wires up the deterministic tool.

4. **`schemas.py` & `config.py`**
   - **What it does:** Defines the final structured output (e.g., `SimulationApproval`) and loads local configuration settings.

## How to proceed:
Study `prompts.py` to understand the agent's constraints, and then deeply study `tools.py` to understand how to mix deterministic code with non-deterministic LLMs for safety and validation.
