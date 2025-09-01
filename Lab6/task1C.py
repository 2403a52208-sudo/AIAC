class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
if __name__ == "__main__":
    print("Enter student details:")
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    student1 = Student(name, roll_no, marks)
    student1.display_details()
    print()
    name2 = input("Enter second student name: ")
    roll_no2 = int(input("Enter second student roll number: "))
    marks2 = float(input("Enter second student marks: "))
    student2 = Student(name2, roll_no2, marks2)
    student2.display_details()