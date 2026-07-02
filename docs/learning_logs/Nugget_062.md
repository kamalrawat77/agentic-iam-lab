# Nugget 062 - Workflow State

## Objective

Treat Investigation as the evolving state of the workflow.

---

# What We Built

Investigation now represents the complete state of execution.

Nodes enrich state instead of replacing it.

---

# Concepts Learned

## Workflow State

A single object that evolves throughout execution.

---

## State Evolution

Each node adds information to the state.

---

## Enum

Replace string statuses with strongly typed values.

---

# Design Patterns

- State Pattern
- Domain Model
- Rich Domain Object

---

# Production Mapping

LangGraph → StateGraph

Temporal → Workflow State

OpenAI Agents SDK → Run Context

Google ADK → Agent State

---

# Interview Question

**Q:** Why do workflow engines prefer a single state object over passing many parameters?

**A:** A single evolving state object simplifies APIs, avoids long parameter lists, centralizes execution data, and allows workflow engines to checkpoint, retry, persist, and resume execution without reconstructing many independent values.

---

# Key Takeaway

The graph controls execution.

The Investigation remembers everything.
