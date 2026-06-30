from dataclasses import dataclass

@dataclass
class WorkflowNode:
    name: str
    action: callable

@dataclass
class WorkflowEdge:
    source: str
    target: str
    condition: callable | None = None

class Workflow:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, source, target):
        self.edges.append(
            WorkflowEdge(source, target)
        )