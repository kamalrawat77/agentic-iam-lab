from dataclasses import dataclass, field
import uuid

@dataclass
class ExecutionContext:

    execution_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    question: str = ""

    tool_results: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)

    errors: list = field(default_factory=list)