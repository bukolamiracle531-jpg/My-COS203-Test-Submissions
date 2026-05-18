def get_student_data():
    """
    Accepts student name, matric number, and score from the user.
    """
    name = input("Enter Student Name: ").strip()
    matric_number = input("Enter Matric Number: ").strip()
    
    while True:
        try:
            score = float(input("Enter Student Score (0-100): "))
            return name, matric_number, score
        except ValueError:
            print("Invalid input! Please enter a valid number for the score.")
