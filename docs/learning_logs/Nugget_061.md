# Nugget 061 - Application as Composition Root

## Objective

Replace scattered startup logic with a single Application object.

---

# What We Built

Application

├── Registry

├── Planner

├── Executor

└── Graph

The notebook now interacts with only one object.

---

# Why We Built It

A single entry point reduces coupling and centralizes application startup.

---

# Concepts Learned

## Application Object

Owns the lifecycle of the system.

---

## Composition Root

One place where dependencies are created and wired together.

---

## Layered Architecture

Notebook → Application → Graph → Services → Tools

---

# Design Patterns

- Composition Root
- Facade
- Dependency Injection
- Singleton

---

# Production Mapping

FastAPI → FastAPI app

Flask → Flask app

OpenAI Agents SDK → Run/Session

Google ADK → Agent Runtime

---

# Interview Question

Q:
Why expose an Application object instead of creating services directly in notebooks?

A:

It provides a single entry point for initialization, hides infrastructure details from callers, centralizes dependency wiring, and makes the system easier to test and maintain.

---

# Key Takeaway

Your notebook should describe **what** to do.

The Application should know **how** the system is built.