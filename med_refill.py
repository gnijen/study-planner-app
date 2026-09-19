from datetime import date, timedelta
class MedRefill:
    def __init__(self, refill_id, user_id, medication_name, dosage, instructions, last_refill_date, days_per_supply, refills_remaining ):
        self.refill_id = refill_id
        self.user_id = user_id
        self.medication_name = medication_name
        self.dosage = dosage
        self.instructions = instructions
        self.last_refill_date = last_refill_date
        self.days_per_supply = days_per_supply
        self.refills_remaining = refills_remaining

    def alert_date(self):
        alert_time = timedelta(days = 14)
        supply_length = timedelta(days = self.days_per_supply)
        alert = (self.last_refill_date + supply_length) - alert_time
        return alert
    def alert_message(self):
        



#     @staticmethod
#     def from_dict(data):
#         task_id = data.get("task_id")
#         title = data.get("title")
#         deadline = data.get("deadline")
#         priority = data.get("priority")
        

#         # new_task = Task(task_id, title, deadline, priority)
#         # new_task.completed = data.get("completed")

#         return new_task
    
#     def __str__(self):
#         check = "✓" if self.completed else " "
#         return f"[{check}] ({self.task_id}) {self.title} - due {self.deadline} - {self.priority}"



        


