import uuid
class GP:

    def __init__(self,
                gp_id,
                first_name,
                last_name,
                email,
                clinic_ids,
                clinic_names,
                specialisation,
                days_off):
        self.gp_id = gp_id if gp_id is not None else str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.clinic_ids = clinic_ids
        self.clinic_names = clinic_names
        self.specialisation = specialisation
        self.days_off = days_off
    
    def to_dict(self):
        return {
            'gp_id': self.gp_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'clinic_ids': self.clinic_ids,
            'clinic_names': self.clinic_names,
            'specialisation': self.specialisation,
            'days_off': self.days_off
        }
    
    def to_print_dict(self):
        return {
            'First name': self.first_name,
            'Last name': self.last_name,
            'Email': self.email,
            'Clinics': self.clinic_names,
            'Specialisation': self.specialisation,
            'Days off': self.days_off
        }