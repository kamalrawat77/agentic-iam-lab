from dataclasses import dataclass, field
from scripts.core.context import ExecutionContext
from scripts.core.plan import Plan

@dataclass
class Investigation:

    question: str

    plan: Plan | None = None

    context: ExecutionContext | None = None

    status: str = "CREATED"

    results: list = field(default_factory=list)

    errors: list = field(default_factory=list)