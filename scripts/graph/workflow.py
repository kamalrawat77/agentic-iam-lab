from langgraph.graph import StateGraph

from scripts.graph.state import AgentState

from scripts.graph.nodes import (
    planner_node,
    executor_node
)

def create_graph(planner, executor):

    workflow = StateGraph(AgentState)

    workflow.add_node(
        "planner",
        lambda state: planner_node(state, planner)
    )

    workflow.add_node(
        "executor",
        lambda state: executor_node(state, executor)
    )

    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "executor")
    workflow.add_edge("executor", END)

    return workflow.compile()