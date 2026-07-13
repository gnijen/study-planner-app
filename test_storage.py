from planner import Planner
from storage import save_tasks, load_tasks

# Create a planner, add some tasks, mark one complete
p = Planner()
p.add_task("Buy groceries", "2026-07-16", "HIGH")
p.add_task("Read a chapter", "2026-07-20", "LOW")
p.mark_task_complete(1)

print("Before saving:")
for task in p.get_all_tasks():
    print(task)

# Save to disk
save_tasks(p.get_all_tasks())

# Simulate a fresh program run — load back from disk
loaded_tasks = load_tasks()

print("\nAfter loading from disk:")
for task in loaded_tasks:
    print(task)