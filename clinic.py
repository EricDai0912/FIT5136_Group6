import uuid
class Clinic:

    def __init__(self,
                clinic_id,
                clinic_name,
                clinic_suburb,
                clinic_services,
                clinic_openning_hours):
        self.clinic_id = clinic_id if clinic_id is not None else str(uuid.uuid4())
        self.clinic_name = clinic_name
        self.clinic_suburb = clinic_suburb
        self.clinic_services = clinic_services
        self.clinic_openning_hours = clinic_openning_hours
    
    def to_dict(self):
        return {
            'clinic_id': self.clinic_id,
            'clinic_name': self.clinic_name,
            'clinic_suburb': self.clinic_suburb,
            'clinic_services': self.clinic_services,
            'clinic_openning_hours': self.clinic_openning_hours,
        }