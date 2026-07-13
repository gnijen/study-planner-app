import json
import os
from task import Task

def save_tasks(tasks, filepath="data/tasks.json"):
    
    task_dicts = [task.to_dict() for task in tasks]
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as f:
        json.dump(task_dicts, f)





def load_tasks(filepath="data/tasks.json"):
    if not os.path.exists(filepath):
        return []
    
    with open(filepath, "r") as f:
        task_dicts = json.load(f)
    
    tasks = [Task.from_dict(d) for d in task_dicts]
    return tasks
    
    
