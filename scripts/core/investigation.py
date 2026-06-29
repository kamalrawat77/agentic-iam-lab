from dataclasses import dataclass, field

from scripts.core.context import ExecutionContext

@dataclass
class Investigation:

    question: str

    plan: list = field(default_factory=list)

    context: ExecutionContext | None = None

    status: str = "CREATED"

    results: list = field(default_factory=list)

    errors: list = field(default_factory=list)