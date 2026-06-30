# Nugget 056 - Framework Dependency Injection

## Objective

Separate user-provided arguments from framework-injected dependencies.

---

# Problem

Tools currently expose every function parameter to the planner.

Example:

```python
def dormant_accounts(
    context,
    days=90
)
```

The planner incorrectly thinks `context` is a user argument.

---

# Solution

Introduce dependency injection.

The planner only sees public parameters.

The framework injects internal dependencies automatically.

---

# Concepts Learned

## Dependency Injection

The framework provides objects that users should never supply.

Examples:

- ExecutionContext
- Logger
- Configuration
- Database Connection

---

## Public API vs Internal API

Public

days

department

include_privileged

Internal

context

logger

runtime

---

# Production Mapping

FastAPI

Depends()

LangGraph

Runtime Injection

OpenAI Agents SDK

RunContext

Google ADK

Agent Context

---

# Design Patterns

- Dependency Injection
- Inversion of Control
- Framework-managed Services

---

# Key Takeaway

The planner describes *what* to execute.

The framework decides *how* to execute it.