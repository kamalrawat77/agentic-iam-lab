from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Tool:
    name: str
    description: str
    category: str
    version: str
    risk: str
    function: Callable
    parameters: Optional[dict] = None