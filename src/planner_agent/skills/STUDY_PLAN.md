# `src/planner_agent/skills/` Directory Study Plan

This folder houses the Google ADK "Skills" available to the planner. Skills are self-contained modules that give agents new capabilities.

## Folders to Study:

1. **`plan-evaluation/`** & **`route-planning/`**
   - **What they are:** Sub-folders containing ADK Skill definitions.
   - **Key Concepts:** In the Google ADK, a skill directory typically contains a `SKILL.md` file detailing what the skill does, and Python tools that actually perform the actions. The Planner's `tools.py` file dynamically loads these folders and equips them into the agent's `SkillToolset`.

## How to proceed:
Open the `SKILL.md` files inside the subdirectories to see how a skill is documented and packaged.
