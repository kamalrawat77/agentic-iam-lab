import inspect
from scripts.tools.validator import validate
from scripts.tools.registry import registry
import time
from scripts.core.context import ExecutionContext

class Executor:
    def execute(self, investigation):
        evidence = []
        investigation.context = ExecutionContext(
            question=investigation.question
        )
        plan=investigation.plan
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
              result = tool.function(context=investigation.context,**arguments)
              
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
        investigation.results.append(evidence)
        return #evidence
