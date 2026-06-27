from inspect import signature
from scripts.tools.registry import registry
from scripts.tools.tool import Tool

def tool(description: str, category: str):

    def decorator(func):

        sig = signature(func)

        parameters = {}

        for name, param in sig.parameters.items():

            parameters[name] = {
                "type": "string",   # We'll improve this in Nugget 052
                "default": (
                    None if param.default is param.empty else param.default
                )
            }

        tool_obj = Tool(
            name=func.__name__,
            description=description,
            category=category,
            function=func,
            parameters=parameters
        )

        registry.register(tool_obj)

        return func

    return decorator