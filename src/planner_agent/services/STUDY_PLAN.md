# `src/planner_agent/services/` Directory Study Plan

This folder handles state management for the agents using Google Cloud.

## Files to Study:

1. **`session_manager.py`**
   - **What it does:** Integrates with Google ADK's `SessionService`.
   - **Key Concepts:** Manages long-lived user sessions, ensuring that when a user returns, the agent context knows who they are.

2. **`memory_manager.py`**
   - **What it does:** Integrates with Google ADK's `MemoryService`.
   - **Key Concepts:** Provides helper functions to save the agent's conversation history and thought process into persistent cloud storage after every interaction.

## How to proceed:
These are utility files. Review them to understand how Google ADK provides out-of-the-box solutions for LLM memory and state persistence.
