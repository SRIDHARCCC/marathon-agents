# `src/planner_agent/evaluator/` Directory Study Plan

This folder contains the **Evaluator Agent**, a specialized sub-agent invoked by the Planner to score and critique the generated marathon plan.

## Files to Study:

1. **`instructions.md`**
   - **What it does:** The system prompt for the Evaluator.
   - **Key Concepts:** Defines 7 specific criteria (Safety, Logistics, Community Impact, etc.) and a "Chain of Thought" methodology to score the plan and generate actionable feedback.

2. **`tools.py`**
   - **What it does:** The most complex file in the evaluation system. It performs the actual programmatic scoring.
   - **Key Concepts:** It uses Vertex AI's `MetricPromptBuilder` to define "LLM-as-a-judge" criteria dynamically. It calls the Vertex AI Evaluation API (`client.evals.evaluate()`) to score the plan. It also contains fallback heuristic logic using Python string matching in case the API is unavailable.

3. **`agent.py`**
   - **What it does:** Instantiates the Evaluator `LlmAgent` from the Google ADK.

4. **`schemas.py`**
   - **What it does:** Defines the structured JSON output (like `EvaluationResult`) so the feedback is easily parsed by the Planner Agent.

5. **`memory_manager.py` & `prompts.py`**
   - **What it does:** Local utilities to manage the evaluator's context history and prompt string constants.

## How to proceed:
Read `instructions.md` to see the grading rubric. Then spend a lot of time reviewing `tools.py` to learn how programmatic LLM Evaluation (LLM-as-a-judge) is implemented using Vertex AI APIs.
