from task import Task

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
        




        """
        TODO: return only tasks where completed is False.
        This is a one-line list comprehension — you've done these before.
        """
        pass

    def prioritize(self):
        """
        THIS IS THE 'AI-adjacent' LOGIC — your sorting/ranking engine.
        
        TODO: return the pending tasks sorted so the most urgent task
        comes first.
        
        Think about what 'urgent' means here. Two candidate approaches:
        (a) Sort purely by deadline (earliest first).
        (b) Sort by a combined score of deadline closeness AND priority
            level, so a HIGH priority task due in 5 days might rank
            above a LOW priority task due in 2 days.
        
        Approach (b) is what makes this feel 'smart' instead of just
        'sorted.' You decide the formula. A simple starting point:
        score = days_until_deadline - (priority_weight * some_constant)
        then sort ascending by score.
        
        This is also your first real use of Big O outside LeetCode —
        what's the time complexity of sorting n tasks? Say it out loud
        before you move on.
        """
        pass