from task import Task
from datetime import datetime

class Planner:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, deadline, priority):
        t = Task(self.next_id,  title, deadline, priority)
        self.tasks.append(t)
        self.next_id += 1

        return t


    def remove_task(self, task_id):
        found = False
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                found = True
    
        if not found:
            return "No task found with the given ID"


    def mark_task_complete(self, task_id):
        found = False
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_complete()
                found = True
        if not found:
            return "No task found with the given ID"


    def get_all_tasks(self):
        return self.tasks

    def get_pending_tasks(self):
        return [task for task in self.tasks if task.completed == False]



    def prioritize(self):
        priority_weights = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
        constant = 3

        def get_score(task):
            today = datetime.now()
            deadline_date = datetime.strptime(task.deadline, "%Y-%m-%d")
            days_until = (deadline_date - today).days
            weight = priority_weights[task.priority]
            score = days_until - (weight * constant)
            return score

        pending = self.get_pending_tasks()
        return sorted(pending, key=get_score)








      
