from patient import Patient
from administrator import Administrator
from file_handler import FileIO
from gp import GP
from clinic import Clinic
from appointment import Appointment
import datetime

class MPMS:

    def __init__(self):
        self.patients = FileIO.read_patients_csv()
        self.gps = FileIO.read_gps_csv()
        self.clinics = FileIO.read_clinics_csv()
        self.appointments = FileIO.read_appointments_csv()
        self.administrator = Administrator()
    
    def get_previous_appointments(self, email):
        today = datetime.date.today()
        previous_appointments = {appointment_id:appointment for appointment_id, appointment in self.appointments.items() if appointment.patient_email == email and appointment.date < today}
        return previous_appointments
    
    def get_upcoming_appointments(self, email):
        today = datetime.date.today()
        upcoming_appointments = {appointment_id:appointment for appointment_id, appointment in self.appointments.items() if appointment.patient_email == email and appointment.date >= today}
        return upcoming_appointments
    
    def get_available_appointments_by_gp_id(self, idx):
        gp_id = list(self.gps.values())[idx - 1].gp_id
        available_appointments = {appointment_id:appointment for appointment_id, appointment in self.appointments.items() if appointment.availability and appointment.gp_id == gp_id}
        return available_appointments

    def get_available_appointments_by_date(self, date):
        available_appointments = {appointment_id:appointment for appointment_id, appointment in self.appointments.items() if appointment.availability and appointment.date == date}
        return available_appointments
    
    def get_available_appointments_by_clinic_suburb(self, suburb):
        available_appointments = {appointment_id:appointment for appointment_id, appointment in self.appointments.items() if appointment.availability and appointment.clinic_suburb == suburb}
        return available_appointments
    
    def get_available_appointments(self):
        available_appointments = {appointment_id:appointment for appointment_id, appointment in self.appointments.items() if appointment.availability}
        return available_appointments
    
    def get_appointments_by_gp_id_clinic_id(self, gid, cid):
        matched_appointments = {appointment_id:appointment for appointment_id, appointment in self.appointments.items() if appointment.gp_id == gid and appointment.clinic_id == cid}
        return matched_appointments
    
    def get_gps_by_clinic_id(self, cid):
        matched_gps = {gp.gp_id:gp for gp in self.gps.values() if cid in gp.clinic_ids}
        return matched_gps

    def get_clinics_by_clinic_suburb(self, suburb):
        matched_clinics = {cid:clinic for cid, clinic in self.clinics.items() if clinic.clinic_suburb == suburb}
        return matched_clinics
    
    def check_patient_booking_access(self, email):
        patient = self.patients[email]
        today = datetime.date.today()
        if today == patient.last_booking_date:
            return False
        else:
            return True
    
    def check_appointment_conflict(self, gp_id, new_start_dt, new_end_dt):
        for appointment in self.appointments.values():
            if appointment.gp_id == gp_id and appointment.date == new_start_dt.date():
                existing_start_dt = datetime.datetime.combine(appointment.date, appointment.time)
                existing_end_dt = existing_start_dt + datetime.timedelta(minutes=appointment.duration)
                if new_start_dt < existing_end_dt and existing_start_dt < new_end_dt:
                    return True
        return False

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

    def create_gp(self, first_name, last_name, email, clinic_ids, clinic_names, specialisation,
                days_off):
        try:
            new_gp = GP(
                gp_id=None,
                first_name=first_name,
                last_name=last_name,
                email=email,
                clinic_ids=clinic_ids,
                clinic_names=clinic_names,
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
            raise ValueError(f"Failed to Greate gp: {e}")
    
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
                   
    def update_gp(self, gp):
        try:
            self.gps[gp.gp_id] = gp
            self.save_data('G')
        except Exception as e:
            raise ValueError(f"Failed to update clinic: {e}")
    
    def create_appointment(self, gp_id, clinic_id, date, time, duration):
        try:
            new_appointment = Appointment(
                appointment_id=None,
                gp_id=gp_id,
                clinic_id=clinic_id,
                clinic_name=self.clinics[clinic_id].clinic_name,
                gp_name=f"{self.gps[gp_id].first_name} {self.gps[gp_id].last_name}",
                clinic_suburb=self.clinics[clinic_id].clinic_suburb,
                date=date,
                time=time,
                duration=duration
            )
        except Exception as e:
            raise ValueError(f"Failed to Greate appointment: {e}")
        
        self.appointments[new_appointment.appointment_id] = new_appointment
        self.save_data('AP')
    
    def delete_appointment(self, appointment_id):
        try:
            del self.appointments[appointment_id]
            self.save_data('AP')
        except Exception as e:
            raise ValueError(f"Failed to delete appointment: {e}")
    
    def update_appointment(self, appointment):
        try:
            self.appointments[appointment.appointment_id] = appointment
            self.save_data('AP')
        except Exception as e:
            raise ValueError(f"Failed to update appointment: {e}")
    
    def cancel_appointment(self, appointment_id, email):
        try:
            appointment = self.appointments[appointment_id]
            appointment.patient_email = None
            appointment.patient_name = ""
            appointment.availability = True
            appointment.reason = ""
            if self.patients[email].last_booking_date == datetime.date.today():
                self.patients[email].last_booking_date = None
            self.save_data('AP')
        except Exception as e:
            raise ValueError(f"Failed to cancel appointment: {e}")
    
    def release_appointment(self, appointment_id):
        try:
            appointment = self.appointments[appointment_id]
            appointment.patient_email = None
            appointment.patient_name = ""
            appointment.availability = True
            appointment.reason = ""
            self.save_data('AP')
        except Exception as e:
            raise ValueError(f"Failed to release appointment: {e}")
    
    def book_appointment(self, appointment_id, email, reason):
        try:
            appointment = self.appointments[appointment_id]
            appointment.patient_email = email
            appointment.patient_name = f"{self.patients[email].first_name} {self.patients[email].last_name}"
            appointment.availability = False
            appointment.reason = reason
            self.patients[email].last_booking_date = datetime.date.today()
            self.save_data('AP')
        except Exception as e:
            raise ValueError(f"Failed to book appointment: {e}")
    
    def save_data(self, code):
        if code == 'P' or code == 'A':
            FileIO.write_patients_csv(self.patients)
        if code == 'G' or code == 'A':
            FileIO.write_gps_csv(self.gps)
        if code == 'C' or code == 'A':
            FileIO.write_clinics_csv(self.clinics)
        if code == 'AP' or code == 'A':
            FileIO.write_appointments_csv(self.appointments)