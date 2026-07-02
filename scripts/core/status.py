from enum import Enum

class InvestigationStatus(Enum):

    CREATED = "CREATED"

    PLANNED = "PLANNED"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"