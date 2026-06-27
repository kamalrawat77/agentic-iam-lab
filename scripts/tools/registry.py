from scripts.tools.tool import Tool
from scripts.tools.identity_tools import dormant_accounts

TOOLS = {
    "dormant_accounts": Tool(
        name="dormant_accounts",
        description="Find dormant accounts",
        category="Identity",
        version="1.0",
        risk="Low",
        function=dormant_accounts,
        parameters={
            "days": {
                "type": "integer",
                "default": 90
            }
        }
    )
}