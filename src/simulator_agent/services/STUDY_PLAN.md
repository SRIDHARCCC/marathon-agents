# `src/simulator_agent/services/` Directory Study Plan

This folder manages state persistence for the Simulator Agent.

## Files to Study:

1. **`session_manager.py` & `memory_manager.py`**
   - **What they do:** Wrap Google ADK's `SessionService` and `MemoryService`.
   - **Key Concepts:** Even for a gatekeeper agent, it's important to persist conversation context and intermediate steps to Cloud Storage for debugging and context tracking.

## How to proceed:
Skim these files to recognize the common pattern of state management in the Google ADK.
