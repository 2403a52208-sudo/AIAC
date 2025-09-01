class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def display_details(self):
        print(f"Name: {self.name}, Roll: {self.rollno}, Marks: {self.marks}")
    def calculate_grade(self):
        if self.marks >= 90: return "A"
        elif self.marks >= 75: return "B"
        elif self.marks >= 60: return "C"
        else: return "Fail"
name = input("Enter name: ")
rollno = int(input("Enter roll no: "))
marks = int(input("Enter marks: "))
student = Student(name, rollno, marks)
student.display_details()
print(f"Grade: {student.calculate_grade()}")