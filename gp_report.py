class GPReport:
    def __init__(self, gp_name, clinic_suburb, total_patients, reasons):
        self.gp_name = gp_name
        self.clinic_suburb = clinic_suburb
        self.total_patients = total_patients
        self.reasons = reasons

    def to_print_dict(self):
        return {
            'GP Name':        self.gp_name,
            'Clinic Suburb':  self.clinic_suburb,
            'Total Patients': str(self.total_patients),
            'Reasons':        ', '.join(sorted(self.reasons))
        }
