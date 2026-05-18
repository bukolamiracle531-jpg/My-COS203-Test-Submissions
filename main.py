import input_module
import logic_module
import output_module

def main():
    print("Welcome to the Modular Student Grading System")
    
    while True:
        # i. Gather input details
        name, matric, score = input_module.get_student_data()
        
        # ii. Validate and process data using logic module
        if logic_module.validate_score(score):
            grade = logic_module.calculate_grade(score)
            
            # iii. Display formatted result
            output_module.display_result(name, matric, score, grade)
        else:
            print(f"\nError: The score {score} is out of bounds (0-100). Record skipped.\n")
            
        # Check if the user wants to terminate the program execution
        choice = input("Do you want to enter another student record? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("Exiting Student Grading System. Goodbye!")
            break

if __name__ == "__main__":
    main()
