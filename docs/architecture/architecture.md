# Agentic IAM Lab — Architecture Overview

> **Purpose:** A quick re-entry guide for anyone returning to this repository after a long break.
>
> **Scope:** This document describes the current implementation, including its limitations and older components. It is not a claim that the application is production-ready.

## 1. What This Application Does

Agentic IAM Lab is a learning implementation of an IAM investigation agent.

A user submits a question. The Planner uses Gemini to propose a sequence of tool calls. The Executor runs those tools and collects evidence. LangGraph orchestrates the workflow.

The current workflow is:

**Question → Investigation → Planner → Plan → Executor → Results**

The sample tools currently return illustrative or hard-coded data. They do not query a live identity platform.

## 2. High-Level Architecture

```text
Notebook / Caller
       |
       v
Application.initialize()
       |
       +---- Tool Registry
       |
       +---- Planner
       |       |
       |       v
       |    Prompt -> Gemini -> JSON -> Plan
       |
       +---- Executor
       |
       v
Compiled LangGraph
  START -> Planner -> Executor -> END
       |
       v
Updated Investigation
  - Plan
  - Execution Context
  - Status
  - Results
  - Errors
```

### Typical entry point

```python
from scripts.application.app import app
from scripts.core.investigation import Investigation

app.initialize()

investigation = Investigation(
    question="Find dormant accounts"
)

result = app.graph.invoke({
    "investigation": investigation
})

final_investigation = result["investigation"]

print(final_investigation.status)
print(final_investigation.plan)
print(final_investigation.results)
```

The graph state is a dictionary containing the `investigation` object. The graph nodes call the Planner and Executor, which update that object.

## 3. The `scripts/` Ecosystem

### `scripts/application/` — Application entry point

**File:** `app.py`

Defines the `Application` class and a module-level `app` instance.

`app.initialize()`:

1. Imports the tool modules so decorated functions register themselves.
2. Retrieves the shared tool registry.
3. Creates the Planner and Executor.
4. Builds the LangGraph workflow.

This is the clearest current entry point for running the application.

### `scripts/agent/` — Agent behavior

**`planner.py`**

- Receives an investigation.
- Retrieves the available tool catalogue.
- Constructs the prompt.
- Calls Gemini using LangChain.
- Parses the response as JSON.
- Converts the response into `Plan` and `PlanStep` objects.
- Updates the investigation status to `PLANNED`.

**`executor.py`**

- Iterates through the planned steps.
- Resolves each tool from the registry.
- Validates tool arguments.
- Executes the tool with an `ExecutionContext`.
- Collects results and execution evidence.
- Updates the investigation status.

The Planner and Executor are separate because deciding what to do and actually doing it are different responsibilities.

### `scripts/graph/` — Workflow orchestration

**`state.py`**

Defines `AgentState`, a `TypedDict` whose current field is the investigation.

**`nodes.py`**

Adapts the Planner and Executor to LangGraph nodes. Each node retrieves the investigation from the state, invokes its component, and returns the state.

**`workflow.py`**

Creates and compiles the LangGraph workflow:

```text
START -> planner -> executor -> END
```

The graph controls the execution order. It does not contain the main planning or execution logic.

### `scripts/core/` — Domain models

These files represent the application's domain concepts rather than LangGraph-specific behavior.

| File | Responsibility |
|---|---|
| `investigation.py` | Main investigation object: question, plan, context, status, results, errors |
| `plan.py` | `Plan` and `PlanStep` models |
| `context.py` | Shared execution context, execution ID, tool results, metadata, errors |
| `status.py` | Investigation lifecycle status enum |
| `workflow.py` | Earlier hand-built workflow model |

The status enum contains `CREATED`, `PLANNED`, `RUNNING`, `COMPLETED`, and `FAILED`.

**Important:** `scripts/core/workflow.py` is an earlier learning implementation. The current LangGraph workflow is built in `scripts/graph/workflow.py`.

### `scripts/tools/` — Tool registration and execution support

**`tool.py`**

Defines the `Tool` dataclass, which stores the tool name, description, category, callable function, version, risk, and parameter metadata.

**`registry.py`**

Defines `ToolRegistry` and the shared `registry` instance. The Planner uses the registry to discover available tools, and the Executor resolves tool names through it.

**`decorators.py`**

Provides the `@tool` decorator. When a decorated tool module is imported, the decorator creates a `Tool` object and registers it. It also derives basic parameter metadata from the function signature.

**`validator.py`**

Checks required parameters, unknown parameters, and supported basic types before tool execution.

**Current sample tools**

- `identity_tools.py`: contains the decorated `dormant_accounts` tool.
- `analytics_tools.py`: contains the decorated `department_breakdown` tool, which reads a previous result from the execution context.
- `incident_tools.py`: currently contains an undecorated sample function. It is not automatically registered through the current decorator-based path.

Importing the tool modules during application initialization is important because registration happens as a side effect of importing decorated functions.

### `scripts/infrastructure/` — Alternative composition approach

**`container.py`**

Defines a `Container` with fields for the registry, Planner, Executor, graph, and LLM.

**`bootstrap.py`**

Defines a module-level container and an `initialize()` function that builds the dependencies and graph.

This approach overlaps with the initialization logic in `scripts/application/app.py`.

The Week 10 learning exercises explored dependency containers and composition roots. For now, use `app.initialize()` as the primary entry point. Later, decide explicitly whether the application facade or infrastructure container should own initialization so the project does not maintain two competing approaches indefinitely.

### Other files under `scripts/`

**`config.py`**

Defines `MODEL_NAME` and retrieves `GEMINI_API_KEY` and `GITHUB_TOKEN` from Google Colab Secrets. It imports `google.colab.userdata`, so the current configuration is Colab-specific.

**`bootstrap.py`**

Contains Git configuration and push/pull helpers for the Colab workflow. Its `push()` function runs `git add .`; review staged changes before pushing to ensure that secrets, generated files, and unrelated changes are excluded.

**`executor.py` and `investigation_tools.py`**

These are simpler implementations from earlier learning stages. The current application initializes `scripts.agent.executor.Executor` and uses the modules under `scripts.tools/`; the top-level legacy files are not the execution path created by `app.initialize()`.

## 4. Core Data Model

```text
Investigation
├── question
├── plan: Plan
│   ├── goal
│   └── steps: list[PlanStep]
│       ├── tool
│       ├── purpose
│       ├── description
│       └── arguments
├── context: ExecutionContext
│   ├── execution_id
│   ├── question
│   ├── tool_results
│   ├── metadata
│   └── errors
├── status
├── results
└── errors
```

The `Investigation` is the domain object that evolves as the workflow runs.

`AgentState` is the LangGraph state envelope that currently carries the investigation through the graph.

## 5. Runtime Lifecycle

1. The caller creates an `Investigation` containing the question.
2. `app.initialize()` creates the Planner, Executor, and graph.
3. Tool modules are imported, registering decorated functions.
4. The Planner receives the question and available tool descriptions.
5. LangChain composes the prompt, Gemini model, and JSON parser.
6. The Planner converts the parsed response into domain objects.
7. LangGraph invokes the Executor node.
8. The Executor validates arguments, invokes tools, and collects evidence.
9. The graph returns its final state containing the updated investigation.

## 6. Known Limitations and Review Items

These describe the current code, not guarantees of the intended design.

- **Demo data:** Sample tools return hard-coded or illustrative results rather than live IAM data.
- **Plan validation:** Basic JSON checks do not guarantee that every selected tool exists or that a plan is semantically correct.
- **Execution status:** The Executor currently sets the investigation status to `COMPLETED` after its loop, even if individual tool calls fail. Inspect individual evidence entries; the overall status alone does not prove every step succeeded.
- **Error handling:** Tool failures may appear in evidence, but the investigation's top-level `errors` field is not consistently populated.
- **Dependency injection:** The Executor imports the module-level registry directly instead of receiving it through its constructor.
- **Duplicate initialization paths:** The Application and infrastructure bootstrap build similar dependencies.
- **Colab coupling:** Configuration imports Colab-specific APIs, limiting execution outside Colab without changes.
- **Legacy files:** The earlier executor, investigation tools, and hand-built workflow should eventually be labelled clearly as legacy or removed if no longer needed.

Use these as a backlog for future lessons. Do not try to refactor everything at once.

## 7. Where to Resume After a Long Break

1. Read this architecture document.
2. Read the [repository README](../../README.md).
3. Review the latest relevant learning log under `docs/learning_logs/`.
4. Review the [Application](../../scripts/application/app.py), [Planner](../../scripts/agent/planner.py), [Executor](../../scripts/agent/executor.py), and [LangGraph workflow](../../scripts/graph/workflow.py).
5. Open `notebooks/week10-LangGraph/Agentic_IAM_LangGraph.ipynb`.
6. Test the Planner independently before running the full workflow.
7. Continue with structured output validation, failure handling, and execution reliability.

## 8. The Architecture to Remember

- **Domain models** define the data the application works with.
- **The Planner** decides which tools to use and creates a plan.
- **The Executor** validates and runs the planned tool calls.
- **The Tool Registry** defines which tools are available.
- **LangChain** composes the LLM interaction pipeline.
- **LangGraph** controls the workflow and state transitions.
- **The Application** wires the components together.

Keep these responsibilities separate as the project grows.
