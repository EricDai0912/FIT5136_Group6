import os, datetime
from controllor import MPMS
from validation import Validation

class Display:
    PAGE_WIDTH = 50

    def __init__(self):
        self.mpms = MPMS()
        self.current_user = None
        self.status_message = "" 

    def display_header(self, title):
        print("=" * Display.PAGE_WIDTH)
        print(title.center(Display.PAGE_WIDTH))
        print("=" * Display.PAGE_WIDTH)
    
    def clear_and_header(self, title):
        os.system("clear")
        self.display_header(title)
        if self.status_message:
            print(self.status_message)
            self.status_message = ""

    def print_table(self, data):
        if not data:
            print("No Record Found.")
            return
        
        data_list = list(data.values())
        rows = [obj.to_print_dict() for obj in data_list]
        headers = ["Option"] + list(rows[0].keys())

        widths = {key: len(key) for key in headers}
        widths["Option"] = max(widths["Option"], len(str(len(rows))))

        for row in rows:
            for key, value in row.items():
                widths[key] = max(widths[key], len(str(value)))

        outline = "+-" + "-+-".join("-" * widths[key] for key in headers) + "-+"
        inline = "| " + " | ".join(f"{{:<{widths[key]}}}" for key in headers) + " |"

        print(outline)
        print(inline.format(*headers))
        print(outline)
        for idx, row in enumerate(rows, start=1):
            values = [str(idx)] + [str(row[h]) for h in headers[1:]]
            print(inline.format(*values))
        print(outline)
    
    def admin_update_delete_clinic(self, idx):
        clinic = list(self.mpms.clinics.values())[idx - 1]
        while True:
            self.clear_and_header("Clinic Details")
            print(f"\n1: Clinic Name: {clinic.clinic_name}")
            print(f"\n2: Clinic Suburb: {clinic.clinic_suburb}")
            print(f"\n3: Clinic Available Services: {clinic.clinic_services}")
            print(f"\n4: Clinic Opearating Hours: {clinic.clinic_openning_hours}")
            print("\n5: Delete")
            print("\n0: Save&Exit")
            choice = input("\nPlease enter an option to update or delete: ").strip()
            if choice == '1':
                while True:
                    self.clear_and_header("Update Clinic Name")
                    print("\nClinic Name:")
                    clinic_name = input("> ").strip()
                    if not Validation.is_empty(clinic_name):
                        clinic.clinic_name = clinic_name
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '2':
                while True:
                    self.clear_and_header("Update Clinic Suburb")
                    print("\nClinic Suburb:")
                    clinic_suburb = input("> ").strip()
                    if not Validation.is_empty(clinic_suburb):
                        clinic.clinic_suburb = clinic_suburb
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '3':
                while True:
                    self.clear_and_header("Update Clinic Available Services")
                    print("\nClinic Available Services:")
                    clinic_services = input("> ").strip()
                    if not Validation.is_empty(clinic_services):
                        clinic.clinic_services = clinic_services
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '4':
               while True:
                    self.clear_and_header("Update Clinic Opearating Hours")
                    print("\nClinic Opearating Hours:")
                    clinic_openning_hours = input("> ").strip()
                    if not Validation.is_empty(clinic_openning_hours):
                        clinic.clinic_openning_hours = clinic_openning_hours
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '5':
                choice = input("\nAre you sure you want to delete[Y/Any key]:")
                if choice == 'Y':
                    self.mpms.delete_clinic(clinic.clinic_id)
                    return
            elif choice == '0':
                self.mpms.update_clinic(clinic)
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"

    
    def admin_list_clinic(self):
        while True:
            self.clear_and_header("Update or Delete Clinic Info")
            print("\nList of all clinics:\n")
            self.print_table(self.mpms.clinics)
            print("\n0: Exit")
            choice = input("\nPlease enter an option to update or delete: ").strip()
            if choice == '0':
                return
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.mpms.clinics):
                    self.admin_update_delete_clinic(choice)
                    break
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
                continue
            

    def admin_list_gp(self):
        while True:
            self.clear_and_header("Update or Delete GP Info")
            print("\nList of all GP:\n")
            self.print_table(self.mpms.gps)
            print("\n0:Exit")
            choice = input("\nPlease enter an option to update or delete: ").strip()
            if choice == '0':
                return
            
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.mpms.gps):
                    self.admin_update_delete_gp(choice)
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
                continue

    def admin_update_delete_appointment(self, idx, appointments):
        appointment = list(appointments.values())[idx-1]
        while True:
            self.clear_and_header("Appointment Details")
            print(f"\n1: Appointment Date: {appointment.date}")
            print(f"\n2: Appointment Time: {appointment.time}")
            print(f"\n3: Appointment Duration: {appointment.duration}")
            print(f"\n4: Appointment Reason: {appointment.reason}")
            print("\n5: Release")
            print("\n6: Delete")
            print("\n0: Save&Exit")
            choice = input("\nPlease enter an option to update or delete: ").strip()
            if choice == '1':
                while True:
                    self.clear_and_header("Update Appointment Date")
                    print("\nAppointment Date:")
                    date = input("> ").strip()
                    if Validation.is_valid_date(date):
                        appointment.date = date
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '2':
                while True:
                    self.clear_and_header("Update Appointment Time")
                    print("\nAppointment Time:")
                    time = input("> ").strip()
                    if Validation.is_valid_time(time):
                        appointment.time = time
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '3':
                while True:
                    self.clear_and_header("Update Appointment Duration")
                    print("\nAppointment Duration:")
                    duration = input("> ").strip()
                    if duration in ['15', '25', '40', '60']:
                        appointment.duration = int(duration)
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '4':
                while True:
                    self.clear_and_header("Update Appointment Reason")
                    print("\nAppointment Reason:")
                    reason = input("> ").strip()
                    if not Validation.is_empty(reason):
                        appointment.reason = reason
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '5':
                choice = input("\nAre you sure you want to release[Y/Any key]:")
                if choice == 'Y':
                    self.mpms.release_appointment(appointment.appointment_id)
            elif choice == '6':
                choice = input("\nAre you sure you want to delete[Y/Any key]:")
                if choice == 'Y':
                    self.mpms.delete_appointment(appointment.appointment_id)
                    return
            elif choice == '0':
                self.mpms.update_appointment(appointment)
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"

    def admin_update_delete_gp(self, idx):
        gp = list(self.mpms.gps.values())[idx-1]
        while True:
            self.clear_and_header("GP Details")
            print(f"\n1: GP First Name: {gp.first_name}")
            print(f"\n2: GP Last Name: {gp.last_name}")
            print(f"\n3: GP Email: {gp.email}")
            print(f"\n4: GP Clinics: {gp.clinic_names}")
            print(f"\n5: GP Specialisation: {gp.specialisation}")
            print(f"\n6: GP Days_off: {gp.days_off}")
            print("\n7: Delete")
            print("\n0: Save&Exit")

            choice = input("\nPlease enter an option to update or delete: ").strip()
            if choice == '1':
                while True:
                    self.clear_and_header("Update GP First Name")
                    print("\nGP First Name:")
                    first_name = input("> ").strip()
                    if not Validation.is_empty(first_name):
                        gp.first_name = first_name
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '2':
                while True:
                    self.clear_and_header("Update GP Last Name")
                    print("\nGP Last Name:")
                    last_name = input("> ").strip()
                    if not Validation.is_empty(last_name):
                        gp.last_name = last_name
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '3':
                while True:
                    self.clear_and_header("Update GP Email")
                    print("\nGP Email:")
                    email = input("> ").strip()
                    if not Validation.is_empty(email) and Validation.is_gp_valid_email(email):
                        gp.email = email
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"   
            elif choice == '4':
                assigned_clinics = []
                while True:
                    self.clear_and_header("Reassign GP Clinics")
                    print("\nList of all clinics:\n")
                    self.print_table(self.mpms.clinics)
                    print("\n0: Done")
                    print(f"\nAssigned Clinic: {[c.clinic_name for c in assigned_clinics]}")
                    print("   *Please select one clinic at a time")
                    choice = input("> ").strip()
                    if choice == '0':
                        gp.clinic_ids = [c.clinic_id for c in assigned_clinics]
                        gp.clinic_names = [c.clinic_name for c in assigned_clinics]
                        break
                    try:
                        idx = int(choice)
                        if 1 <= idx <= len(self.mpms.clinics):
                            clinic = list(self.mpms.clinics.values())[idx - 1]
                            if not clinic in assigned_clinics:
                                assigned_clinics.append(clinic)
                            else:
                                self.status_message = f"\n\nError: This clinic has already assigned!\n"
                            continue
                        else:
                            raise ValueError
                    except ValueError:
                        self.status_message = f"\n\nError: Invalid Input!\n"
                        continue         
            elif choice == '5':
                while True:
                    self.clear_and_header("Update GP Specialisation")
                    print("\nGP Specialisation:")
                    specialisation = input("> ").strip()
                    if not Validation.is_empty(specialisation):
                        gp.specialisation = specialisation
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"   
            elif choice == '6':
                while True:
                    self.clear_and_header("Update GP Last Name")
                    print("\nGP Days_off:")
                    days_off = input("> ").strip()
                    if not Validation.is_empty(days_off):
                        gp.days_off = days_off
                        break
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
            elif choice == '7':
                choice = input("\nAre you sure you want to delete[Y/Any key]:")
                if choice == 'Y':
                    self.mpms.delete_gp(gp.gp_id)
                    return
            elif choice == '0':
                self.mpms.update_gp(gp)
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"

    def admin_create_appointment(self, gid, cid):    
        while True:
            self.clear_and_header("Create a New Appointment")
            print("\nDate :")
            print("   *Format dd/mm/yyyy ")
            date = input("> ").strip()
            if Validation.is_valid_date(date):
                date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
                self.clear_and_header("Create a New Appointment")
                print("\nTime :")
                print("   *Format HH:MM (24h) ")
                time = input("> ").strip()
                if Validation.is_valid_time(time):
                    time = datetime.datetime.strptime(time, "%H:%M").time()
                    self.clear_and_header("Create a New Appointment")
                    print("\nDuration :")
                    print("   * 15/25/40/60 mins")
                    print("   * Only enter the number")
                    duration = input("> ").strip()
                    if duration in ['15', '25', '40', '60']:
                        duration = int(duration)
                        start_dt = datetime.datetime.combine(date, time)
                        end_dt = start_dt + datetime.timedelta(minutes=duration)
                        if not self.mpms.check_appointment_conflict(
                            gid, start_dt, end_dt
                            ):
                            break
                        else:
                            self.status_message = f"\n\nError: Appointment Conflict!\n"
                    else:
                        self.status_message = f"\n\nError: Invalid Input!\n"
                else:
                    self.status_message = f"\n\nError: Invalid Input!\n"
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        try:
            self.mpms.create_appointment(
                gid, cid, date, time, duration
            )
        except ValueError as e:
            self.status_message = f"\nCreate Appointment failed: {e}\n"
            return
        return

    def admin_create_clinic(self):
        while True:
            self.clear_and_header("Create a New Appointment")
            print("\nClinic Name:")
            clinic_name = input("> ").strip()
            if not Validation.is_empty(clinic_name):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Create a New Appointment")
            print("\nClinic Suburb:")
            clinic_suburb = input("> ").strip()
            if not Validation.is_empty(clinic_suburb):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        while True:
            self.clear_and_header("Create a New Appointment")
            print("\nClinic Services:")
            clinic_services = input("> ").strip()
            if not Validation.is_empty(clinic_services):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        while True:
            self.clear_and_header("Create a New Appointment")
            print("\nClinic Openning Hours:")
            clinic_openning_hours = input("> ").strip()
            if not Validation.is_empty(clinic_openning_hours):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        try:
            self.mpms.create_clinic(
                clinic_name, clinic_suburb, clinic_services,
                clinic_openning_hours
            )
        except ValueError as e:
            self.status_message = f"\nCreate GP failed: {e}\n"
            return
        return

    def admin_create_gp(self):
        while True:
            self.clear_and_header("Create a New GP")
            print("\nFirst Name:")
            first_name = input("> ").strip()
            if not Validation.is_empty(first_name):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Create a New GP")
            print("\nLast Name:")
            last_name = input("> ").strip()
            if not Validation.is_empty(last_name):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        while True:
            self.clear_and_header("Create a New GP")
            print("\nEmail:")
            email = input("> ").strip()
            if not Validation.is_empty(email) and Validation.is_gp_valid_email(email):
                break
            else:
                self.status_message = "\n\nError: Invalid Input!\n"

        assigned_clinics = []   
        while True:
            self.clear_and_header("Create a New GP")
            print("\nList of all clinics:\n")
            self.print_table(self.mpms.clinics)
            print("\n0: Done")
            print(f"\nAssigned Clinic: {[c.clinic_name for c in assigned_clinics]}")
            print("   *Please select one clinic at a time")
            choice = input("> ").strip()
            if choice == '0':
                clinic_ids = [c.clinic_id for c in assigned_clinics]
                clinic_names = [c.clinic_name for c in assigned_clinics]
                break
            try:
                idx = int(choice)
                if 1 <= idx <= len(self.mpms.clinics):
                    clinic = list(self.mpms.clinics.values())[idx - 1]
                    if not clinic in assigned_clinics:
                        assigned_clinics.append(clinic)
                    else:
                        self.status_message = f"\n\nError: This clinic has already assigned!\n"
                    continue
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
                continue
        
        while True:
            self.clear_and_header("Create a New GP")
            print("\nSpeciallisation:")
            specialisation = input("> ").strip()
            if not Validation.is_empty(specialisation):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        while True:
            self.clear_and_header("Create a New GP")
            print("\nAvailability:")
            days_off = input("> ").strip()
            if not Validation.is_empty(days_off):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        try:
            self.mpms.create_gp(
                first_name, last_name, email, clinic_ids, clinic_names, specialisation,
                days_off
            )
        except ValueError as e:
            self.status_message = f"\nCreate GP failed: {e}\n"
            return
        return
        
    def patient_register(self):
        while True:
            self.clear_and_header("Patient Register")
            print("\nEmail Monash student email or staff email:")
            print("   *Email Monash student email or staff email")
            email = input("> ").strip()
            if Validation.is_valid_email(email):
                if not self.mpms.is_patient_exist(email):
                    break
                else:
                    self.status_message = f"\n\nError: Email already registered!\n"
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nPassword:")
            print("   *Minimum eight characters")
            print("   *At least one uppercase")
            print("   *At least one number")
            password = input("> ").strip()
            error = Validation.is_valid_password(password)
            if error == "":
                break
            else:
                self.status_message = f"\n\n{error}!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nFirst Name:")
            first_name = input("> ").strip()
            if not Validation.is_empty(first_name):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nLast Name:")
            last_name = input("> ").strip()
            if not Validation.is_empty(last_name):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        while True:
            self.clear_and_header("Patient Register")
            print("\nDate of Birth :")
            print("   *Format dd/mm/yyyy ")
            date_of_birth = input("> ").strip()
            if Validation.is_valid_dob(date_of_birth):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nGender: (Male/Female/Other/Prefer not to say)")
            print("   *Male: M")
            print("   *Female: F")
            print("   *Other: O")
            print("   *Prefer not to say: N")
            gender = input("> ").strip()
            if Validation.is_valid_gender(gender):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nMobile Number (+61):")
            phone_number = input("> ").strip()
            if Validation.is_valid_phone(phone_number):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        self.clear_and_header("Patient Register")
        print("\nAddress (Optional):")
        address = input("> ").strip()

        try:
            self.mpms.register_patient(
                email, password, first_name, last_name,
                date_of_birth, gender, phone_number, address
            )
        except ValueError as e:
            self.status_message = f"\nRegistration failed: {e}\n"
            return

        self.patient_register_success(first_name)

    def patient_register_success(self, name):
        self.clear_and_header("Registration Successful")
        print("\n\n" + f"Hello {name}, you have registered successfully!".center(Display.PAGE_WIDTH))
        input("\n\n\nPress Enter to return to main menu.\n")
        return

    def patient_booking_success(self, name, appointment_id):
        self.clear_and_header("Registration Successful")
        print("\n\n" + f"Hello {name}, you have booked successfully!".center(Display.PAGE_WIDTH))
        print("\n\nHere is your appointment details:")
        self.print_table({appointment_id: self.mpms.appointments[appointment_id]})
        input("\n\n\nPress Enter to return.\n")
        return

    def patient_login(self):
        while True:
            self.clear_and_header("Patient Login")
            print("\nEnter 'exit' to go back at any time")
            print("\nPlease enter your Email:")
            email = input("> ").strip()
            if email.lower() == 'exit':
                return
            print("\nPlease enter your Password:")
            password = input("> ").strip()
            if password.lower() == 'exit':
                return
            try:
                patient = self.mpms.login_patient(email, password)
            except ValueError as e:
                self.status_message = f"\n\nError: {e} Please try again\n"
                continue
            break

        self.current_user = patient
        self.patient_menu()
        return

    def admin_login(self):
        while True:
            self.clear_and_header("Admin Login")
            print("\nEnter 'exit' to go back at any time")
            print("\nPlease enter your Email:")
            email = input("> ").strip()
            if email.lower() == 'exit':
                return
            print("\nPlease enter your Password:")
            password = input("> ").strip()
            if password.lower() == 'exit':
                return
            try:
                admin = self.mpms.login_admin(email, password)
            except ValueError as e:
                self.status_message = f"\n\nError: {e} Please try again\n"
                continue
            break

        self.current_user = admin
        self.admin_menu()
        return

    def admin_gp_management(self):
        while True:
            self.clear_and_header("GP Management")
            print("1: Create a new GP")
            print("2: Update or Delete GPs")
            print("0: Exit")
            choice = input("\nPlease enter an option: ").strip()

            if choice == '1':
                self.admin_create_gp()
            elif choice == '2':
                self.admin_list_gp()
            elif choice == '0':
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"
    
    def admin_clinic_management(self):
        while True:
            self.clear_and_header("Clinic Management")
            print("1: Create a new Clinic")
            print("2: Update or Delete Clinics")
            print("0: Exit")
            choice = input("\nPlease enter an option: ").strip()

            if choice == '1':
                self.admin_create_clinic()
            elif choice == '2':
                self.admin_list_clinic()
            elif choice == '0':
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"
    
    def admin_appointment_list_per_gp(self, gid, cid):
        appointments = self.mpms.get_appointments_by_gp_id_clinic_id(gid, cid)
        while True:
            self.clear_and_header(f"DR.{self.mpms.gps[gid].first_name}")
            print("\nList of all Appointments:\n")
            self.print_table(appointments)
            print("\nn: set a new appointment")
            print("0: Exit")
            choice = input("\nPlease enter an option or choose one to update: ").strip()
            if choice == '0':
                return
            elif choice == 'n':
                self.admin_create_appointment(gid, cid)
                continue
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.mpms.appointments):
                    self.admin_update_delete_appointment(choice, appointments)
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
                continue
    
    def admin_appointment_management(self):
        while True:
            self.clear_and_header("Appointment Management")
            print("\n0: Exit")
            print("\nPlease enter the Clinic Suburb:")
            clinic_suburb = input("> ").strip()
            if clinic_suburb == '0':
                return
            clinics = self.mpms.get_clinics_by_clinic_suburb(clinic_suburb)
            while True:
                self.clear_and_header(f"{clinic_suburb}")
                print("\nList of all clinics:\n")
                self.print_table(clinics)
                print("\n0: Exit")
                choice = input("\nPlease enter an option: ").strip()
                if choice == '0':
                    break
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(clinics):
                        cid = list(clinics.values())[choice - 1].clinic_id
                        gps = self.mpms.get_gps_by_clinic_id(cid)
                        while True:
                            self.clear_and_header(f"{self.mpms.clinics[cid].clinic_name}")
                            print("\nList of all gps:\n")
                            self.print_table(gps)
                            print("\n0: Exit")
                            choice = input("\nPlease enter an option: ").strip()
                            if choice == '0':
                                break
                            try:
                                choice = int(choice)
                                if 1 <= choice <= len(gps):
                                    gid = list(gps.values())[choice - 1].gp_id
                                    self.admin_appointment_list_per_gp(gid, cid)
                                else:
                                    raise ValueError
                            except ValueError:
                                self.status_message = f"\n\nError: Invalid Input!\n"
                                continue
                    else:
                        raise ValueError
                except ValueError:
                    self.status_message = f"\n\nError: Invalid Input!\n"
                    continue
    
    def patient_previous_appointments(self):
        appointments = self.mpms.get_previous_appointments(self.current_user.email)
        while True:
            self.clear_and_header("Previous Appointments")
            print("\nList of all previous appointments:\n")
            self.print_table(appointments)
            print("\n0: Exit")
            choice = input("\nPlease enter an option: ").strip()
            if choice == '0':
                return
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
    
    def patient_upcoming_appointments(self):
        appointments = self.mpms.get_upcoming_appointments(self.current_user.email)
        while True:
            self.clear_and_header("Upcoming Appointments")
            print("\nList of all upcoming appointments:\n")
            self.print_table(appointments)
            print("\n0: Exit")
            choice = input("\nPlease enter an option to cancel: ").strip()
            if choice == '0':
                return
            try:
                idx = int(choice)
                if 1 <= idx <= len(appointments):
                    choice = input("\nAre you sure you want to Cancel[Y/Any key]:")
                    if choice == 'Y':
                        appointment = list(appointments.values())[idx - 1]
                        self.mpms.cancel_appointment(appointment.appointment_id, self.current_user.email)
                        appointments = self.mpms.get_upcoming_appointments(self.current_user.email)
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
    
    def patient_list_appointments(self):
        available_appointments = self.mpms.get_available_appointments()
        while True:
            self.clear_and_header("Available Appointments")
            print("\nList of all available appointments:\n")
            self.print_table(available_appointments)
            print("\nFilter by:")
            print(" *f1: Date")
            print(" *f2: GP")
            print(" *f3: Clinic Suburb")
            print(" *f4: clear all filters")
            print("\n0: Exit")
            print("\nNOTE: Each Patient can only book one appointment per day")
            choice = input("\nPlease enter an option to book: ").strip()
            if choice == '0':
                return
            elif choice == 'f1':
                available_appointments = self.patient_filter_date()
                continue
            elif choice == 'f2':
                available_appointments = self.patient_filter_gp()
                continue
            elif choice == 'f3':
                available_appointments = self.patient_filter_clinic_suburb()
                continue
            elif choice == 'f4':
                available_appointments = self.mpms.get_available_appointments()
                continue
            try:
                choice = int(choice)
                if 1 <= choice <= len(available_appointments):
                    available_appointments = self.patient_book_appointments(choice, available_appointments)
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
    
    def patient_book_appointments(self, idx, available_appointments):
        if self.mpms.check_patient_booking_access(self.current_user.email):
            while True:
                self.clear_and_header("Book an Appointment")
                print("\nPlease enter your reason for visit:")
                print("   * General Consultation/Specialist Referral/Vaccination/Other")
                reason = input("> ").strip()
                if reason in ['General Consultation', 'Specialist Referral', 'Vaccination', 'Other']:
                    break
                else:
                    self.status_message = f"\n\nError: Invalid Input!\n"
            appointment = list(available_appointments.values())[idx - 1]
            self.mpms.book_appointment(appointment.appointment_id, self.current_user.email, reason)
            available_appointments = self.mpms.get_available_appointments()
            self.patient_booking_success(self.current_user.first_name, appointment.appointment_id)
        else:
            self.status_message = f"\n\nError: You have already booked an appointment today!\n"
        return available_appointments
    
    def patient_filter_date(self):
        while True:
            self.clear_and_header("Filter Appointments by Date")
            print("\nenter 'exit' to exit")
            print("\nDate:")
            print("   *Format dd/mm/yyyy ")
            date = input("> ").strip()
            if Validation.is_valid_date(date):
                available_appointments = self.mpms.get_available_appointments_by_date(
                    datetime.datetime.strptime(date, "%d/%m/%Y").date())
                break
            elif date == 'exit':
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        return available_appointments
        
    def patient_filter_clinic_suburb(self):
        while True:
            self.clear_and_header("Filter Appointments by Clinic Suburb")
            print("\nenter 'exit' to exit")
            print("\nClinic Suburb:")
            clinic_suburb = input("> ").strip()
            if not Validation.is_empty(clinic_suburb):
                available_appointments = self.mpms.get_available_appointments_by_clinic_suburb(clinic_suburb)
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        return available_appointments
    
    def patient_filter_gp(self):
        while True:
            self.clear_and_header("Filter Appointments by GP")
            print("\nList of all gps:\n")
            self.print_table(self.mpms.gps)
            print("\n0: Exit")
            choice = input("\nPlease enter an choose an gp: ").strip()
            if choice == '0':
                break
            try:
                idx = int(choice)
                if 1 <= idx <= len(self.mpms.gps):
                    available_appointments = self.mpms.get_available_appointments_by_gp_id(idx)
                    break
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
        return available_appointments
    
    def admin_report_custom_range(self):
        while True:
            self.clear_and_header("Custom Range")
            print("\nStart Date:")
            print("   *Format dd/mm/yyyy ")
            start_date = input("> ").strip()
            if Validation.is_valid_date(start_date):
                start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Custom Range")
            print("\nEnd Date:")
            print("   *Format dd/mm/yyyy ")
            end_date = input("> ").strip()
            if Validation.is_valid_date(end_date):
                end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y").date()
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        return start_date, end_date
    
    def admin_show_report(self, report, title, start_date, end_date):
        while True:
            self.clear_and_header(title)
            print(f"\nDate Range: {start_date} to {end_date}")
            self.print_table(report)
            print("\n\n\n1: Export to csv\n")
            print("0: Exit\n")
            choice = input("\nPlease enter an option: ").strip()
            if choice == '1':
                try:
                    file_path = self.mpms.export_report_to_csv(report, title, start_date, end_date)
                    self.status_message = f"\nExported successfully to \'./{file_path}\'\n"
                except ValueError as e:
                    self.status_message = f"\nExport failed: {e}\n"
            elif choice == '0':
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"


    def admin_gp_report(self):
        while True:
            self.clear_and_header("Report on Patient Volume per GP")
            print("\nDate Range of the Report:\n")
            print("1: Today")
            print("2: Last 7 Days")
            print("3: Last 30 Days")
            print("4: Custom Range")
            print("0: Exit")
            choice = input("\nPlease enter an option to generate the report: ").strip()
            if choice == '0':
                return
            elif choice == '1':
                start_date = datetime.datetime.now().date()
                end_date = start_date
            elif choice == '2':
                start_date = datetime.datetime.now().date() - datetime.timedelta(days=7)
                end_date = datetime.datetime.now().date()
            elif choice == '3':
                start_date = datetime.datetime.now().date() - datetime.timedelta(days=30)
                end_date = datetime.datetime.now().date()
            elif choice == '4':
                start_date, end_date = self.admin_report_custom_range()
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"
                continue
            try:
                report = self.mpms.generate_gp_report(start_date, end_date)
            except ValueError as e:
                self.status_message = f"\n\nError: {e} Please try again\n"
            self.admin_show_report(report, "Report on Patient Volume per GP", start_date, end_date)

    def admin_clinic_report(self):
        while True:
            self.clear_and_header("Report on Patient Volume per Clinic")
            print("\nList of all clinics:\n")
            self.print_table(self.mpms.clinics)
            print("\n0: Exit")
            choice = input("\nPlease enter an option: ").strip()
            if choice == '0':
                return
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.mpms.clinics):
                    cid = list(self.mpms.clinics.values())[choice - 1].clinic_id
                    clinic_name = self.mpms.clinics[cid].clinic_name
                    while True:
                        self.clear_and_header(f"Report on Patient Volume {clinic_name}")
                        print("\nDate Range of the Report:\n")
                        print("1: Today")
                        print("2: Last 7 Days")
                        print("3: Last 30 Days")
                        print("4: Custom Range")
                        print("0: Exit")
                        choice = input("\nPlease enter an option to generate the report: ").strip()
                        if choice == '0':
                            break
                        elif choice == '1':
                            start_date = datetime.datetime.now().date()
                            end_date = start_date
                        elif choice == '2':
                            start_date = datetime.datetime.now().date() - datetime.timedelta(days=7)
                            end_date = datetime.datetime.now().date()
                        elif choice == '3':
                            start_date = datetime.datetime.now().date() - datetime.timedelta(days=30)
                            end_date = datetime.datetime.now().date()
                        elif choice == '4':
                            start_date, end_date = self.admin_report_custom_range()
                        else:
                            self.status_message = "\nError: Invalid option, please try again.\n"
                            continue
                        try:
                            report = self.mpms.generate_clinic_report(cid, start_date, end_date)
                        except ValueError as e:
                            self.status_message = f"\n\nError: {e} Please try again\n"
                        self.admin_show_report(report, f"Report on Patient Volume of {clinic_name}", start_date, end_date)
                else:
                    raise ValueError
            except ValueError:
                self.status_message = f"\n\nError: Invalid Input!\n"
                continue
            

    def patient_menu(self):
        while True:
            self.clear_and_header("Patient Menu")
            print("1: Book an Appointment")
            print("2: Upcoming Appointments")
            print("3: Previous Appointments")
            print("0: Logout")
            choice = input("\nPlease enter an option: ").strip()

            if choice == '1':
                self.patient_list_appointments()
            elif choice == '2':
                self.patient_upcoming_appointments()
            elif choice == '3':
                self.patient_previous_appointments()
            elif choice == '0':
                print("\nLogging out...")
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"


    def admin_menu(self):
        while True:
            self.clear_and_header("Admin Menu")
            print("1: Report on Patient Volume per GP")
            print("1: Report on Patient Volume per Clinic")
            print("3: Appointment Management")
            print("4: GP Management")
            print("5: Clinic Management")
            print("0: Logout")
            choice = input("\nPlease enter an option: ").strip()

            if choice == '1':
                self.admin_gp_report()
            elif choice == '2':
                self.admin_clinic_report()
            elif choice == '3':
                self.admin_appointment_management()
            elif choice == '4':
                self.admin_gp_management()
            elif choice == '5':
                self.admin_clinic_management()
            elif choice == '0':
                print("\nLogging out...")
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"
    
    def index_menu(self):
        while True:
            self.clear_and_header("Monash Patient Management System (MPMS)")
            print("\n" + "Welcome to the MPMS!".center(Display.PAGE_WIDTH) + "\n")
            print("1: Register")
            print("2: Patient Login")
            print("3: Admin Login")
            print("0: Exit")
            choice = input("\nPlease enter an option: ").strip()

            if choice == '1':
                self.patient_register()
            elif choice == '2':
                self.patient_login()
            elif choice == '3':
                self.admin_login()
            elif choice == '0':
                print("\nExiting MPMS...")
                self.mpms.save_data('A')
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"

if __name__ == "__main__":
    display = Display()
    display.index_menu()