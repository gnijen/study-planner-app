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
        if self.refills_remaining == 0:
            return f"Please book your doctor's appointment for prescription/medication refill. Your {self.medication_name} is running low."
        else:
            return f"Please contact your pharmacy for your {self.medication_name} refill. Your medication is running low."


    @staticmethod
    def from_dict(data):
        refill_id = data.get("refill_id")                                       
        user_id = data.get("user_id")
        medication_name = data.get("medication_name")
        dosage = data.get("dosage")
        instructions = data.get("instructions")
        last_refill_date = date.fromisoformat(data.get("last_refill_date"))
        days_per_supply = data.get("days_per_supply")
        refills_remaining = data.get("refills_remaining")

        return MedRefill(refill_id, user_id, medication_name, dosage, instructions, last_refill_date, days_per_supply, refills_remaining)

        
    
#     def __str__(self):
#         check = "✓" if self.completed else " "
#         return f"[{check}] ({self.task_id}) {self.title} - due {self.deadline} - {self.priority}"



        


