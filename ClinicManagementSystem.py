from patient import patient
class ClinicManagementSystem:
    def __init__(self):
        self.listOfPatient = []
    def add_patient(self):

            name = input("Enter patient's name: ")
            validated_name = patient.get_validated_input(name, "name")
            age = input("Enter patient's age: ")
            validated_age = patient.get_validated_input(age, "age")
            gender = input("Enter patient's gender (Male, Female): ")
            validated_gender = patient.get_validated_input(gender, "gender")
            condition = input("Enter patient's medical condition: ")
            new_patient = patient(validated_name, validated_age, validated_gender, condition)
            self.listOfPatient.append(new_patient)
            print(f"Patient '{new_patient.name}' added successfully!")

    def remove_patient(self):
        if not self.listOfPatient:
            print("No patients found in the system.")
            return
        self.view_patients()  # Display patient list for reference
        patient_name = input("Enter the name of the patient to remove: ")
        found = False
        for i, patient in enumerate(self.listOfPatient):
            if patient.name == patient_name:
                del self.listOfPatient[i]  # Remove patient at index i
                print(f"Patient '{patient.name}' removed successfully!")
                found = True
                break
        if not found:
            print(f"Patient '{patient_name}' not found in the system.")

    def view_patients(self):
        if not self.listOfPatient:
            print("No patients found in the system.")
            return
        print("** Patient List **")
        for patient in self.listOfPatient:
            print(patient)
            print("-" * 30)

    def mark_patient_completed(self):
        if not self.listOfPatient:
            print("No patients found in the system.")
            return
        self.view_patients()  # Display patient list for reference
        patient_name = input("Enter the name of the patient to mark as treated: ")
        found = False
        for patient in self.listOfPatient:
            if patient.name == patient_name:
                patient.update_status("Treated")
                print(f"Patient '{patient.name}' marked as treated successfully!")
                found = True
                break


