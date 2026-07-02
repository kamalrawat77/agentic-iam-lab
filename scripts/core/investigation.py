from dataclasses import dataclass, field
from scripts.core.context import ExecutionContext
from scripts.core.plan import Plan
from scripts.core.status import InvestigationStatus

@dataclass
class Investigation:

    question: str

    plan: Plan | None = None

    context: ExecutionContext | None = None

    status: InvestigationStatus | None = None

    results: list = field(default_factory=list)

    errors: list = field(default_factory=list)