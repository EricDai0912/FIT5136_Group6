import datetime

class Patient:
    def __init__(self, 
                 first_name: str = None, 
                 last_name: str = None,
                 email: str = None, 
                 password: str = None, 
                 date_of_birth: str = None, 
                 gender: str = None,
                 phone_number: str = None, 
                 address: str = None,
                 notification: str = None,
                 last_booking_date: datetime.date = None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.notification = notification
        self.last_booking_date = last_booking_date
    
    def to_dict(self):
        return {
            'email':         self.email,
            'password':      self.password,
            'first_name':    self.first_name,
            'last_name':     self.last_name,
            'date_of_birth': self.date_of_birth,
            'gender':        self.gender,
            'phone_number':  self.phone_number,
            'address':       self.address,
            'notification':  self.notification,
            'last_booking_date': self.last_booking_date
        }