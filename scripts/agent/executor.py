import inspect
from scripts.tools.validator import validate
from scripts.tools.registry import registry
import time

class Executor:
    def execute(self, plan):
        evidence = []
        for step in plan["steps"]:
          tool_name = step["tool"]
          #tool = TOOLS[tool_name]  
          tool = registry.get(tool_name)
          if tool is None:
            evidence.append({
                "tool": tool_name,
                "status": "FAILED",
                "reason": "Tool not found"
            })
            continue  
          start = time.time()          
          print(f"Executing: {tool_name}")          
          try:  
              args=inspect.signature(tool.function)
              #print(args)
              arguments = step.get("arguments", {})
              validate(tool, arguments)
              result = tool.function(**arguments)
              valid_parameters = tool.parameters.keys()
              for parameter in arguments:
                if parameter not in valid_parameters:
                  raise ValueError(
                      f"Unknown parameter {parameter}"
                  )
              result = tool.function()
              status = "SUCCESS"
              print(f"Completed: {tool_name}")          
          except Exception as e:
              result = str(e)
              status = "FAILED"
              print(f"Error Executing: {tool_name}")
          duration = time.time() - start
          evidence.append(
              {     
                  "tool": tool.name,      
                  "purpose": step["purpose"],   
                  "status": status,
                  "result": result,
                  "execution_time": round(duration, 3)
              }
          )
        return evidence
