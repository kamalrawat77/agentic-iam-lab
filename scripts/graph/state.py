from typing import TypedDict

from scripts.core.investigation import Investigation

class AgentState(TypedDict):

    investigation: Investigation