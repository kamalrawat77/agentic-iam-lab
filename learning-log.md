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

## Nugget 012

Learned:
- Agent memory
- Session state
- Conversation history

Insight:


Agents become significantly more useful when they can remember prior interactions.

## Nugget 013

Learned:
- Observations
- Insight generation
- Prompt refinement

Insight:
Business value comes from interpreting data, not merely reporting it.

## Nugget 014

Learned:
- Risk scoring
- Business rules
- Classification

Insight:
Production AI systems often use deterministic business rules for decisions and LLMs for explanations.

## Nugget 015

Learned:
- Evidence-based reasoning
- Grounding
- Supported conclusions

Insight:
Production AI systems should explain conclusions using evidence rather than intuition.

## Nugget 016

Learned:
- Retrieval
- Grounding
- Context Injection

Insight:
The best AI systems retrieve information before generating answers.
## Nugget 017

Learned:
- Missing information detection
- Multi-step retrieval
- Planner pattern

Insight:
Good agents know when they do not have enough information to answer confidently.

## Nugget 018

Learned:
- Planner Agent
- Executor Agent
- Dynamic execution

Insight:
Separating planning from execution creates more reliable and maintainable agents.

## Nugget 019

Learned:
- Critic agents
- Evidence validation
- Confidence assessment

Insight:
Good agents generate answers.

## Nugget 020

Learned:
- Confidence scoring
- Evidence strength
- Rule-based confidence

Insight:
A conclusion without confidence is incomplete. Production systems communicate both the answer and how strongly they believe it.
Great agents challenge their own answers.

## Nugget 021

Learned:
- Evidence quality
- Evidence sufficiency
- Data completeness

Insight:
Strong conclusions require not just evidence, but enough high-quality evidence.

## Nugget 022

Learned:
- Root cause analysis
- Hypothesis generation
- Evidence-backed conclusions

Insight:
Observations are not root causes. Root causes require supporting evidence.

## Nugget 023

Learned:
- Hypothesis ranking
- Probabilistic reasoning
- Cause prioritization

Insight:
A good investigator ranks possible causes instead of jumping to conclusions.

## Nugget 024

Learned:
- Investigation workflows
- End-to-end reasoning pipelines
- Hypothesis generation and ranking

Insight:
Individual agent components become much more valuable when connected into a repeatable workflow.

## Nugget 025

Learned:
- State management
- Trend analysis
- Historical comparisons

Insight:
Point-in-time metrics provide observations.

## Nugget 026

Learned:
- Persistent memory
- Saving investigations
- Retrieving historical state

Insight:
An agent becomes significantly more valuable when it can remember past investigations and reason across time.
State and history provide insight.

## Nugget 027

Learned:
- Knowledge retrieval
- Searchable investigation history
- Historical case analysis

Insight:
Stored investigations become significantly more valuable when agents can search and reuse them.
