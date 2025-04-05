import os
class MPMS:

    PAGE_WIDTH = 50

    def __init__(self):
        pass

    def displayHeader(self, displayString):
        print("=" * MPMS.PAGE_WIDTH)
        print(displayString.center(MPMS.PAGE_WIDTH))
        print("=" * MPMS.PAGE_WIDTH)

    def indexMenu(self):
        while True:
            self.displayMainMenu()
            choice = input("\nPlease enter an option: ").strip()

            if choice == '1':
                self.register()
            elif choice == '2':
                self.patient_login()
            elif choice == '3':
                self.admin_login()
            elif choice == '0':
                print("\nExiting MPMS...")
                break
            else:
                print("\nError: Invalid option, please try again.\n")

    def displayMainMenu(self):
        os.system("clear")
        self.displayHeader("Monash Patient management System (MPMS)")
        print("\n\n" + "Welcome to the MPMS!".center(MPMS.PAGE_WIDTH) + "\n\n")
        print("1: Register")
        print("2: Patient Login")
        print("3: Admin Login")
        print("0: Exit")
        print("=" * MPMS.PAGE_WIDTH)

    def register(self):
        os.system("clear")
        self.displayHeader("Patient Register")
        
        print("\nEmail Monash student email or staff email:")
        print("   *Email Monash student email or staff email")
        email = input("> ")

        print("\nPassword:")
        print("   *Minimum eight characters")
        print("   *at least one uppercase")
        print("   *at least one number")
        password = input("> ")

        print("\nFirst Name:")
        first_name = input("> ")

        print("\nLast Name:")
        last_name = input("> ")

        print("\nDate of Birth :")
        print("   *Format dd/mm/yyyy ")
        dob = input("> ")

        print("\nGender: (Male/Female/Other/Prefer not to say)")
        gender = input("> ")

        print("\nMobile Number (+61):")
        mobile = input("> ")

        print("\nAddress (Optional):")
        address = input("> ")

        self.register_success(first_name)

        return
    
    def register_success(self, name):
        os.system("clear")
        self.displayHeader("Patient Register")
        print("\n\n\n" + f"Hello {name} , you have registered successfully!".center(MPMS.PAGE_WIDTH))
        print("\n" +"Thank you for using MPMS!".center(MPMS.PAGE_WIDTH))
        print("\n\n\n\n" + "Enter any key to Exit".center(MPMS.PAGE_WIDTH))
        print("=" * MPMS.PAGE_WIDTH)
        action = input()
        if action or not action:
            self.indexMenu()
        pass


    def patient_login(self):
        pass

    def admin_login(self):
        pass


if __name__ == "__main__":
    mpms = MPMS()
    mpms.indexMenu()