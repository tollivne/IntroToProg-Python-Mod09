# ---------------------------------------------------------- #
# Title: IOClasses
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# N. Tolliver, 6.14.2020, Added Error Handling
# N. Tolliver, 6.14.2020, Added Press Enter to Continue Function
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else:
    import DataClasses as DC

class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_employee_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) Show current employee data
        2) Add new employee data.
        3) Save employee data to File
        4) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current items employees are: *******")
        for row in list_of_rows:
            print(str(row.employee_id)
                  + ","
                  + row.first_name
                  + ","
                  + row.last_name)
        print("*******************************************")
        print()  # Add an extra line for looks
    @staticmethod
    def input_employee_data():
        """ Gets data for an employee object
        :return: (employee) object with input data
        """
        # Note: This reads data into a list object
        try:
            employee_id = (input("What is the employee Id? - ").strip())
            if employee_id.isalpha():
                raise Exception("IDs must be numbers")
            first_name = str(input("What is the employee First Name? - ").strip())
            if first_name.isnumeric():
                raise Exception("First name must be alpha characters")
            last_name = str(input("What is the employee Last Name? - ").strip())
            if last_name.isnumeric():
                raise Exception("Last name must be alpha characters")
            print()  # Add an extra line for looks
            # Converts data from a list object to an employee object
            emp = DC.Employee(employee_id,first_name,last_name)
        except Exception as e:
            print(e)
        return emp

    @staticmethod
    def input_press_to_continue(optional_message):
        """ Pause the program and display a message before continuing
        param: optional_message:  An optional message to display to the user
        return: nothing
        """
        print(optional_message)
        input("Press the [Enter] key to return to menu.")

