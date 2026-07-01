
def planner_node(state,planner):

    investigation = state["investigation"]

    planner.create_plan(investigation)

    return state



def executor_node(state,executor):

    investigation = state["investigation"]

    executor.execute(investigation)

    return state