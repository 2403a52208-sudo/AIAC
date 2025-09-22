def welcome_student(name: str) -> None:
    """
    Print a welcome message for a single student.

    Args:
        name (str): The name of the student.
    """
    print("Welcome", name)


def welcome_students(student_list: list[str]) -> None:
    """
    Print welcome messages for a list of students.

    Args:
        student_list (list[str]): List of student names.
    """
    for student in student_list:
        welcome_student(student)


# Example usage:
students = ["Alice", "Bob", "Charlie"]
welcome_students(students)
