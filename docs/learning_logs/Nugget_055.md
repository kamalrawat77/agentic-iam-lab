# Nugget 055 - Investigation Domain Model

## Objective

Introduce a first-class Investigation object that owns the complete lifecycle of an investigation.

---

# What We Built

Planner

↓

Investigation

↓

Executor

↓

Updated Investigation

Instead of passing multiple independent values, every stage now operates on the Investigation.

---

# Why We Built It

As workflows grow, passing many arguments becomes difficult to maintain.

The Investigation object centralizes workflow state and evolves throughout execution.

---

# Concepts Learned

## Domain Model

Represent a real business concept as an object.

In our framework, the Investigation is the core domain entity.

---

## Aggregate Root

The Investigation owns:

- Question
- Plan
- Context
- Results
- Errors
- Status

Other components interact with it rather than managing their own copies.

---

## Workflow Lifecycle

An investigation progresses through well-defined states:

CREATED → PLANNED → RUNNING → COMPLETED

This makes the workflow observable and extensible.

---

# Design Patterns

- Domain Model
- Aggregate Root
- Encapsulation
- Single Source of Truth

---

# Production Mapping

LangGraph → Graph State

Temporal → Workflow Instance

OpenAI Agents SDK → Run

Google ADK → Agent Session

---

# Common Mistakes

❌ Passing unrelated dictionaries between components.

❌ Losing workflow context after planning.

❌ Letting multiple components own the same state.

---

# Interview Questions

Q:
Why use an Investigation object instead of passing dictionaries?

A:

It centralizes workflow state, reduces coupling, improves discoverability, and creates a stable API that can evolve without changing every method signature.

---

# Key Takeaways

Question

↓

Investigation

↓

Planner

↓

Executor

↓

Completed Investigation

The Investigation is now the backbone of the framework.