# Nugget 060 - Composition Root

## Objective

Introduce a Composition Root to manage application startup and dependency wiring.

---

# What We Built

Notebook

↓

Bootstrap

↓

Container

↓

Planner

↓

Executor

↓

Graph

The notebook now knows nothing about application internals.

---

# Why We Built It

Creating dependencies throughout the application leads to duplication and tight coupling.

A Composition Root centralizes object creation.

---

# Concepts Learned

## Composition Root

One place where all application objects are created.

---

## Dependency Container

Stores shared services.

---

## Dependency Injection

Objects receive dependencies instead of creating them.

---

# Design Patterns

- Composition Root
- Dependency Injection
- Singleton
- Factory

---

# Production Mapping

FastAPI → Startup Events

LangGraph → Graph Factory

Google ADK → Agent Runtime

OpenAI Agents SDK → Application Startup

---

# Interview Question

Q:
What is a Composition Root?

A:

A Composition Root is the single location where application dependencies are created and wired together. It centralizes object creation, simplifies testing, and keeps business logic independent of infrastructure.

---

# Key Takeaway

Objects should not create other major application objects.

They should receive them.