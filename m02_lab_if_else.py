'''
Jeremy Baltazar 
m02_lab_if_else.py

This program will be able to determine if a student
made it on the Dean's List, Honor Roll, or neither 
by checking their GPA. 
'''
import sys

# Asking for students last name
stuLastName: str = input('What is your last name? ')
# Will exit program is user types 'ZZZ'.
if stuLastName == 'ZZZ': 
    sys.exit(0) # Exit program 

# Asking for students first name
stuFirstName: str = input('What is your first name? ')
# Asking for students GPA
studentGPA: float = float(input('Enter your GPA: '))
# If student has GPA 3.5 
if studentGPA >= 3.5:
    print(f"{stuFirstName} {stuLastName} has made the Dean's List.")
elif studentGPA >= 3.25:
    print(f"{stuFirstName} {stuLastName} has made the Honor Roll.")
else:
    print(f"{stuFirstName} {stuLastName} did not make it on any of the lists.")