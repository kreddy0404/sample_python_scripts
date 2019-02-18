class Employee:

    def __init__(self, myFN, myLN, myUID):
        self.first_name = myFN
        self.last_name = myLN
        self.user_id = myUID

    def show_employee_details(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("User ID:", self.user_id)

def main():

    # Create new object.
    employee = Employee("Kesava", "Reddy", "kesa2403")
    employee_02 = Employee("Chinnapa", "Reddy", "kesa0824")

    # Display employee details
    employee.show_employee_details()
    employee_02.show_employee_details()

main()
