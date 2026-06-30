from scripts.tools.decorators import tool
from scripts.core.context import ExecutionContext

@tool(
    description="Show department breakdown",
    category="Analytics"
)
def department_breakdown(context: ExecutionContext):

    dormant = context.tool_results["dormant_accounts"]

    result = {
        "Engineering": 20,
        "Finance": 10,
        "HR": 12,
        "dormant" : dormant
    }

    context.tool_results["department_breakdown"] = result


    return result



#def trend_analysis():
#    return "Dormant accounts increased from 20 to 27"
