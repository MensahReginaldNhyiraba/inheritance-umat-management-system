# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class: Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # Overriding display_info()
    def display_info(self):
        super().display_info()
        print("Student ID:", self.student_id)

    def enroll_course(self, course):
        print(self.name, "has enrolled in", course)


# Child Class: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def teach_course(self, course):
        print(self.name, "is teaching", course)


# Creating objects
student1 = Student("Reginald Mensah", 21, "UMAT202501")
lecturer1 = Lecturer("Dr. Cobbinah", 45, "EMP1001")


# Demonstrating inherited method
print("===== STUDENT DETAILS =====")
student1.display_info()
student1.enroll_course("Object-Oriented Programming")

print("\n===== LECTURER DETAILS =====")
lecturer1.display_info()
lecturer1.teach_course("Object-Oriented Programming")