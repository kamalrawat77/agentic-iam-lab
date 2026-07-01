from scripts.infrastructure.container import Container

container = Container()

def initialize():

    import scripts.tools
    from scripts.tools.registry import registry
    from scripts.agent.planner import Planner
    from scripts.agent.executor import Executor

    container.registry = registry
    container.planner = Planner(registry)
    container.executor = Executor()

    from scripts.graph.workflow import create_graph

    container.graph = create_graph(
        planner=container.planner,
        executor=container.executor
    )
