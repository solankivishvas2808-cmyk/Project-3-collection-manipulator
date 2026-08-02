# ==========================================================
#               STUDENT DATA ORGANIZER
#              Collection Manipulator Project
# ==========================================================

students = []                  # List
student_database = {}          # Dictionary
subjects_offered = set()       # Set


# ==========================================================
# Welcome Function
# ==========================================================

def welcome():

    print("\n" + "=" * 70)
    print("             WELCOME TO STUDENT DATA ORGANIZER")
    print("=" * 70)
    print("This program helps you manage student records.")
    print("It uses List, Tuple, Set and Dictionary concepts.")
    print("=" * 70)


# ==========================================================
# Menu Function
# ==========================================================

def menu():

    print("\n")
    print("=" * 70)
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    print("=" * 70)


# ==========================================================
# Input Validation Functions
# ==========================================================

def get_student_id():

    while True:

        try:

            student_id = int(input("Enter Student ID : "))

            if student_id <= 0:
                print("Student ID must be positive.")
            elif student_id in student_database:
                print("Student ID already exists.")
            else:
                return student_id

        except ValueError:

            print("Please enter numbers only.")


def get_age():

    while True:

        try:

            age = int(input("Enter Age : "))

            if age < 1 or age > 100:
                print("Enter a valid age.")
            else:
                return age

        except ValueError:

            print("Age must be numeric.")


def get_subjects():

    subject_input = input(
        "Enter Subjects (comma separated) : "
    )

    subject_list = []

    for subject in subject_input.split(","):

        subject = subject.strip().title()

        if subject != "":

            if subject not in subject_list:
                subject_list.append(subject)

            subjects_offered.add(subject)

    return subject_list


# ==========================================================
# Add Student
# ==========================================================

def add_student():

    print("\n" + "-" * 50)
    print("ADD NEW STUDENT")
    print("-" * 50)

    student_id = get_student_id()

    name = input("Enter Student Name : ").title().strip()

    age = get_age()

    grade = input("Enter Grade : ").upper().strip()

    dob = input("Enter Date of Birth (YYYY-MM-DD) : ").strip()

    subjects = get_subjects()

    # Immutable Tuple

    student_tuple = (student_id, dob)

    # Dictionary

    student = {

        "student_tuple": student_tuple,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects

    }

    # Mutable List

    students.append(student)

    # Dictionary with Student ID

    student_database[student_id] = {

        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects

    }

    print("\nStudent Added Successfully.")

    # String Formatting

    print(f"Welcome {name}!")

    print("Grade : {}".format(grade))

    print("Age : %d Years" % age)

    # ==========================================================
# Search Student Function
# ==========================================================

def search_student(student_id):

    for student in students:

        if student["student_tuple"][0] == student_id:
            return student

    return None


# ==========================================================
# Display All Students
# ==========================================================

def display_students():

    if len(students) == 0:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 100)
    print("{:<10} {:<20} {:<8} {:<10} {}".format(
        "ID", "NAME", "AGE", "GRADE", "SUBJECTS"))
    print("=" * 100)

    for student in students:

        student_id = student["student_tuple"][0]

        subjects = ", ".join(student["subjects"])

        print("{:<10} {:<20} {:<8} {:<10} {}".format(
            student_id,
            student["name"],
            student["age"],
            student["grade"],
            subjects
        ))

    print("=" * 100)

    print(f"\nTotal Students : {len(students)}")


# ==========================================================
# Display Complete Information of One Student
# ==========================================================

def display_single_student():

    if len(students) == 0:
        print("\nNo student records available.")
        return

    student_id = int(input("Enter Student ID : "))

    student = search_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\n" + "=" * 50)
    print("STUDENT DETAILS")
    print("=" * 50)

    print(f"Student ID     : {student['student_tuple'][0]}")
    print(f"Name           : {student['name']}")
    print(f"Age            : {student['age']}")
    print(f"Grade          : {student['grade']}")
    print(f"Date of Birth  : {student['student_tuple'][1]}")
    print("Subjects       : " + ", ".join(student["subjects"]))

    print("=" * 50)


# ==========================================================
# Student Statistics
# ==========================================================

def student_statistics():

    print("\n" + "=" * 40)
    print("STUDENT STATISTICS")
    print("=" * 40)

    print(f"Total Students : {len(students)}")
    print(f"Unique Subjects: {len(subjects_offered)}")

    if len(subjects_offered) > 0:
        print("Subjects Offered:")

        count = 1

        for subject in sorted(subjects_offered):
            print(f"{count}. {subject}")
            count += 1

    print("=" * 40)

# ==========================================================
# Update Student Information
# Demonstrates Mutability of List and Dictionary
# ==========================================================

def update_student():

    if len(students) == 0:
        print("\nNo student records available.")
        return

    student_id = int(input("Enter Student ID to Update : "))

    student = search_student(student_id)

    if student is None:
        print("Student not found.")
        return

    while True:

        print("\n")
        print("=" * 50)
        print("UPDATE MENU")
        print("=" * 50)
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Grade")
        print("4. Update Subjects")
        print("5. Back")
        print("=" * 50)

        choice = input("Enter Your Choice : ")

        # -------------------------------
        # Update Name
        # -------------------------------
        if choice == "1":

            new_name = input("Enter New Name : ").title().strip()

            student["name"] = new_name
            student_database[student_id]["name"] = new_name

            print("Name Updated Successfully.")

        # -------------------------------
        # Update Age
        # -------------------------------
        elif choice == "2":

            new_age = get_age()

            student["age"] = new_age
            student_database[student_id]["age"] = new_age

            print("Age Updated Successfully.")

        # -------------------------------
        # Update Grade
        # -------------------------------
        elif choice == "3":

            new_grade = input("Enter New Grade : ").upper().strip()

            student["grade"] = new_grade
            student_database[student_id]["grade"] = new_grade

            print("Grade Updated Successfully.")

        # -------------------------------
        # Update Subjects
        # -------------------------------
        elif choice == "4":

            new_subjects = get_subjects()

            student["subjects"] = new_subjects
            student_database[student_id]["subjects"] = new_subjects

            print("Subjects Updated Successfully.")

        # -------------------------------
        # Back
        # -------------------------------
        elif choice == "5":

            break

        else:

            print("Invalid Choice! Please Try Again.")


# ==========================================================
# Demonstration of Tuple Immutability
# ==========================================================

def tuple_information():

    print("\n" + "=" * 60)
    print("TUPLE (IMMUTABILITY) DEMONSTRATION")
    print("=" * 60)

    if len(students) == 0:
        print("No student records available.")
        return

    student_id = int(input("Enter Student ID : "))

    student = search_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Tuple : ", student["student_tuple"])

    print("\nStudent ID and Date of Birth are stored")
    print("inside a Tuple.")

    print("Tuple is immutable, therefore these")
    print("values should not be modified once created.")

    print("=" * 60)

# ==========================================================
# Rebuild Subject Set
# (Keeps the Set updated after deletion or subject changes)
# ==========================================================

def rebuild_subjects():

    subjects_offered.clear()

    for student in students:

        for subject in student["subjects"]:

            subjects_offered.add(subject)


# ==========================================================
# Delete Student (Using del Keyword)
# ==========================================================

def delete_student():

    if len(students) == 0:

        print("\nNo student records available.")
        return

    student_id = int(input("Enter Student ID to Delete : "))

    for index in range(len(students)):

        if students[index]["student_tuple"][0] == student_id:

            # -------- del Keyword --------
            del students[index]

            # Delete from Dictionary
            del student_database[student_id]

            # Update Subject Set
            rebuild_subjects()

            print("\nStudent Record Deleted Successfully.")
            return

    print("\nStudent ID Not Found.")


# ==========================================================
# Display All Unique Subjects (Using Set)
# ==========================================================

def display_subjects():

    if len(subjects_offered) == 0:

        print("\nNo subjects available.")
        return

    print("\n" + "=" * 50)
    print("        UNIQUE SUBJECTS OFFERED")
    print("=" * 50)

    for number, subject in enumerate(sorted(subjects_offered), start=1):

        print(f"{number}. {subject}")

    print("=" * 50)


# ==========================================================
# Display Student Database (Dictionary)
# ==========================================================

def display_database():

    if len(student_database) == 0:

        print("\nDatabase is Empty.")
        return

    print("\n" + "=" * 70)
    print("        STUDENT DATABASE (DICTIONARY)")
    print("=" * 70)

    for student_id, details in student_database.items():

        print(f"\nStudent ID : {student_id}")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Grade      : {details['grade']}")
        print("Subjects   : " + ", ".join(details["subjects"]))

    print("=" * 70)

# ==========================================================
# Exit Function
# ==========================================================

def exit_program():

    print("\n" + "=" * 70)
    print("      Thank You For Using Student Data Organizer")
    print("         Keep Learning Python. Have a Nice Day!")
    print("=" * 70)


# ==========================================================
# Main Program
# ==========================================================

welcome()

while True:

    menu()

    choice = input("Enter Your Choice : ").strip()

    if choice == "1":

        add_student()

    elif choice == "2":

        display_students()

    elif choice == "3":

        update_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        display_subjects()

    elif choice == "6":

        exit_program()
        break

    else:

        print("\nInvalid Choice! Please Enter a Valid Option.")
"""
======================================================================
             WELCOME TO STUDENT DATA ORGANIZER
======================================================================
This program helps you manage student records.
It uses List, Tuple, Set and Dictionary concepts.
======================================================================


======================================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
======================================================================
Enter Your Choice : 1

--------------------------------------------------
ADD NEW STUDENT
--------------------------------------------------
Enter Student ID : 101
Enter Student Name : vishu
Enter Age : 18
Enter Grade : A=
Enter Date of Birth (YYYY-MM-DD) : 2008-07-28
Enter Subjects (comma separated) : python,englidh,computer

Student Added Successfully.
Welcome Vishu!
Grade : A=
Age : 18 Years


======================================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
======================================================================
Enter Your Choice : 1

--------------------------------------------------
ADD NEW STUDENT
--------------------------------------------------
Enter Student ID : 102
Enter Student Name : yash
Enter Age : 16
Enter Grade : b
Enter Date of Birth (YYYY-MM-DD) : 2011=09=11
Enter Subjects (comma separated) : python,history,bio

Student Added Successfully.
Welcome Yash!
Grade : B
Age : 16 Years


======================================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
======================================================================
Enter Your Choice : 2

====================================================================================================
ID         NAME                 AGE      GRADE      SUBJECTS
====================================================================================================
101        Vishu                18       A+         Python, Englidh, Computer
102        Yash                 16       B          Python, History, Bio
====================================================================================================

Total Students : 2


======================================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
======================================================================
Enter Your Choice : 3
Enter Student ID to Update : 101


==================================================
UPDATE MENU
==================================================
1. Update Name
2. Update Age
3. Update Grade
4. Update Subjects
5. Back
==================================================
Enter Your Choice : 2
Enter Age : 19
Age Updated Successfully.


==================================================
UPDATE MENU
==================================================
1. Update Name
2. Update Age
3. Update Grade
4. Update Subjects
5. Back
==================================================
Enter Your Choice : 4
Enter Subjects (comma separated) : python,bio
Subjects Updated Successfully.


==================================================
UPDATE MENU
==================================================
1. Update Name
2. Update Age
3. Update Grade
4. Update Subjects
5. Back
==================================================
Enter Your Choice : 3
Enter New Grade : a
Grade Updated Successfully.


==================================================
UPDATE MENU
==================================================
1. Update Name
2. Update Age
3. Update Grade
4. Update Subjects
5. Back
==================================================
Enter Your Choice : 5


======================================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
======================================================================
Enter Your Choice : 5

==================================================
        UNIQUE SUBJECTS OFFERED
==================================================
1. Bio
2. Computer
3. Englidh
4. History
5. Python
==================================================


======================================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
======================================================================
Enter Your Choice : 4
Enter Student ID to Delete : 102

Student Record Deleted Successfully.


======================================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
======================================================================
Enter Your Choice : 6

======================================================================
      Thank You For Using Student Data Organizer
         Keep Learning Python. Have a Nice Day!
======================================================================
"""
