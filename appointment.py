import uuid
import datetime

class Appointment:
    def __init__(self,
                 appointment_id: str = None,
                 patient_email: str = None,
                 patient_name: str = "",
                 gp_id: str = None,
                 clinic_id: str = None,
                 clinic_name: str = None,
                 gp_name: str = None,
                 clinic_suburb: str = None,
                 date: datetime.date = None,     
                 time: datetime.time = None,      
                 duration: int = 0,
                 availability: bool = True,             
                 reason: str = None):
        self.appointment_id  = appointment_id or str(uuid.uuid4())
        self.patient_email      = patient_email
        self.patient_name    = patient_name
        self.gp_id           = gp_id
        self.clinic_id       = clinic_id
        self.clinic_name     = clinic_name
        self.gp_name         = gp_name
        self.clinic_suburb   = clinic_suburb
        self.date            = date
        self.time            = time
        self.duration        = duration
        self.availability    = availability
        self.reason          = reason

    def to_dict(self):
        return {
            'appointment_id':  self.appointment_id,
            'patient_email':      self.patient_email,
            'patient_name':    self.patient_name,
            'gp_id':           self.gp_id,
            'clinic_id':       self.clinic_id,
            'clinic_name':     self.clinic_name,
            'gp_name':         self.gp_name,
            'clinic_suburb':   self.clinic_suburb,
            'date':            self.date,       # "dd/mm/yyyy"
            'time':            self.time, # "HH:MM"
            'duration':        self.duration,
            'availability':    self.availability,
            'reason':          self.reason
        }
    
    def to_print_dict(self):
        return {
            'patient_name':    self.patient_name,
            'clinic_name':     self.clinic_name,
            'gp_name':         self.gp_name,
            'clinic_suburb':   self.clinic_suburb,
            'date':            self.date,       # "dd/mm/yyyy"
            'time':            self.time, # "HH:MM"
            'duration':        self.duration,
            'availability':    self.availability,
            'reason':          self.reason
        }