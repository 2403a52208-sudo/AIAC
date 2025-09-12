class sru_student:
    """
    Class representing a student at SRU with basic attributes and methods.
    """
    
    def __init__(self, name, roll_no, hostel_status):
        """
        Initialize a student with name, roll number, and hostel status.
    
        Args:
            name (str): Student's name
            roll_no (str): Student's roll number
            hostel_status (str): Whether student is in hostel or not
        """
        # Set basic student attributes
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False  # Default fee status - all students start with unpaid fees
    
    def fee_update(self, fee_status):
        """
        Update the fee payment status of the student.
        
        Args:
            fee_status (bool): True if fee is paid, False otherwise
        """
        # Update the fee status for this student
        self.fee_paid = fee_status
        
        # Provide feedback based on fee status
        if fee_status:
            print(f"Fee payment updated: {self.name} has paid the fees.")
        else:
            print(f"Fee payment updated: {self.name} has not paid the fees.")
    
    def display_details(self):
        """
        Display all details of the student.
        """
        # Create a formatted header for student details
        print("\n" + "="*40)
        print("STUDENT DETAILS")
        print("="*40)
        
        # Display all student information
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Status: {'Paid' if self.fee_paid else 'Not Paid'}")  # Convert boolean to readable text
        
        # Footer line for formatting
        print("="*40)

def get_student_input():
    """
    Function to get student details from user input.
    Returns a sru_student object.
    """
    # Display header for input section
    print("Enter Student Details:")
    print("-" * 20)
    
    # Get basic student information
    name = input("Enter student name: ").strip()  # Remove extra whitespace
    roll_no = input("Enter roll number: ").strip()
    
    # Display hostel status options
    print("Hostel Status Options:")
    print("1. Yes - Student lives in hostel")
    print("2. No - Student doesn't live in hostel")
    
    # Validate hostel choice input
    while True:
        hostel_choice = input("Enter choice (1 or 2): ").strip()
        if hostel_choice == "1":
            hostel_status = "Yes"
            break
        elif hostel_choice == "2":
            hostel_status = "No"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")  # Prompt for valid input
    
    # Create and return student object
    return sru_student(name, roll_no, hostel_status)

def get_fee_status():
    """
    Function to get fee payment status from user.
    Returns boolean value.
    """
    # Keep asking until valid input is provided
    while True:
        fee_input = input("Has the student paid fees? (y/n): ").strip().lower()  # Convert to lowercase for consistency
        
        # Check for positive responses
        if fee_input in ['y', 'yes']:
            return True
        # Check for negative responses
        elif fee_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Error message for invalid input

# Example usage and main program execution
if __name__ == "__main__":
    # Step 1: Get student details from user input
    student = get_student_input()
    
    # Step 2: Get fee payment status from user
    fee_paid = get_fee_status()
    student.fee_update(fee_paid)  # Update student's fee status
    
    # Step 3: Display complete student details
    student.display_details()
    
    # Step 4: Optional feature - Allow user to update fee status
    print("\nDo you want to update fee status? (y/n)")
    update_choice = input().strip().lower()
    
    # Update fee status if user chooses to do so
    if update_choice in ['y', 'yes']:
        new_fee_status = get_fee_status()  # Get new fee status
        student.fee_update(new_fee_status)  # Apply the update
        student.display_details()  # Show updated details
