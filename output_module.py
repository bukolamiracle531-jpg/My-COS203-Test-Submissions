def display_result(name, matric_number, score, grade):
    """Displays a well-formatted summary of the student's academic record."""
    print("\n" + "="*40)
    print("         STUDENT ACADEMIC RECORD        ")
    print("="*40)
    print(f"Name:          {name}")
    print(f"Matric No:     {matric_number}")
    print(f"Score:         {score:.2f}")
    print(f"Grade:         {grade}")
    print("="*40 + "\n")
