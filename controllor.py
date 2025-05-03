from patient import Patient
from administrator import Administrator
from file_handler import FileIO
from gp import GP
from clinic import Clinic

class MPMS:

    def __init__(self):
        self.patients = FileIO.read_patients_csv()
        self.gps = FileIO.read_gps_csv()
        self.clinics = FileIO.read_clinics_csv()
        self.administrator = Administrator()

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
        self.save_data('P')


    def login_patient(self, email, password):

        if not self.is_patient_exist(email):
            raise ValueError("Email not registered")

        patient = self.patients[email]
        if patient.password != password:
            raise ValueError("Incorrect password")

        return patient
    
    def login_admin(self, email, password):

        if self.administrator.email != email:
            raise ValueError("Incorrect Admin Email")

        if self.administrator.password != password:
            raise ValueError("Incorrect password")

        return self.administrator

    def create_clinic(self, clinic_name, clinic_suburb, clinic_services,
                    clinic_openning_hours):
        try:
            new_clinic = Clinic(
                clinic_id=None,
                clinic_name=clinic_name,
                clinic_suburb=clinic_suburb,
                clinic_services=clinic_services,
                clinic_openning_hours=clinic_openning_hours
            )
        except Exception as e:
            raise ValueError(f"Failed to Greate gp: {e}")
        
        self.clinics[new_clinic.clinic_id] = new_clinic
        self.save_data('C')
    
    def delete_clinic(self, clinic_id):
        try:
            del self.clinics[clinic_id]
            self.save_data('C')
        except Exception as e:
            raise ValueError(f"Failed to delete clinic: {e}")
    
    def update_clinic(self, clinic):
        try:
            self.clinics[clinic.clinic_id] = clinic
            self.save_data('C')
        except Exception as e:
            raise ValueError(f"Failed to update clinic: {e}")

    def create_gp(self, first_name, last_name, email, clinics, specialisation,
                days_off):
        try:
            new_gp = GP(
                gp_id=None,
                first_name=first_name,
                last_name=last_name,
                email=email,
                clinics=clinics,
                specialisation=specialisation,
                days_off=days_off,
            )
        except Exception as e:
            raise ValueError(f"Failed to Greate gp: {e}")
        
        self.gps[new_gp.gp_id] = new_gp
        self.save_data('G')

    def delete_gp(self, gp_id):
        try:
            del self.gps[gp_id]
            self.save_data('G')
        except Exception as e:
            raise ValueError(f"Failed to update gp: {e}")
                   
    def update_gp(self, gp):
        try:
            self.gps[gp.gp_id] = gp
            self.save_data('G')
        except Exception as e:
            raise ValueError(f"Failed to update clinic: {e}")
    








    def save_data(self, code):
        if code == 'P' or code == 'A':
            FileIO.write_patients_csv(self.patients)
        if code == 'G' or code == 'A':
            FileIO.write_gps_csv(self.gps)
        if code == 'C' or code == 'A':
            FileIO.write_clinics_csv(self.clinics)