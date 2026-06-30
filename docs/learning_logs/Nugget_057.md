# Nugget 057 - Plan Domain Model

## Objective

Replace raw dictionaries with Plan and PlanStep objects.

---

# What We Built

Investigation

↓

Plan

↓

PlanStep

The planner converts LLM JSON into domain objects before the executor uses them.

---

# Why We Built It

Dictionaries are flexible but fragile.

Objects provide:

- Type safety
- Autocomplete
- Easier refactoring
- Clearer APIs

---

# Concepts Learned

## Domain Model

Represent business concepts as objects.

---

## Composition

An Investigation owns a Plan.

A Plan owns many PlanSteps.

---

## Boundary Pattern

LLM output remains JSON only at the system boundary.

Inside the framework, everything becomes strongly typed objects.

---

# Design Patterns

- Domain Model
- Composition
- Boundary Translation
- Encapsulation

---

# Production Mapping

LangGraph → Graph State + Nodes

Temporal → Workflow + Activities

Airflow → DAG + Operators

---

# Interview Question

Q:
Why convert LLM JSON into domain objects?

A:

JSON is an exchange format, not a domain model. Converting to objects improves maintainability, enables validation, and gives the application a stable internal API.

---

# Key Takeaway

LLM

↓

JSON

↓

Domain Objects

↓

Workflow Engine

Treat JSON as an external contract, not the internal representation of your application.