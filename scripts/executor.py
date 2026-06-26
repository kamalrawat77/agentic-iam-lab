import time

def execute_plan(plan, tools):
    
    evidence = []
    for step in plan["steps"]:
        start = time.time()
        tool_name = step["tool"]
        print(f"Executing: {tool_name}")
        result = tools[tool_name]()
        print(f"Completed: {tool_name}")
        duration = time.time() - start
        evidence.append({
            "tool": tool_name,
            "purpose": step["purpose"],
            "result": result,
            "execution_time": duration
        })
    return evidence
