from .tool import Tool

from .identity_tools import dormant_accounts

TOOLS = {

    "dormant_accounts":

        Tool(

            name="dormant_accounts",

            description="Returns dormant accounts",

            function=dormant_accounts
        )
}
