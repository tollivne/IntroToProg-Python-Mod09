# ---------------------------------------------------------- #
# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# N. Tolliver, 6.11.2020 Created script from Listing 07
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
import sys
class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = "Data was saved to file"
            print(success_status)
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except FileNotFoundError as e:
            print("Please make sure the file by the name of : " + file_name + " exists!")
            print("If using the CMD window, change directory to the folder you're working in "
                  "by typing the following command cd c:\_Name of Path")
            sys.exit()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

class DatabaseProcessor:
    # TODO: Add code to process to and from a database
    def add_data_to_list(employee_object, list_of_employee_objects):
        """ This function adds an Employee to the Table
        param: employee_object - Employee ID, First name, Last name
        return: list_of_employee_objects, status
        """
        # row = [product, price]
        list_of_employee_objects.append(employee_object)  # Add the new row to the list/table
        return list_of_employee_objects, "Employee has been added!"