from scripts.tools.tool import Tool


class ToolRegistry:

    def __init__(self):
        self._tools = {}

    def register(self, tool: Tool):
      self._tools[tool.name] = tool

    def get(self, tool_name):
      return self._tools.get(tool_name)

    def list_for_planner(self):
      planner_tools = []
      for tool in self._tools.values():
          planner_tools.append({
              "name": tool.name,
              "description": tool.description,
              "category": tool.category

          })
      return planner_tools

    def exists(self, tool_name):
      raise ValueError(
          f"Planner returned unknown tool: {tool_name}"
      )

registry = ToolRegistry()

from scripts.tools.identity_tools import dormant_accounts

registry.register(
        Tool(
    name="dormant_accounts",
    description="Find dormant accounts",

    category="Identity",

    function=dormant_accounts,

    parameters={
        "days":{
            "type":"integer",
            "description":"Minimum inactivity period",
            "default":90
        }
    }
)
    )
    