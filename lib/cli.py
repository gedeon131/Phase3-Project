# Menu principal de l'application CLI

from lib.helpers import clear_screen
from lib.models.course import list_courses, create_course, delete_course
from lib.models.student import list_students, create_student, delete_student
from lib.models.enrollment import enroll_student

def main_menu():
    while True:
        clear_screen()
        print("\n=== Course Management CLI ===")
        print("1. View all courses")
        print("2. Add a course")
        print("3. View all students")
        print("4. Add a student")
        print("5. Enroll student to course")
        print("6. Delete a student")
        print("7. Delete a course")
        print("8. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_courses()
        elif choice == "2":
            create_course()
        elif choice == "3":
            list_students()
        elif choice == "4":
            create_student()
        elif choice == "5":
            enroll_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            delete_course()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")
