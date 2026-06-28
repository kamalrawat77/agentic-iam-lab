from inspect import signature
from scripts.tools.registry import registry
from scripts.tools.tool import Tool

def tool(description: str, category: str):
    
    TYPE_MAP = {
        int: "integer",
        float: "number",
        bool: "boolean",
        str: "string",
        list: "array",
        dict: "object"
    }

    def decorator(func):
        sig = signature(func)
        
        parameters = {}
        
        for name, param in sig.parameters.items():
        
            annotation = param.annotation
        
            json_type = TYPE_MAP.get(annotation, "string")
        
            required = param.default is param.empty
        
            default = None if required else param.default
        
            parameters[name] = {
                "type": json_type,
                "required": required,
                "default": default
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