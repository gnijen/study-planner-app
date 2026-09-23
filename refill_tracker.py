from med_refill import MedRefill
from datetime import datetime
from datetime import date

class RefillTracker:
    def __init__(self):
        self.medicines = []
        self.next_meds_id = 1

    def add_medication(self, user_id, medication_name, dosage, instructions, last_refill_date, days_per_supply, refills_remaining):
        m = MedRefill(self.next_meds_id, user_id, medication_name, dosage, instructions, last_refill_date, days_per_supply, refills_remaining)
        self.medicines.append(m)
        self.next_meds_id += 1
        return m

    def get_all_medicines(self):
        return self.medicines

    def meds_needing_attention(self):
        return [medication for medication in self.medicines if (date.today()) >= medication.alert_date()]


    # def remove_task(self, task_id):
    #     found = False
    #     for task in self.tasks:
    #         if task.task_id == task_id:
    #             self.tasks.remove(task)
    #             found = True
    
    #     if not found:
    #         return "No task found with the given ID"


    # def mark_task_complete(self, task_id):
    #     found = False
    #     for task in self.tasks:
    #         if task.task_id == task_id:
    #             task.mark_complete()
    #             found = True
    #     if not found:
    #         return "No task found with the given ID"









      
