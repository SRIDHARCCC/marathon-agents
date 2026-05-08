"""Evaluator Agent — scores marathon plans using Vertex AI Evaluation.

Uses gemini-3.1-pro-preview for best evaluation quality.
"""

import os

import vertexai
from google.adk.agents import LlmAgent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

from .prompts import INSTRUCTION
from .services.memory_manager import auto_save_memories
from .schemas import EvaluationResult

# Agent identity
AGENT_NAME = "evaluator_agent"
AGENT_DESCRIPTION = (
    "Evaluates marathon plans across multiple quality criteria using Vertex AI "
    "Evaluation with custom metrics. Acts as LLM-as-Judge to score plans and "
    "provide actionable feedback for iterative improvement."
)

# Model — use gemini-3.1-pro-preview for evaluation accuracy
MODEL = os.getenv("EVALUATOR_MODEL", "gemini-3.1-pro-preview")

# Structured output schema — guarantees every response matches EvaluationResult
OUTPUT_SCHEMA = EvaluationResult

# Criterion weights must sum to 1.0
CRITERION_WEIGHTS = {
    "safety_compliance": 0.20,
    "community_impact": 0.15,
    "logistics_completeness": 0.20,
    "financial_viability": 0.15,
    "participant_experience": 0.15,
    "intent_alignment": 0.10,
    "distance_compliance": 0.05,
}

SEVERITY_THRESHOLDS = {"high": 40.0, "medium": 60.0, "low": 80.0}

# Initialize Vertex AI
project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
if project_id:
    vertexai.init(project=project_id, location=location)

from google.genai.types import GenerateContentConfig, ThinkingConfig
from .tools import evaluate_plan

# Enable thinking for better evaluation reasoning
evaluator_config = GenerateContentConfig(max_output_tokens=4096)
if "pro" in MODEL:
    evaluator_config.thinking_config = ThinkingConfig(thinking_budget=1024)

evaluator_agent = LlmAgent(
    name="evaluator_agent",
    model=MODEL,
    description=AGENT_DESCRIPTION,
    static_instruction=INSTRUCTION,
    output_schema=OUTPUT_SCHEMA,
    generate_content_config=evaluator_config,
    include_contents='none',
    tools=[PreloadMemoryTool(), evaluate_plan],
    after_agent_callback=auto_save_memories,
)

root_agent = evaluator_agent