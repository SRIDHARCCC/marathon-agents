# Marathon Planner Agent: Codebase Breakdown & Study Plan

This document provides a complete breakdown of the `marathon-agents` codebase and a structured study plan to help you learn and understand the project from the ground up.

## 1. File-by-File Breakdown

The project is built using Google's Agent Development Kit (ADK) and the Agent-to-Agent (A2A) SDK, integrated with Vertex AI to construct a multi-agent system consisting of a Planner, Evaluator, and Simulator.

### Root & Configuration
*   **`pyproject.toml`**: The main project configuration. Defines dependencies like `google-cloud-aiplatform`, `google-adk`, and `a2a-sdk`.
*   **`src/config.py`**: A shared configuration file that loads environment variables like `GOOGLE_CLOUD_PROJECT` and `BUCKET_URI` using `python-dotenv`.

### The Planner Agent (`src/planner_agent/`)
The main orchestrator. It interacts with the user, gathers constraints, designs a plan, and sends it to the Evaluator and Simulator.
*   **`agent/agent.py`**: Wires up the `LlmAgent` for the planner. Connects prompts, tools, output schemas, and Vertex AI configurations.
*   **`agent/planner-instruction.md`**: The core system prompt. Instructs the agent on its role as a "city marathon event architect" and defines its workflow (planning, then invoking Evaluator and Simulator).
*   **`agent/tools.py`**: Configures the tools available to the planner. Notably, it contains `SerializableRemoteA2aAgent`, a custom wrapper that sets up the connection to the remote Simulation Agent via the A2A protocol. It also dynamically loads ADK skills.
*   **`agent/schemas.py`**: Defines Pydantic models like `MarathonPlan` to ensure the LLM outputs structured JSON data.
*   **`skills/`**: Contains ADK Skill definitions (`plan-evaluation`, `route-planning`) that are loaded dynamically into the agent's toolset.
*   **`services/memory_manager.py` & `session_manager.py`**: Utilities integrating with ADK's `MemoryService` and `SessionService` to keep track of user sessions and persist conversation history.
*   **`runtime/agent_executor.py`**: Implements the `AgentExecutor` required by the A2A platform. It handles the request context, spins up an ADK `Runner`, and manages task states (like updating UI artifacts as the plan generates).

### The Evaluator Agent (`src/planner_agent/evaluator/`)
A sub-agent called by the Planner to score the marathon plan.
*   **`agent.py`**: Instantiates the Evaluator `LlmAgent`.
*   **`instructions.md`**: Outlines a strict "Chain of Thought" evaluation methodology across 7 criteria (Safety, Logistics, Community Impact, etc.).
*   **`tools.py`**: The heavy lifter for evaluation. It uses `vertexai.types.MetricPromptBuilder` to dynamically create LLM-as-a-judge metrics. It hits the Vertex AI Evaluation API to score the plan and falls back to a deterministic heuristic function if the API fails.

### The Simulator Agent (`src/simulator_agent/`)
The final gatekeeper before the plan is deployed/simulated. It ensures data completeness.
*   **`agent/agent.py`**: Sets up the Simulator `LlmAgent`.
*   **`agent/prompts.py`**: System prompt clarifying that the simulator does *not* evaluate quality, but rather checks for deterministic prerequisites (data completeness).
*   **`agent/tools.py`**: Contains `check_plan_readiness`, a Python function using Regex and keyword matching to ensure the plan mentions specific distances, water stations, medical tents, and budgets.

---

## 2. Recommended Study Plan

To fully understand how to build complex multi-agent architectures using Google ADK and Vertex AI, follow this 4-phase study plan:

### Phase 1: The Foundation (Core ADK & LLM setup)
**Goal:** Understand how a single agent is built and prompted.
1.  **Read `pyproject.toml`**: Familiarize yourself with the libraries used.
2.  **Explore `src/planner_agent/agent/agent.py`**: Look at how `LlmAgent` is initialized with Vertex AI.
3.  **Read `planner-instruction.md`**: Study how to effectively write a system prompt that dictates a strict multi-step workflow.
4.  **Review `schemas.py`**: Understand how Pydantic is used to enforce structured output from Vertex AI.

### Phase 2: Skills and Tooling (Connecting Agents to Code)
**Goal:** Learn how agents execute code and perform actions.
1.  **Examine `src/simulator_agent/agent/tools.py`**: Look at `check_plan_readiness`. See how standard Python deterministic logic is exposed as a tool to the LLM.
2.  **Examine `src/planner_agent/agent/tools.py`**: Focus on the `get_tools()` function to see how ADK Skills (folders containing `SKILL.md`) are loaded into a `SkillToolset`.

### Phase 3: Agent-to-Agent (A2A) Communication
**Goal:** Understand how different agents communicate across the Google Cloud Agent Engine.
1.  **Study `src/planner_agent/agent/tools.py` (Remote A2A)**: Look at the `SerializableRemoteA2aAgent` class. This shows how an agent can be treated as a "tool" by another agent via an HTTP/A2A endpoint.
2.  **Review the Evaluator vs Simulator connection**: Notice how the Evaluator is loaded locally (`create_evaluator_tool`), while the Simulator is loaded remotely over the network (`create_simulator_agent`).

### Phase 4: Advanced Evaluation & Deployment
**Goal:** Learn how to programmatically evaluate LLM outputs and deploy the app.
1.  **Deep Dive into `src/planner_agent/evaluator/tools.py`**: This is the most complex file. Study how `MetricPromptBuilder` is used to create custom LLM evaluation rubrics and how the code calls `client.evals.evaluate()`.
2.  **Examine `src/planner_agent/runtime/agent_executor.py`**: Look at how the A2A `AgentExecutor` class wraps the ADK `Runner`. Pay attention to how it handles `TaskUpdater` and `EventQueue` to stream status updates back to a user interface.
3.  **Examine Services (`services/memory_manager.py`)**: See how memories and sessions are persisted in Google Cloud.
