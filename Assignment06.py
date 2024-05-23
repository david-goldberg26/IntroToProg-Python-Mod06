# ------------------------------------------------------------------------------------------ #
# Title: Assignment 06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   David Goldberg, 5/18/2024, attempt at Assigment 06
# ------------------------------------------------------------------------------------------ #
import json
from typing import TextIO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Variables 
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


class FileProcessor:
    '''
    Contains two functions that read in and write to a JSON File
    '''
    @staticmethod
    def read_data_from_file(file_name:str, student_data: list):   
        '''
        Function that reads in data from a JSON file and then into a dictionary
        :param file_name: A string indicating the file name
        :param student_data: dictionary from students inputs
        :return: list of student data

        '''
        file: TextIO = None 
        try:
            file = open(file_name, "r")     # open the file in read mode
            student_data = json.load(file)      # load the previous dictionaries from the json file
            print(student_data)
            print('''
                  This was the data read from the file
                  ''')
            file.close()
        except Exception as e:
            IO.output_error_message(message='text file not found\n', error = e)     # calling IO class for structured error
        finally:
            if file == False:
                file.close()
        return student_data
    
    @staticmethod
    def write_data_to_file(file_name:str, student_data:list):
        '''
        Function that reads the students dictionarties into the JSON File
        :param file_name: A string indicating the file name
        :param student_data: dictionary from students inputs

        '''
        try:
            file = open(file_name, "w")     # open a file to write to
            json.dump(student_data, file)       # write the dictionary/dictionaries to the json file
            file.close()
            print("The following data was saved to file!\n")
            IO.output_student_courses(student_data=student_data)        # calling IO class to output inputs 
        except Exception as e:      # Structured error handling if any exceptions occur
            if file.closed == False:
                file.close()
            IO.output_error_message(message='There was a problem with writing the file', error=e)       # calling IO class for structured error
        finally:
            if file.closed == False:
                file.close()


    
class IO:
    '''
    Contains functions that deal with inputs and outputs
    Printing the Menu
    Selecting a Menu Choice
    Error handling
    inputting student data
    outputting student data
    '''
    @staticmethod
    def output_error_message(message:str, error: Exception = None):
        '''
        Function displays prints error statements
        :param message: string of data containing a message
        :param error: message that pertains to the Exception

        :return: None

        '''

        print(message)
        if error is not None:       #Print error messages from the exceptions 
            print('--- technical info--\n')
            print(error, error.__doc__, type(error), sep = '\n') 

    
    @staticmethod
    def output_menu(menu:str):
        '''
        Function Displays menu choices to students
        :param menu: student menu choice
        :return: None
        '''
        print('\n')
        print(menu)     # will print the menu
        print('\n')

    @staticmethod
    def input_menu_choice():
        '''
        Function allows students to input student choice
        :return: students string choice
        '''
        string_choice = input("Enter a choice from the menu: ")     #allows student to input the menu choice
        while string_choice not in ['1', '2', '3', '4']:        # checks if input is 1-4
            IO.output_error_message("Please enter an option between 1 and 4")       # calling IO class for structured error
            string_choice = input('Enter a valid menu choice: ')        # will ask the user again
        return string_choice

    @staticmethod
    def input_student_data(student_data):
        '''
        Function allows for students to input their names and courses
         :param student_data: list of dictionaries that are filled by students inputs
        :return: dictionary (list)
          '''
        student_first_name: str = ''
        student_last_name: str = ''
        course_name: str = ''
        student: list = []
        try:
            student_first_name = input("Enter the student's first name: ")      # student will input first name
            if not student_first_name.isalpha():        # checks if input doesnt have a letter
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")        #student will input their last name
            if not student_last_name.isalpha():      # checks if input doesnt have a letter
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}      # builds dictionary of students inputs
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_message(message= "inputted name is not the correct data type", error=e)     # calling IO class for structured error
        except Exception as e:
            IO.output_error_message(message= "Error: Problem with entering your data", error=e)     # calling IO class for structured error
        return student_data
    
    @staticmethod
    def output_student_courses(student_data:list):
        '''
        Function is to output the students compelete dictionary
        :param student_data: list of students inputs
        '''
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')      # output students inputs when called
        print("-" * 50)


# Main Body

students = FileProcessor.read_data_from_file(FILE_NAME, students)       #calls the class and function necessary to read data 

while True:

    IO.output_menu(menu=MENU)       # calls IO class and a method to output the menu
    menu_choice = IO.input_menu_choice()        # calls IO class and a method to get students choice

    if menu_choice == "1":
        students = IO.input_student_data(students)      # if choice is 1 it will call the input method 
        continue

    elif menu_choice == "2":
        IO.output_student_courses(students)     # if choice is 2 it will call the output student method
        continue

    elif menu_choice == '3':
        FileProcessor.write_data_to_file(FILE_NAME, students)       #if choice is 3 it will call method to write to file
        continue

    elif menu_choice == '4':        # break out of the program and exit
        break

print('End of program')
        