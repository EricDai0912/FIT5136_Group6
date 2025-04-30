import uuid
class GP:

    def __init__(self,
                gp_id,
                first_name,
                last_name,
                email,
                clinics,
                specialisation,
                days_off):
        self.gp_id = gp_id if gp_id is not None else str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.clinics = clinics
        self.specialisation = specialisation
        self.days_off = days_off
    
    def to_dict(self):
        return {
            'gp_id': self.gp_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'clinics': self.clinics,
            'specialisation': self.specialisation,
            'days_off': self.days_off
        }