class Employee:
    "Base class for employees."

    # __init__ method will intialize object attributes.
    def __init__(self):
        self.first_name = 'N/A'
        self.last_name = 'N/A'
        self.user_id = 'N/A'
        self.position_type = 'N/A'

    ######## Setters #############
    def set_first_name(self, myFN):
        self.first_name = myFN

    def set_last_name(self, myLN):
        self.last_name = myLN

    def set_user_id(self, myUserid):
        self.user_id = myUserid

    def set_position_type(self, myPT):
        self.position_type = myPT

    ######## Getters ################
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_id(self):
        return self.user_id

    def get_position_type(self):
        return self.position_type

# Main method.
def main():
    # Create a new employee object.
    employee_01 = Employee()

    # Default values.
    print("First Name:", employee_01.get_first_name())
    print("Last Name:", employee_01.get_last_name())
    print("Position Type:", employee_01.get_position_type())
    print("User ID:", employee_01.get_user_id())

    # Modify default values.
    employee_01.set_first_name("Kesava")
    employee_01.set_last_name("Reddy")
    employee_01.set_user_id("kesa3807")
    employee_01.set_position_type("Lead")

    # Display new values.
    print("*** New changes ***\n")
    print("First Name:", employee_01.get_first_name())
    print("Last Name:", employee_01.get_last_name())
    print("Position Type:", employee_01.get_position_type())
    print("User ID:", employee_01.get_user_id())

main()



