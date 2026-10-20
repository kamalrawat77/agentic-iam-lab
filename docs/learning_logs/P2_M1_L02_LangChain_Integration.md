# Phase 2 — Module 1 — Lesson 2: LangChain Integration

## Objective

Integrate LangChain's prompt, chat model, and output parser into the existing IAM Planner.

## Engineering Problem

The Planner previously constructed prompts, called Gemini directly, and parsed response text in one method. This coupled LLM interaction to application logic.

## What We Built

- `ChatPromptTemplate` for reusable messages.
- `ChatGoogleGenerativeAI` for Gemini model access.
- `JsonOutputParser` for converting model output into Python data.
- An LCEL chain composed with `prompt | model | parser`.
- Integration with existing `Plan`, `PlanStep`, and `Investigation` domain models.

## Architecture Decision

LangChain handles the LLM interaction pipeline. The existing application retains responsibility for planning, execution, tools, and workflow orchestration.

## Reliability Notes

- JSON parsing does not guarantee semantic correctness.
- Model-generated tool arguments must be validated.
- A completed workflow does not necessarily mean every tool succeeded.
- API keys must remain outside source control.

## Interview Checkpoint

Explain LCEL composition, output parsers, and why LangChain does not replace the application's domain model or LangGraph workflow.

## Next Step

Explore structured outputs, schema validation, and failure handling for LLM-generated plans.
