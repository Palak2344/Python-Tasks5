def create_student_marks():
    """Create a dictionary of student marks."""
    return {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 88,
        "Eva": 95
    }

def get_student_marks(student_marks, student_name):
    """Retrieve the marks for a given student name."""
    return student_marks.get(student_name, None)

# Create the dictionary of student marks
student_marks = create_student_marks()

# Ask the user for a student's name
student_name = input("Please enter the student's name: ")

# Retrieve and display the corresponding marks
marks = get_student_marks(student_marks, student_name)

if marks is not None:
    print(f"{student_name}'s marks: {marks}")
else:
    print(f"Error: Student '{student_name}' not found.")
