# Problem 1
students = {} # creating a dictionary 

def add_student():
    roll_no = int(input("Enter your roll number: "))
    name = input("Enter your name: ")
    n = int(input("Enter number of subjects: "))

    marks = [] # creating a list to store marks for diffferent subjects
    for i in range(n):
      m = int(input("Enter your marks: "))
      marks.append(m)

    students[roll_no] = (name,marks) #  entering the inputted data in the dictionary, with the name and marks in a tupple
    print()
    print("Student data added succcesfully.\n")


def display_students_above_90():
    print("Students with average marks above 90 are:\n")
    for roll_no in students: # accesing the key and value by looping the dictionary
        name = students[roll_no][0]
        marks = students[roll_no][1]
        average = sum(marks)/len(marks)
        if average > 90:
            print("Roll number:",roll_no, "Name", name, "Average", average)
        print()


def update_student_marks():
    roll_no = int(input("Enter Roll number to update"))
    if roll_no not in students: # checking if inputted roll number exists in dictionary or not 
        print("Student with given roll number does not exist")
    else:
        name = students[roll_no][0]
        old_marks = students[roll_no][1]
        print("Name: ", name, "Current Marks: ", old_marks)

        n = int(input("Enter number of subjects: "))
        new_marks = []
        for i in range(n):
            m = int(input("Enter new marks"))
            new_marks.append(m)

    students[roll_no] = (name, new_marks)

    print("Marks have been updated.\n")


def display_all():
    print("\nAll Sudent Records")
    for roll_no in students:
        name = students[roll_no][0]
        marks = students[roll_no][1]
        print("Roll no: ", roll_no,  "\nName: ", name, "\nMarks: ", marks)

    print()

#------- Main program to manage student data -------#

while True:
    print("\nStudent Data Management System")
    print("1. Add Student")
    print("2. Students with average marks above 90")
    print("3. Update Student Marks")
    print("4. Show all students")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students_above_90()
    elif choice == '3':
        update_student_marks()
    elif choice == '4':
        display_all()
    elif choice == '5':
        print("Exiting the program.")
        break
