# Marathon Agents

This project is a multi-agent system built using the Google Agent Development Kit (ADK), the Agent-to-Agent (A2A) SDK, and Vertex AI. It is designed to act as a Marathon Planner, bringing together different AI agents to generate, evaluate, and validate a marathon event plan.

## Architecture

The system consists of three main components:
1. **Planner Agent:** The main orchestrator that gathers user requirements and designs a comprehensive marathon plan (route, logistics, community impact).
2. **Evaluator Agent:** A local sub-agent that acts as a judge. It uses LLM-as-a-judge metrics via Vertex AI Evaluation to score the proposed plan across 7 criteria.
3. **Simulator Agent:** A remote gatekeeper agent that performs deterministic prerequisite checks to ensure the plan is ready for a hypothetical simulation engine.

## Getting Started

See [study_plan.md](study_plan.md) for a complete file-by-file breakdown and a recommended 4-phase learning journey to understand how this multi-agent architecture is built.
