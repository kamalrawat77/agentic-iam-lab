class Application:

    def __init__(self):

        self.registry = None
        self.planner = None
        self.executor = None
        self.graph = None


    def initialize(self):

        import scripts.tools
        from scripts.tools.registry import registry
        from scripts.agent.planner import Planner
        from scripts.agent.executor import Executor
        from scripts.graph.workflow import create_graph

        self.registry = registry
        self.planner = Planner(registry)
        self.executor = Executor()

        

        self.graph = create_graph(
            planner=self.planner,
            executor=self.executor
        )

app = Application()