from scripts.tools.decorators import tool

@tool(
    description="Find dormant accounts",
    category="Identity"
)
def dormant_accounts(
    days: int = 90,
    include_privileged: bool = False,
    department: str = "Finance"
):
    return {}