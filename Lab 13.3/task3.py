class Student:
    """
    Represents a student with a name, age, and marks in three subjects.
    Provides methods to display details and calculate total marks.
    """

    def __init__(self, name, age, marks):
        """
        Initialize the Student object.

        :param name: str - Name of the student
        :param age: int - Age of the student
        :param marks: list - List containing marks in 3 subjects
        """
        self.name = name
        self.age = age
        self.marks = marks  # e.g., [85, 90, 88]

    def display_details(self):
        """Display the student's name and age."""
        print(f"\nStudent Name: {self.name}")
        print(f"Student Age: {self.age}")

    def total_marks(self):
        """Return the total marks of the student."""
        return sum(self.marks)


def main():
    """Main function to get user input and display student details."""
    try:
        name = input("Enter student's name: ").strip()
        age = int(input("Enter student's age: "))

        marks = []
        print("Enter marks for 3 subjects:")
        for i in range(3):
            mark = float(input(f"  Subject {i + 1}: "))
            marks.append(mark)

        student = Student(name, age, marks)

        # Display student info
        student.display_details()
        print(f"Marks: {marks}")
        print(f"Total Marks: {student.total_marks()}")

    except ValueError:
        print(" Invalid input! Please enter numeric values for age and marks.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
