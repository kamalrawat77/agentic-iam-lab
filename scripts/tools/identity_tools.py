from scripts.tools.decorators import tool

@tool(
    description="Find dormant accounts",
    category="Identity"
)
def dormant_accounts(days=90):

    return {
        "days": days,
        "count": 42
    }