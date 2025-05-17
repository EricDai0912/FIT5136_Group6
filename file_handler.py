import csv, json, datetime
from patient import Patient
from gp import GP
from clinic import Clinic
from appointment import Appointment

class FileIO:

    PATIENT_CSV_PATH = './patient.csv'
    GPS_CSV_PATH = './gps.csv'
    CLINICS_CSV_PATH = './clinics.csv'
    APPOINTMENTS_CSV_PATH = './appointments.csv'
    REPORT_CSV_SUFFIX = '_report.csv'
    
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
                row = gp.to_dict()
                row['clinic_ids'] = json.dumps(gp.clinic_ids, ensure_ascii=False)
                row['clinic_names'] = json.dumps(gp.clinic_names, ensure_ascii=False)
                writer.writerow(row)
    
    @staticmethod
    def write_appointments_csv(appointments):
        if not appointments:
            raise ValueError("No appointments to write")
        
        appointments_list = list(appointments.values())

        fieldnames = list(appointments_list[0].to_dict().keys())

        with open(FileIO.APPOINTMENTS_CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for appointment in appointments_list:
                row = appointment.to_dict()
                if isinstance(row.get('date'), datetime.date):
                    row['date'] = row['date'].strftime("%d/%m/%Y")
                if isinstance(row.get('time'), datetime.time):
                    row['time'] = row['time'].strftime("%H:%M")
                writer.writerow(row)
    
    @staticmethod
    def write_report_csv(report, file_path_prefix):
        if not report:
            raise ValueError("Report is empty, nothing to write.")
        
        file_path = file_path_prefix + FileIO.REPORT_CSV_SUFFIX
        first = next(iter(report.values()))
        headers = list(first.to_print_dict().keys())

        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for item in report.values():
                writer.writerow(item.to_print_dict())
        return file_path
    
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
                        address      = row['address'],
                        notification = row['notification'],
                        last_booking_date = row['last_booking_date']
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
                        clinic_ids     = json.loads(row.get('clinic_ids', '[]')),
                        clinic_names   = json.loads(row.get('clinic_names', '[]')),
                        specialisation = row['specialisation'],
                        days_off       = row['days_off'],
                    )
                    gps[gp.gp_id] = gp
        except FileNotFoundError:
            return {}
        return gps
    
    @staticmethod
    def read_appointments_csv():
        appointments = {}
        try:
            with open(FileIO.APPOINTMENTS_CSV_PATH, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    appointment = Appointment(
                        appointment_id = row.get('appointment_id'),
                        patient_email     = row.get('patient_email'),
                        patient_name   = row.get('patient_name'),
                        gp_id          = row.get('gp_id'),
                        clinic_id      = row.get('clinic_id'),
                        clinic_name    = row.get('clinic_name'),
                        gp_name        = row.get('gp_name'),
                        clinic_suburb  = row.get('clinic_suburb'),
                        date           = datetime.datetime.strptime(row['date'], "%d/%m/%Y").date(),
                        time           = datetime.datetime.strptime(row['time'], "%H:%M").time(),
                        duration       = int(row.get('duration')),
                        availability   = True if row.get('availability') == 'True' else False,
                        reason         = row.get('reason')
                    )
                    appointments[appointment.appointment_id] = appointment
        except FileNotFoundError:
            return {}
        return appointments
    
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