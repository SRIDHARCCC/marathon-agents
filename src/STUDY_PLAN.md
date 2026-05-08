# `src/` Directory Study Plan

Welcome to the `src/` directory! This is the root source folder containing the Python codebase for the multi-agent system.

## Files to Study:

1. **`config.py`**
   - **What it does:** This is the shared configuration file for the entire multi-agent system. It uses `python-dotenv` to load environment variables.
   - **Key Concepts:** It loads essential Google Cloud configuration variables like `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, and `BUCKET_URI`. It also includes a `validate_config()` function to ensure these mandatory variables are set before the application starts.
   - **Why it matters:** Centralized configuration ensures that all agents and sub-modules point to the correct Google Cloud Project and Storage instances.

## How to proceed:
Once you understand how the global configuration works in `config.py`, head over to the `planner_agent/` and `simulator_agent/` directories to see how the specific agents are implemented.
