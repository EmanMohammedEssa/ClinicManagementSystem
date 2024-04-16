from ClinicManagementSystem import ClinicManagementSystem

clinic_system = ClinicManagementSystem()
while True:
        print("\nClinic Management System \n")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Mark Patient as Treated")
        print("4. Remove Patient")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            clinic_system.add_patient()
        elif choice == "2":
            clinic_system.view_patients()
        elif choice == "3":
            clinic_system.mark_patient_completed()
        elif choice == "4":
            clinic_system.remove_patient()
        elif choice == "5":
            print("Exiting Clinic Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        