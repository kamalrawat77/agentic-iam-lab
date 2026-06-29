from inspect import signature
from scripts.tools.registry import registry
from scripts.tools.tool import Tool

TYPE_MAP = {
        int: "integer",
        float: "number",
        bool: "boolean",
        str: "string",
        list: "array",
        dict: "object"
    }
    
FRAMEWORK_PARAMETERS = {
    "context"
}    
def tool(description: str, category: str):
    
    def decorator(func):
        print(f"Decorator executed for {func.__name__}")
        sig = signature(func)
        
        parameters = {}
        
        for name, param in sig.parameters.items():
            if name in FRAMEWORK_PARAMETERS:
              continue

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
        print("Registered", func.__name__)
        return func

    return decorator