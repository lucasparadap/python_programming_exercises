#Unfinished Code

'''
The task in this project is to build a database to hold student information, classes, and grades.
---- This is a simplistic database and not designed to be feature-rich.
The basic functions of a database include the ability to:
 - Create the data entries (C)
X - Read the data (R)
 - Update the entries (U)
X - Delete the data entries (D)
                         ^^^^^----- (often referred to by the acronym CRUD)

While a full database will be able to do these on the data store directly -
- in this project the data will be read into a local variable and then written out to the file.
'''
def read_data():
    with open ("students.txt") as file:
        for line in file:
            print(line)

def update_name():
    school = []
    with open("students.txt") as file:
        for line in file.readlines():
            strip = line.rstrip("\n")
            school = strip.split("|")
            names = school[:-1]
        student = input("Which Student would you like to update? ----\n press 'exit' to quit. ")
        for student in names:
            if student in names:
                response = input("What would you like to change it to? ")
                student.replace(student,response)
                return names
            elif student not in names:
                print("Sorry, we have no record of that person... ")
            elif student.lower() == 'exit':
                break


#def add_student():
roster = []
pairing = {}
pairing2 = {}
pairing3 = {}
with open("students.txt") as file:
    for line in file.readlines():
        strip = line.rstrip("\n")
        split = strip.split(":")
        split2 = split[0].split("|")
        pairing[split[0]] = split[1]
        split3 = split[1].split(",")
        split4 = split[2].split(",")
        pairing2[split3[0]] = split3[1]
        pairing3[split4[0]] = split4[1]
        roster.append(pairing)
        roster.append(pairing2)
        roster.append(pairing3)
    print(roster)


# def build_student():
student_pair1 = {}
student_pair2 = {}
student_pair3 = {}
student_list = []
name = input("Please enter the students name ")
_class1 = input("Please enter the student's first class ")
_entry1 = name+'|'+_class1
_grade1 = input("Please enter the letter grade the student has received for the stated class.\nIf grade is not known or not application -- enter 'X'")
student_pair1[_entry1] = _grade1
_class2 = input("Please enter the student's second class ")
_grade2 = input("Please enter the letter grade the student has received for the stated class.\nIf grade is not known or not application -- enter 'X'")
student_pair2[_class2] = _grade2
_class3 = input("Please enter the student's second class ")
_grade3 = input("Please enter the letter grade the student has received for the stated class.\nIf grade is not known or not application -- enter 'X'")
student_pair3[_class3] = _grade3
student_list.append(student_pair1)
student_list.append(student_pair2)
student_list.append(student_pair3)
print(student_list)
#












def brkdwn_data():
    grades = {}
    with open("students.txt") as file:
        for line in file.readlines():
            strip = line.rstrip("\n")
            school = strip.split("|")
            report = {}
            grades[school[0]] = school[1].split(":")
            for grade_pair in school[1].split(","):
                grade_pair_split = grade_pair.split(":")
                report[grade_pair_split[0]] = grade_pair_split[1]
            return(report)
'''
def update_data():                                                              #THIS NEEDS HELP
    course = input("Please enter the course the student is enrolled in: ")
    grade = input("Please enter the letter grade the student has received in the respective course\n"
                      "If grade is not known or not application -- enter 'X'")
    update = {}
    for key in update.keys():
        update = f'{key}: {update[key]}'  # dictionary f string - to read
    print(update)
'''


def del_student():
    import os
    original_file = "students.txt"
    temp_file = "temp.txt"

    which_student = input("What student would you like to delete?")

    with open(original_file, "r") as input:
        with open("temp.txt", "w") as output:
            for line in input:
                if not line.strip("\n").startswith(which_student):
                    output.write(line)
        os.replace('temp.txt', 'students.txt')
        print("students.txt")


#def report_card():

'''
#Optional: def class_roster():
# Optional: def add_course()
'''