# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# N. Tolliver, 6.11.2020 Created Script from Listing 13
# N. Tolliver, 6.11.2020 Added code for printing menu, getting user choice, and choices 1 and 4
# N. Tolliver, 6.11.2020 Added code for menu choice 3 and while loop
# N. Tolliver, 6.14.2020 Added error handling for FileNotFound Error

# ------------------------------------------------------------------------ #
# TODO: Import Modules
file_name = "EmployeeData.txt"
import sys

if __name__ == "__main__":
    try:
        import DataClasses as D  # data classes
    # Include Error Handling in case the Module Name is not found
    except ModuleNotFoundError as e:
            print("Please make sure the Module by the name of DataClasses exists!")
            print("If using the CMD window, change directory to the folder you're working in "
                  "by typing the following command cd c:\_Name of Path")
            sys.exit()
    try:
        from DataClasses import Employee as Emp  # Employee class only!
    # Include Error Handling in case the Module Name is not found
    except ModuleNotFoundError as e:
        print("Please make sure the Module by the name of DataClasses exists!")
        print("If using the CMD window, change directory to the folder you're working in "
              "by typing the following command cd c:\_Name of Path")
        sys.exit()
    # Include Error Handling in case the Class Name is not found
    except ImportError as e:
        print("Please make sure the function by the name of Employee exists in the DataClasses Module!")
        sys.exit()
    try:
        import ProcessingClasses as P  # processing classes
    # Include Error Handling in case the Module Name is not found
    except ModuleNotFoundError as e:
            print("Please make sure the Module by the name of ProcessingClasses exists!")
            print("If using the CMD window, change directory to the folder you're working in "
                  "by typing the following command cd c:\_Name of Path")
            sys.exit()
    try:
        from IOClasses import EmployeeIO as Eio
    # Include Error Handling in case the Module Name is not found
    except ModuleNotFoundError as e:
            print("Please make sure the Module by the name of IOClasses exists!")
            print("If using the CMD window, change directory to the folder you're working in "
                  "by typing the following command cd c:\_Name of Path")
    # Include Error Handling in case the Class Name is not found
    except ImportError as e:
        print("Please make sure the function by the name of Employee exists in the IOClasses Module!")
        sys.exit()

else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
lstTable = []
lstFileData = P.FileProcessor.read_data_from_file(file_name)
lstTable.clear() # Clear list before loading from file
for line in lstFileData: # Convert list of strings to Employee objects
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
# for row in lstTable:  # show Employee data from refilled list
#      print(row.to_string(), type(row))

# Show user a menu of options
try:
    while(True):
        Eio.print_menu_items()

        # Get user's menu option choice

        strChoice = Eio.input_menu_options()

        if strChoice.strip() == "1":

            # Show user current data in the list of employee objects
            # for row in lstTable:
                Eio.print_current_list_items(lstTable)

        elif strChoice.strip() == "2":
            # Let user add data to the list of employee objects
            new_employee = Eio.input_employee_data()
            print(new_employee.to_string().strip()) # Debuggins statement
            lstTable, strStatus = P.DatabaseProcessor.add_data_to_list(new_employee, lstTable)
            Eio.input_press_to_continue(strStatus)

        elif strChoice.strip() == "3":
            # let user save current data to file
            P.FileProcessor.save_data_to_file(file_name, lstTable)

        elif strChoice.strip() == "4":
            # Let user exit program
            print("Goodbye")
            break

        else: print("Choice Must be 1, 2, 3, or 4")

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
  # Main Body of Script  ---------------------------------------------------- #