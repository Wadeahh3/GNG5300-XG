class Student:
    def __init__(self, name):
        self.name = name
        self.grade = None

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"{self.name}: {self.grade if self.grade is not None else 'No grade'}"

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print(f"{name} is already in the list.")
        else:
            self.students[name] = Student(name)
            print(f"Added {name} to the list.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].set_grade(grade)
            print(f"Added grade {grade} for {name}.")
        else:
            print(f"{name} is not in the list. Please add the student name first.")

    def print_all_students(self):
        print("\nAll students and their grades:")
        for student in self.students.values():
            print(student)

def main():
    manager = StudentManager()

    while True:
        action = input("Do you want to add a student name or enter a grade? (name/grade/exit): ").strip().lower()
        
        if action == "exit":
            break
        elif action == "name":
            student_name = input("Please enter the student's name: ").strip()
            manager.add_student(student_name)
        elif action == "grade":
            student_name = input("Please enter the student's name to add a grade: ").strip()
            try:
                grade = float(input(f"Please enter the grade for {student_name}: ").strip())
                manager.add_grade(student_name, grade)
            except ValueError:
                print("Invalid grade. Please enter a valid number.")
        else:
            print("Invalid action. Please enter 'name', 'grade', or 'exit'.")

    manager.print_all_students()

if __name__ == "__main__":
    main()