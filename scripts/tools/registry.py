from scripts.tools.tool import Tool
from scripts.tools.identity_tools import dormant_accounts
from scripts.tools.analytics_tools import trend_analysis
from scripts.tools.incident_tools import search_history

TOOLS = {

    "dormant_accounts": Tool(
        "dormant_accounts",
        "Returns dormant account metrics",
        dormant_accounts
    ),

    "trend_analysis": Tool(
        "trend_analysis",
        "Analyzes trends",
        trend_analysis
    ),

    "search_history": Tool(
        "search_history",
        "Search historical investigations",
        search_history
    )

}
