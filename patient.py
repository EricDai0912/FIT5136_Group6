from inbox import Inbox

class Patient:
    def __init__(self, 
                 inbox: Inbox = None,
                 first_name: str = None, 
                 last_name: str = None,
                 email: str = None, 
                 password: str = None, 
                 date_of_birth: str = None, 
                 gender: str = None,
                 phone_number: str = None, 
                 address: str = None):
        
        self.inbox = inbox
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
    