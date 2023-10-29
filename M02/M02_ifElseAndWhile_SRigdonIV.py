#!/usr/bin/env python

"""M02_ifElseAndWhile.py a small python app that accepts student names and gpas and tests to see if studnet qualifies for dean's list or honor role"""

__author__ = "Sammy Rigdon IV"
__version__ = "1.0.0"
__email__ = "srigdon5@ivytech.edu"

# Create student class
class Student:
    def __init__(self, last_name=str, first_name=str, gpa=float) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.gpa = gpa

    def check_gpa(self):
        if self.gpa >= 3.5:
            print(f"{self.first_name} {self.last_name} has made the Dean's List with a GPA of {self.gpa}")
        elif self.gpa >= 3.25:
            print(f"{self.first_name} {self.last_name} has made the Honor Roll with a GPA of {self.gpa}")
        else:
            print(f"{self.first_name} {self.last_name} did not make the Honor Roll or Dean's List")

def create_student(last_name=str, first_name=str, gpa=float):
    return Student(last_name=last_name, first_name=first_name, gpa=gpa)


# Create function for user input
def main():
    while True:
        # Welcome user
        input('\nHello and Welcome to the GPA Checker. When prompted please input the information for the student you wish to check. The search is not case sensitive.\n'
              'please press enter to continue. If you wish to exit, enter Student Last Name as "ZZZ"')
        # Get last name
        user_ln_input = input('Student Last Name: ')
        
        # check for exit code
        if user_ln_input.upper() == 'ZZZ':
            print("Now Exiting")
            break
        
        # get first name
        user_fn_input = input('Student First Name: ')
        
        # get gpa
        user_gpa_input = input('GPA(please enter as a decimal number): ')
        
        # convert gpa to float
        try:
            user_gpa_input = float(user_gpa_input)
        except ValueError:
            print("Please only enter numbers when entering GPA")
            continue
        
        # create new student
        user_student = create_student(last_name=user_ln_input, first_name=user_fn_input, gpa=user_gpa_input)        
        print(f"Testing GPA of {user_student.first_name} {user_student.last_name}")
        
        # test gpa
        user_student.check_gpa()
        
# run main
if __name__ == '__main__':
    main()
