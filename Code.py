import os
import sys

STUDENT_FILE = "students.txt"
COURSE_FILE = "courses.txt"

# Sample users
USERS = {"admin": "admin123", "Dhruva": "Std1", "Amarnath": "Std2", "Balaji":"Std3", "Chandini":"Std4"}

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pause function (like getch)
def pause():
    input("Press Enter to continue...")

# Display ASCII welcome header
def display_header():
    clear_screen()
    print(r"""
 -------------------------------------------------------------------------
|                                                                         |
|                                                                         |
|       W      W  WW W W  W       WW W W  WW W WW  WW    WW  WW W W       |
|       W      W  W       W       W       W     W  W W  W W  W            |
|       W  WW  W  WW W W  W       W       W     W  W  WW  W  WW W W       |
|       W W  W W  W       W       W       W     W  W      W  W            |
|       WW    WW  WW W W  WW W W  WW W W  WW W WW  W      W  WW W W       |
|                                                                         |
|                                                                         |
 -------------------------------------------------------------------------

                    *************************************************
                    *                                               *
                    *       -----------------------------           *
                    *          STUDENT DATA MANAGEMENT              *
                    *       -----------------------------           *
                    *                                               *
                    *                                               *
                    *                                               *
                    *             Brought To You By                 *
                    *             1. Konapala Dhruva                *
                    *             2. Pittu Amarnath                 *
                    *             3. Ravulapalli Balaji             *
                    *             4. Chandini Shaik                 *
                    *************************************************
""")
    pause()

# Login
def login():
    clear_screen()
    print("LOGIN\n")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if USERS.get(username) == password:
        print("\nLOGIN SUCCESSFUL!")
        pause()
        return True
    else:
        print("\nIncorrect username or password.")
        pause()
        return False

# Load all students from file
def load_students():
    students = []
    if not os.path.exists(STUDENT_FILE):
        return students
    with open(STUDENT_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 6:
                student = {
                    "ID": parts[0],
                    "roll": int(parts[1]),
                    "name": parts[2],
                    "email": parts[3],
                    "phone": parts[4],
                    "num_courses": int(parts[5])
                }
                students.append(student)
    return students

# Save all students to file
def save_students(students):
    with open(STUDENT_FILE, "w") as f:
        for s in students:
            f.write(f"{s['ID']},{s['roll']},{s['name']},{s['email']},{s['phone']},{s['num_courses']}\n")

# Load courses
def load_courses():
    courses = []
    if not os.path.exists(COURSE_FILE):
        return courses
    with open(COURSE_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                course = {"student_id": parts[0], "code": parts[1], "name": parts[2]}
                courses.append(course)
    return courses

# Save courses
def save_courses(courses):
    with open(COURSE_FILE, "w") as f:
        for c in courses:
            f.write(f"{c['student_id']},{c['code']},{c['name']}\n")

# Menu
def menu():
    print("\nMain Menu:")
    print("[1] Add Student")
    print("[2] Show All Students")
    print("[3] Search Student")
    print("[4] Edit Student")
    print("[5] Delete Student")
    print("[6] Delete All Students")
    print("[0] Exit")
    choice = input("Choice: ")
    return choice

# Add new student
def add_student():
    clear_screen()
    students = load_students()
    courses = load_courses()

    student = {}
    student["ID"] = input("Enter ID: ")
    student["roll"] = int(input("Enter Roll No: "))
    student["name"] = input("Enter Name: ")
    student["email"] = input("Enter Email: ")
    student["phone"] = input("Enter Phone: ")
    student["num_courses"] = int(input("Enter number of courses: "))

    students.append(student)
    save_students(students)

    for i in range(student["num_courses"]):
        course = {}
        course["student_id"] = student["ID"]
        course["code"] = input(f"Course {i+1} Code: ")
        course["name"] = input(f"Course {i+1} Name: ")
        courses.append(course)
    save_courses(courses)
    print("\nStudent added successfully!")
    pause()

# Show all students
def show_all_students():
    clear_screen()
    students = load_students()
    courses = load_courses()
    if not students:
        print("No students found.")
    for s in students:
        print(f"\nID: {s['ID']}\nRoll: {s['roll']}\nName: {s['name']}\nEmail: {s['email']}\nPhone: {s['phone']}\nCourses: {s['num_courses']}")
        for i, c in enumerate([c for c in courses if c["student_id"] == s["ID"]], start=1):
            print(f"  Course {i}: {c['code']} - {c['name']}")
    pause()

# Search student
def search_student():
    clear_screen()
    sid = input("Enter Student ID to search: ")
    students = load_students()
    courses = load_courses()
    found = False
    for s in students:
        if s["ID"] == sid:
            found = True
            print(f"\nID: {s['ID']}\nRoll: {s['roll']}\nName: {s['name']}\nEmail: {s['email']}\nPhone: {s['phone']}\nCourses: {s['num_courses']}")
            for i, c in enumerate([c for c in courses if c["student_id"] == s["ID"]], start=1):
                print(f"  Course {i}: {c['code']} - {c['name']}")
            break
    if not found:
        print("Student not found.")
    pause()

# Edit student
def edit_student():
    clear_screen()
    students = load_students()
    courses = load_courses()
    sid = input("Enter Student ID to edit: ")
    student = next((s for s in students if s["ID"] == sid), None)
    if not student:
        print("Student not found.")
        pause()
        return
    student["name"] = input(f"Enter new Name [{student['name']}]: ") or student["name"]
    student["email"] = input(f"Enter new Email [{student['email']}]: ") or student["email"]
    student["phone"] = input(f"Enter new Phone [{student['phone']}]: ") or student["phone"]
    student["num_courses"] = int(input(f"Enter new Number of courses [{student['num_courses']}]: ") or student["num_courses"])

    # Remove old courses
    courses = [c for c in courses if c["student_id"] != sid]
    # Add new courses
    for i in range(student["num_courses"]):
        course = {}
        course["student_id"] = student["ID"]
        course["code"] = input(f"Course {i+1} Code: ")
        course["name"] = input(f"Course {i+1} Name: ")
        courses.append(course)

    save_students(students)
    save_courses(courses)
    print("Student updated successfully!")
    pause()

# Delete student
def delete_student():
    clear_screen()
    sid = input("Enter Student ID to delete: ")
    students = load_students()
    courses = load_courses()
    students = [s for s in students if s["ID"] != sid]
    courses = [c for c in courses if c["student_id"] != sid]
    save_students(students)
    save_courses(courses)
    print("Student deleted successfully.")
    pause()

# Delete all students
def delete_all_students():
    clear_screen()
    open(STUDENT_FILE, "w").close()
    open(COURSE_FILE, "w").close()
    print("All students deleted.")
    pause()

# Main loop
def main():
    display_header()
    if not login():
        sys.exit()
    while True:
        clear_screen()
        choice = menu()
        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            delete_all_students()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
            pause()

if __name__ == "__main__":
    main()
