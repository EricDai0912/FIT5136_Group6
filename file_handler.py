import csv
from patient import Patient
from gp import GP
from clinic import Clinic

class FileIO:

    PATIENT_CSV_PATH = './patient.csv'
    GPS_CSV_PATH = './gps.csv'
    CLINICS_CSV_PATH = './clinics.csv'
    
    @staticmethod
    def write_clinics_csv(clinics):
        if not clinics:
            raise ValueError("No clinics to write")
            
        clinics_list = list(clinics.values())

        fieldnames = list(clinics_list[0].to_dict().keys())

        with open(FileIO.CLINICS_CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for clinic in clinics_list:
                writer.writerow(clinic.to_dict())

    @staticmethod
    def write_patients_csv(patients):
        if not patients:
            raise ValueError("No patients to write")
        
        patients_list = list(patients.values())

        fieldnames = list(patients_list[0].to_dict().keys())

        with open(FileIO.PATIENT_CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for patient in patients_list:
                writer.writerow(patient.to_dict())
    
    @staticmethod
    def write_gps_csv(gps):
        if not gps:
            raise ValueError("No gp to write")
        
        gps_list = list(gps.values())

        fieldnames = list(gps_list[0].to_dict().keys())

        with open(FileIO.GPS_CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for gp in gps_list:
                writer.writerow(gp.to_dict())
    
    @staticmethod
    def read_patients_csv():
        patients = {}
        try:
            with open(FileIO.PATIENT_CSV_PATH, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    p = Patient(
                        email        = row['email'],
                        password     = row['password'],
                        first_name   = row['first_name'],
                        last_name    = row['last_name'],
                        date_of_birth= row['date_of_birth'],
                        gender       = row['gender'],
                        phone_number = row['phone_number'],
                        address      = row['address']
                    )
                    patients[p.email] = p
        except FileNotFoundError:
            return {}
        return patients
    
    @staticmethod
    def read_gps_csv():
        gps = {}
        try:
            with open(FileIO.GPS_CSV_PATH, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    gp = GP(
                        gp_id          = row['gp_id'],
                        first_name     = row['first_name'],
                        last_name      = row['last_name'],
                        email          = row['email'],
                        clinics        = row['clinics'],
                        specialisation = row['specialisation'],
                        days_off       = row['days_off'],
                    )
                    gps[gp.gp_id] = gp
        except FileNotFoundError:
            return {}
        return gps
    
    @staticmethod
    def read_clinics_csv():
        clinics = {}
        try:
            with open(FileIO.CLINICS_CSV_PATH, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    clinic = Clinic(
                        clinic_id             = row['clinic_id'],
                        clinic_name           = row['clinic_name'],
                        clinic_suburb         = row['clinic_suburb'],
                        clinic_services       = row['clinic_services'],
                        clinic_openning_hours = row['clinic_openning_hours']
                    )
                    clinics[clinic.clinic_id] = clinic
        except FileNotFoundError:
            return {}
        return clinics