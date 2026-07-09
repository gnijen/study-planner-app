class Task:
    def __init__(self, task_id, title, deadline, priority):
        self.task_id = task_id
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):

        return {"task_id": self.task_id,
        "title" : self.title,
        "deadline" : self.deadline,
       "priority":  self.priority,
        "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        task_id = data.get("task_id")
        title = data.get("title")
        deadline = data.get("deadline")
        priority = data.get("priority")
        

        new_task = Task(task_id, title, deadline, priority)
        new_task.completed = data.get("completed")

        return new_task
    
    def __str__(self):
        check = "✓" if self.completed else " "
        return f"[{check}] ({self.task_id}) {self.title} - due {self.deadline} - {self.priority}"



        


