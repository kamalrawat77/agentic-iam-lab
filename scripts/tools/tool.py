from dataclasses import dataclass, field
from typing import Callable

@dataclass
class Tool:

    name: str
    description: str
    category: str
    function: Callable
    version: str = "1.0"
    risk: str = "Low"
    parameters: dict = field(default_factory=dict)