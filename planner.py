from task import Task

class Planner:
    def __init__(self):
        """
        TODO: initialize an empty list to hold tasks.
        Also initialize a counter for generating task IDs (starts at 1).
        """
        pass

    def add_task(self, title, deadline, priority):
        """
        TODO: create a new Task using the next available id,
        append it to your task list, increment the id counter.
        Return the new task (useful for confirming to the user what got added).
        """
        pass

    def remove_task(self, task_id):
        """
        TODO: find the task with this id and remove it from the list.
        What should happen if no task with that id exists? Decide, and
        handle it — don't let it silently crash.
        """
        pass

    def mark_task_complete(self, task_id):
        """
        TODO: find the task by id, call its mark_complete() method.
        """
        pass

    def get_all_tasks(self):
        """
        TODO: return the full list of tasks.
        """
        pass

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