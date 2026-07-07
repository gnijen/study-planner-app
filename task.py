class Task:
    def __init__(self, task_id, title, deadline, priority):
        """
        Initialize a Task.
        
        TODO: store all four+ attributes on self.
        Remember: completed should default to False here — it's not a parameter,
        because a brand-new task is never already done.
        """
        pass

    def mark_complete(self):
        """
        TODO: flip self.completed to True.
        Think about why this is a method on Task rather than something
        Planner does by reaching into task.completed directly.
        """
        pass

    def to_dict(self):
        """
        TODO: return this task as a plain dictionary.
        Why do we need this? Because JSON doesn't know how to save a
        custom Python object — it only understands dicts, lists, strings,
        numbers, booleans. This method is the translator.
        """
        pass

    @staticmethod
    def from_dict(data):
        """
        TODO: given a dictionary (like the one to_dict produces),
        build and return a Task object.
        This is the reverse translator — dict back into object.
        """
        pass

    def __str__(self):
        """
        TODO: return a human-readable string like:
        "[✓] (1) Finish resume — due 2026-07-15 — HIGH"
        This is what the user actually sees when tasks are listed.
        """
        pass