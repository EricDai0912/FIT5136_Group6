import os
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
                self.register()
            elif choice == '2':
                self.patient_login()
            elif choice == '3':
                self.admin_login()
            elif choice == '0':
                print("\nExiting MPMS...")
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"

    def patient_menu(self):
        while True:
            self.clear_and_header("Patient Menu")
            print("0: Logout")
            choice = input("\nPlease enter an option: ").strip()

            if choice == '1':
                self.view_patient_details()
            elif choice == '0':
                print("\nLogging out...")
                return
            else:
                self.status_message = "\nError: Invalid option, please try again.\n"

    def register(self):
        validation = Validation()
        while True:
            self.clear_and_header("Patient Register")
            print("\nEmail Monash student email or staff email:")
            print("   *Email Monash student email or staff email")
            email = input("> ").strip()
            if validation.is_valid_email(email):
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
            error = validation.is_valid_password(password)
            if error == "":
                break
            else:
                self.status_message = f"\n\n{error}!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nFirst Name:")
            first_name = input("> ").strip()
            if not validation.is_empty(first_name):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nLast Name:")
            last_name = input("> ").strip()
            if not validation.is_empty(last_name):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"
        
        while True:
            self.clear_and_header("Patient Register")
            print("\nDate of Birth :")
            print("   *Format dd/mm/yyyy ")
            date_of_birth = input("> ").strip()
            if validation.is_valid_dob(date_of_birth):
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
            if validation.is_valid_gender(gender):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

        while True:
            self.clear_and_header("Patient Register")
            print("\nMobile Number (+61):")
            phone_number = input("> ").strip()
            if validation.is_valid_phone(phone_number):
                break
            else:
                self.status_message = f"\n\nError: Invalid Input!\n"

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

        self.register_success(first_name)

    def register_success(self, name):
        self.clear_and_header("Registration Successful")
        print("\n\n" + f"Hello {name}, you have registered successfully!".center(Display.PAGE_WIDTH))
        input("\n\n\nPress Enter to return to main menu.")
        return

    def patient_login(self):
        while True:
            self.clear_and_header("Patient Login")
            print("\nEnter 'exit' to go back at any time")
            print("\nPlease enter your Email:")
            email = input("> ").strip()
            if email.lower() == 'exit':
                return
            if not self.mpms.is_patient_exist(email):
                self.status_message = f"\n\nError: Email does not exist!\n"
                continue
            break

        while True:
            self.clear_and_header("Patient Login")
            print("\nEnter 'exit' to go back at any time")
            print("\nPlease enter your Password:")
            password = input("> ").strip()
            if password.lower() == 'exit':
                return
            try:
                patient = self.mpms.login_patient(email, password)
            except ValueError as e:
                self.status_message = f"\n\nError: {e}\n"
                continue
            break

        self.current_user = patient
        self.patient_menu()
        return

    def admin_login(self):
        self.clear_and_header("Admin Login")
        pass

if __name__ == "__main__":
    display = Display()
    display.index_menu()
