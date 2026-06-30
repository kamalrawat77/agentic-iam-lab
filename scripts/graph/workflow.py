from langgraph.graph import StateGraph

from scripts.graph.state import AgentState

from scripts.graph.nodes import (
    planner_node,
    executor_node
)

workflow = StateGraph(AgentState)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "executor",
    executor_node
)

from langgraph.graph import START, END

workflow.add_edge(
    START,
    "planner"
)

workflow.add_edge(
    "planner",
    "executor"
)

workflow.add_edge(
    "executor",
    END
)

graph = workflow.compile()