# `src/planner_agent/` Directory Study Plan

This folder encapsulates the **Marathon Planner Agent**, the primary orchestrator of the multi-agent system. 

## Folder Structure to Study:

1. **`agent/`**: Contains the core logic, prompts, schemas, and tools for the Planner Agent. This is the "brain" that gathers requirements and drafts the initial plan.
2. **`evaluator/`**: Contains an internal sub-agent (the Evaluator) that is invoked by the Planner to score the drafted plan against 7 strict criteria.
3. **`runtime/`**: Contains the execution code that runs the agent on Google Cloud Agent Engine using the Agent-to-Agent (A2A) SDK.
4. **`services/`**: Contains utilities to manage conversation sessions and persist memories using Google ADK.
5. **`skills/`**: Contains dynamic Google ADK skills (like route generation) that the agent can equip as tools.

## How to proceed:
Your best starting point is the `agent/` folder, followed by `evaluator/` to see how the plan gets judged. After understanding the agents, look at `runtime/` to see how they are executed.
