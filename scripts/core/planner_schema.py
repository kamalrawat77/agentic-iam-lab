from pydantic import BaseModel, Field


class PlannedStepOutput(BaseModel):
    """Expected structure of one LLM-generated plan step."""

    tool: str = Field(
        description="Name of a registered tool"
    )
    purpose: str = Field(
        description="Why this tool is needed"
    )
    description: str = Field(
        description="What the tool should do"
    )
    arguments: dict = Field(
        default_factory=dict,
        description="Arguments to pass to the tool"
    )


class PlannerResponse(BaseModel):
    """Expected structure of the complete planner response."""

    investigation: str = Field(
        description="The goal of the investigation"
    )
    steps: list[PlannedStepOutput] = Field(
        description="Ordered steps to investigate the question"
    )