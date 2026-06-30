from dataclasses import dataclass, field

@dataclass
class PlanStep:

    tool: str
    purpose: str
    description: str
    arguments: dict = field(default_factory=dict)

    def __post_init__(self):

        if not self.tool:
            raise ValueError("Tool name cannot be empty")

        if not self.purpose:
            raise ValueError("Purpose cannot be empty")


from scripts.core.plan import PlanStep

@dataclass
class Plan:

    goal: str

    steps: list[PlanStep] = field(default_factory=list)