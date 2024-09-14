def main():
    students = {}

    while True:
        action = input("Do you want to add a student name or enter a grade? (name/grade/exit): ").strip().lower()
        
        if action == "exit":
            break
        elif action == "name":
            student_name = input("Please enter the student's name: ").strip()
            if student_name in students:
                print(f"{student_name} is already in the list.")
            else:
                students[student_name] = None
                print(f"Added {student_name} to the list.")
        elif action == "grade":
            student_name = input("Please enter the student's name to add a grade: ").strip()
            if student_name in students:
                try:
                    grade = float(input(f"Please enter the grade for {student_name}: ").strip())
                    students[student_name] = grade
                    print(f"Added grade {grade} for {student_name}.")
                except ValueError:
                    print("Invalid grade. Please enter a valid number.")
            else:
                print(f"{student_name} is not in the list. Please add the student name first.")
        else:
            print("Invalid action. Please enter 'name', 'grade', or 'exit'.")

    print("\nAll students and their grades:")
    for student, grade in students.items():
        print(f"{student}: {grade}")

if __name__ == "__main__":
    main()