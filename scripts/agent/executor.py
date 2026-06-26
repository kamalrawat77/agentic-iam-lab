from scripts.tools.registry import TOOLS
import time

class Executor:
    def execute(self, plan):
        evidence = []
        for step in plan["steps"]:
          start = time.time()
          tool_name = step["tool"] 
          print(f"Executing: {tool_name}")
          tool = TOOLS[tool_name]      
          result = tool.function()   
          print(f"Completed: {tool_name}")
          duration = time.time() - start
          evidence.append(
              {     
                  "tool": tool.name,      
                  "purpose": step["purpose"],      
                  "result": result,
                  "execution_time": duration
              }
          )
        return evidence
