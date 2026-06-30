from scripts.agent.planner import Planner
import scripts.tools
from scripts.tools.registry import registry

planner = Planner(registry)

def planner_node(state):

    investigation = state["investigation"]

    planner.create_plan(investigation)

    return state


from scripts.agent.executor import Executor

executor = Executor()

def executor_node(state):

    investigation = state["investigation"]

    executor.execute(investigation)

    return state