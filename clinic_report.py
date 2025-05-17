class ClinicReport:
    def __init__(self, clinic_name, total_patients,
                 appts_per_gp, reasons, peak_hours):
        self.clinic_name    = clinic_name
        self.total_patients = total_patients
        self.appts_per_gp   = appts_per_gp 
        self.reasons        = reasons      
        self.peak_hours     = peak_hours 

    def to_print_dict(self):
        return {
            'Clinic Name':        self.clinic_name,
            'Total Patients':     str(self.total_patients),
            'Appointments per GP':       ', '.join(f"{gp}({cnt})"
                                            for gp, cnt in sorted(self.appts_per_gp.items())),
            'Reasons':            ', '.join(sorted(self.reasons)),
            'Peak Hours':         ', '.join(self.peak_hours)
        }