# Nugget 058 - Workflow Graphs

## Objective

Understand why workflow engines model execution as graphs.

---

# What We Built

Workflow

├── Nodes

└── Edges

Control flow is now represented independently of execution.

---

# Why We Built It

Linear execution cannot express:

- Branching
- Parallelism
- Human approvals
- Retries
- Loops

Graphs naturally support all of these.

---

# Concepts Learned

## Graph

A collection of nodes connected by edges.

---

## Node

Represents a unit of work.

---

## Edge

Represents possible execution paths.

---

## Separation of Concerns

Investigation → State

Workflow → Control Flow

Executor → Execution

---

# Design Patterns

- Graph Model
- Separation of Concerns
- State vs Control Flow

---

# Production Mapping

LangGraph → StateGraph

Airflow → DAG

Temporal → Workflow Graph

Azure Durable Functions → Orchestrator

---

# Interview Question

Q:
Why do AI workflow frameworks use graphs instead of loops?

A:

Graphs can naturally model branching, retries, loops, parallel execution, and human-in-the-loop workflows, whereas loops only represent fixed sequential execution.

---

# Key Takeaway

State answers **"What do we know?"**

The graph answers **"Where do we go next?"**

Keep those two concerns separate.