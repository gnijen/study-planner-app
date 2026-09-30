from lab_record import LabRecord

class LabTracker:
    def __init__(self):
        self.lab_records = []
        self.next_record_id = 1

    def add_lab_records(self, user_id, test_name, value, test_date, reference_low, reference_high, doctor_notes):
            l = LabRecord(self.next_record_id, user_id, test_name, value, test_date, reference_low, reference_high, doctor_notes)
            self.lab_records.append(l)
            self.next_record_id += 1
            return l