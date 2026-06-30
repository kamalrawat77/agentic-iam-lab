from scripts.tools.decorators import tool
from scripts.core.context import ExecutionContext

@tool(
    description="Find dormant accounts",
    category="Identity"
)
def dormant_accounts(
    context: ExecutionContext,
    days: int = 90,
    include_privileged: bool = False,
    department: str = "Finance"
):
    result = {
        "count": 42,
        "days": days
    }

    context.tool_results["dormant_accounts"] = result

    return result