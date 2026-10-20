# Nugget 063 — Structured Outputs and Plan Validation

## Objective

Strengthen the IAM Planner so it rejects malformed model responses, unknown tool names, and invalid tool arguments before creating a plan.

## Engineering Problem

Valid JSON is not necessarily a valid plan. A model can return syntactically correct JSON that references an unavailable tool or supplies arguments that the tool cannot accept.

## What We Built

- `scripts/core/planner_schema.py` defines `PlannedStepOutput` and `PlannerResponse` using Pydantic.
- `PydanticOutputParser` parses and validates the model response against the schema.
- The Planner resolves proposed tools through the registry.
- The existing argument validator checks required parameters, unknown parameters, and supported types.
- The Planner creates domain `PlanStep` objects only after all proposed steps pass validation.

## Architecture Decision

Keep the LLM response schema separate from the application's domain models.

The schema describes the expected output from the model. `Plan` and `PlanStep` remain the application's domain representations. The Planner converts between them after validation.

## Concepts Learned

- Structured output
- Pydantic models
- Schema validation
- Syntactic validity versus semantic validity
- Registry-based tool validation
- Validation before execution
- Separation of model output contracts from domain models

## Reliability Notes

- A schema does not guarantee that a plan is logically correct.
- A known tool can still be inappropriate for a question.
- Valid arguments do not establish that a user is authorized to perform an operation.
- Validation errors currently stop planning; automatic retries are not implemented.
- The existing argument validator supports only a limited set of parameter types.

## Interview Checkpoint

1. Why is valid JSON insufficient for an agent?
2. What is the difference between schema validation and business validation?
3. Why keep Pydantic response models separate from domain models?
4. Why should validation happen before tool execution?
5. What additional safeguards are needed before an agent can perform real IAM operations?

## Mini Exercise

Create a malformed `PlannerResponse` payload and confirm Pydantic rejects it. Then test a structurally valid response that references an unknown tool and confirm the Planner rejects it before creating the plan.

## Git Commit

`feat: validate planner outputs and tool arguments`

## Next Nugget

Improve tool argument validation: support more JSON types, improve type checks, and test the validator independently of Gemini.
