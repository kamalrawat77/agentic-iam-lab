# Nugget 054 - Execution Context

## Objective

Introduce a shared context object that lives for the duration of an investigation.

---

# What We Built

Before

Executor

↓

Tool

After

Executor

↓

Execution Context

↓

Tool

Every tool now receives the same context object.

---

# Why We Built It

Without context

- Tools cannot share results.
- Function signatures keep growing.
- Workflow state becomes fragmented.

Context centralizes all investigation state.

---

# Concepts Learned

## Execution Context

A single object that carries information across an entire workflow.

---

## Shared State

Tool A writes.

Tool B reads.

Tool C updates.

No direct communication between tools is required.

---

## Workflow State

The context stores:

- Execution ID
- User question
- Tool results
- Metadata
- Errors

---

# Design Patterns

- Context Object Pattern
- Shared State Pattern
- Single Source of Truth

---

# Production Mapping

LangGraph

↓

Graph State

Google ADK

↓

Run Context

CrewAI

↓

Shared Memory

Temporal

↓

Workflow Context

---

# Why This Matters

As systems grow, new features like logging, tracing, retries, caching, and authentication can all be added to the context without changing every tool's interface.

---

# Common Mistakes

❌ Passing dozens of function parameters.

❌ Using global variables.

❌ Letting tools depend directly on one another.

---

# Interview Questions

Q:
Why introduce an Execution Context?

A:

To provide a shared, extensible object for workflow state while keeping tool interfaces stable and minimizing coupling.

---

# Key Takeaways

Planner

↓

Executor

↓

Execution Context

↓

Tools

The context is the backbone of every investigation.