# Nugget 053 - Schema Validation Engine

## Objective

Introduce deterministic validation between the planner and executor.

Instead of trusting the LLM output, validate every tool call before execution.

---

# What We Built

Planner

↓

Validation Engine

↓

Executor

↓

Tool

---

# Why We Built It

LLMs are probabilistic.

They can

- Miss required arguments
- Invent parameters
- Return incorrect data types

Business logic should never receive unvalidated input.

---

# Concepts Learned

## Input Contracts

Every tool defines a contract.

Example

days

↓

integer

↓

required

The validator enforces this contract.

---

## Guardrails

Guardrails prevent invalid LLM output from affecting the system.

Examples

- Unknown arguments
- Missing required fields
- Incorrect types

---

## Fail Fast

Detect errors immediately.

Don't allow invalid data to continue through the execution pipeline.

---

## Custom Exceptions

Create meaningful exception types.

ValidationError

is more expressive than

Exception.

---

# Design Patterns

- Validation Layer
- Guardrail Pattern
- Fail Fast
- Defensive Programming

---

# Production Mapping

OpenAI

↓

JSON Schema Validation

↓

Tool Call

---

Google ADK

↓

Function Declaration Validation

---

FastAPI

↓

Pydantic Validation

↓

Endpoint Execution

---

# Common Mistakes

❌ Trusting LLM output.

❌ Using generic exceptions.

❌ Skipping validation for internal systems.

---

# Interview Questions

Q:

Why validate LLM output?

A:

LLMs generate probabilistic outputs.

Validation ensures only deterministic, contract-compliant data reaches business logic.

---

Q:

What is Fail Fast?

A:

Detect and stop invalid execution as early as possible.

---

# Key Takeaways

Planner

↓

Validator

↓

Executor

↓

Tool

LLMs suggest actions.

Deterministic code enforces correctness.