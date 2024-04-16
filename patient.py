class patient:
    def __init__(self, name, age, gender, condition, status="In Treatment"):
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nCondition: {self.condition}\nStatus:{self.status}\n"

    @classmethod
    def get_validated_input(self, value, type_name):
        if type_name == "name":
            if not value.isalpha():
                return "Error: Invalid name. Please enter only letters.\n"
        elif type_name == "age":
            try:
                age = int(value)
                if age <= 0:
                    return "Error: Age must be a positive integer.\n"
            except ValueError:
                return "Error: Invalid age. Please enter an integer.\n"

        elif type_name == "gender":
            if value.lower() not in ("male", "female"):
                return "Error: Invalid gender. Please enter 'Male', 'Female'\n"
        # if valid input
        return value

