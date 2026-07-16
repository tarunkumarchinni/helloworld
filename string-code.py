students = [
    {"roll_number": 101, "name": "Jathin", "marks": 85},
    {"roll_number": 102, "name": "Aarav", "marks": 92},
    {"roll_number": 103, "name": "Priya", "marks": 78},
    {"roll_number": 104, "name": "Sneha", "marks": 88},
    {"roll_number": 105, "name": "Rahul", "marks": 95}
]

def searchWithRollno():
    enteredRollNo = int(input('Enter rollno for search'))
    found = False
    for student in students:
        if student["roll_number"] == enteredRollNo :
            found = True
            print(f"Searched Student:\n"
                f"RollNo-{student["roll_number"]}\n",
              f"name-{student["name"]}\n",
              f"marks={student["marks"]}\n")
            break
    if found == False :
        print("not found")
    selectMenuItem()


def addNewStudent():
    newStudent = {}
    newStudent['name'] = input('Enter Student Name')
    newStudent['roll_number'] = int(input('Enter Student Roll no'))
    newStudent['marks'] = int(input('Enter Student Marks'))

    students.append(newStudent)
    selectMenuItem()


def displayAllStudents():
    print("------------------------")
    for student in students:
        print(f"RollNo-{student["roll_number"]}",
              f"name-{student["name"]}",
              f"marks-{student["marks"]}")
        
    print("------------------------")
    selectMenuItem()

def identifyTopper():
    highestMarks = 0
    studentWithHighestMarks = {}
    print("------------------------")
    for student in students:
         if highestMarks < student["marks"]:
            highestMarks=student["marks"]
            studentWithHighestMarks =student
    print("Topper Student: \n",
          f"RollNo-{studentWithHighestMarks["roll_number"]}\n",
          f"name-{studentWithHighestMarks["name"]}\n",
          f"marks={studentWithHighestMarks["marks"]}\n")
    print("------------------------")
    selectMenuItem()
    
        
def selectMenuItem():
    print("Menu:\n"
      "1. Add new Student\n" 
      "2. Display all Students\n" 
      "3. Search For a student With Roll no\n" 
      "4. Identify Student with Highest marks\n"
      "5. Exit application")
    menuItem = int(input("Enter number from above Menu"))

    match menuItem:
        case 1:
            addNewStudent()
        case 2:
            displayAllStudents()
        case 3:
            searchWithRollno()
        case 4:
            identifyTopper()
        case _:
            print("Closed")


selectMenuItem()