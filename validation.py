import re
import datetime

class Validation:

    @staticmethod
    def is_valid_email(email: str):
        return email.endswith("@student.monash.edu") or email.endswith("@staff.monash.edu")
    
    @staticmethod
    def is_gp_valid_email(email: str) -> bool:
        return "@" in email and "." in email
    
    @staticmethod
    def is_valid_password(password: str):

        if len(password) < 8:
            return "ERROR: Less than eight characters!"
        if not any(c.isupper() for c in password):
            return "ERROR: No Uppercase!"
        if not any(c.isdigit() for c in password):
            return "ERROR: No number!"

        return ""
    
    @staticmethod
    def is_valid_gender(gender: str):
        if gender == 'F' or gender == 'M' or gender == 'O' or gender == 'N':
            return True
        else:
            return False
    
    @staticmethod
    def is_empty(s: str):
        if s == "" or s is None:
            return True
        else:
            return False
    
    @staticmethod
    def is_valid_date(dob: str):
        pattern = r'^\d{2}/\d{2}/\d{4}$'
        if not re.match(pattern, dob):
            return False

        day, month, year = map(int, dob.split('/'))

        if not (1 <= day <= 31):
            return False
        if not (1 <= month <= 12):
            return False
        if not (1000 <= year <= 9999):
            return False

        return True

    @staticmethod
    def is_valid_time(time_str):
        try:
            datetime.time.fromisoformat(time_str)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_phone(phone: str):
        pattern = r'^4\d{8}$'
        return re.match(pattern, phone) is not None