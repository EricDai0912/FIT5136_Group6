from patient import Patient

class MPMS:

    def __init__(self):
        self.patients = {}

    def is_patient_exist(self, email):
        return email in self.patients

    def register_patient(
                            self,
                            email,
                            password,
                            first_name,
                            last_name,
                            date_of_birth,
                            gender,
                            phone_number,
                            address
                        ):
        if self.is_patient_exist(email):
            raise ValueError("Email already registered")

        try:
            new_patient = Patient(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                gender=gender,
                phone_number=phone_number,
                address=address
            )
        except Exception as e:
            raise ValueError(f"Failed to register patient: {e}")

        self.patients[new_patient.email] = new_patient

    def login_patient(self, email, password):

        if not self.is_patient_exist(email):
            raise ValueError("Email not registered")

        patient = self.patients[email]
        if patient.password != password:
            raise ValueError("Incorrect password")

        return patient
