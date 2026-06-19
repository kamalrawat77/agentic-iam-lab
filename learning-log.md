# Learning Log

## Nugget 001

Date : 2026-06-18

Objective: Create project foundation

Completed:
-Repository created
-README created
-Learning Log created

Questions:
- None yet

- Next Nugget 002

## Nugget 002

Learned:
- Lists
- Dictionaries
- Loops
- Basic aggregation

Artifact:
- First IAM analysis notebook

Questions:
-What do we do in below code snippet. Explain

enabled_count = sum(1 for u in users if u["enabled"])

print(f"Enabled Users: {enabled_count}")

- Also explain  departments[dept] = departments.get(dept, 0) + 1

## Nugget 003

Learned:
- Pandas
- DataFrames
- Reading CSV files
- Filtering rows
- value_counts()

Artifact:
- First real CSV analysis

Questions:
...How to put csv in collab. Answer put in Content folder
## Nugget 004

Learned:
- API keys
- LLM calls
- Prompt engineering basics
- Gemini SDK

Artifact:
- First AI interaction from Python

Questions:
.Is the calling the LLM function same for all type of LLMS. Is it reusable for all and we just change the key and model?

Observation:

LLMs are becoming interchangeable.

The durable skills are:
- Python
- Data processing
- Tool calling
- RAG
- Agent workflows
- Evaluation

## Nugget 005

Learned:
- Functions
- Reusable tools
- Report generation

Key Insight:
Agents do not magically know things.
They use tools to obtain information.

Artifact:
First IAM analysis toolkit.

---
Task: 

Agent calculate
1. Orphaned accounts
2. Dormant accounts
3. accounts with unusual activity
4. target identity system connections
5. Daily JML completion time

## Nugget 006

Included in Nugget 004. How to call prompts with data

## Nugget 007

Learned:
- Tool selection
- Routing
- LLM decision making

Insight:
The LLM does not need to do the work.

## Nugget 008
LLM + Tools

## Nugget 009

Learned:
- Multi-step agent flow
- Tool execution
- Result interpretation

Insight:
The LLM can be used twice:
1. To decide what to do
2. To explain what happened
Its job can be deciding which tool should do the work.

## Nugget 010

Learned:
- Planning
- Multi-tool reasoning
- Information gathering

Insight:
An agent should decide what information it needs before deciding what answer to give.

## Nugget 011

Learned:
- Validation
- Error handling
- Guardrails

Insight:
Production agents must expect bad outputs and recover gracefully.
