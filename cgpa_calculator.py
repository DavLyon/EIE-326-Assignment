def calculate_cgpa():
    print("CGPA Calculator for 6 Courses")
    print("-----------------------------")
    
    # Define grade points dictionary
    grade_points = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'F': 0.0
    }
    
    # Alternative grading system (can be commented out if not needed)
    # grade_points = {
    #     'A': 4.0,
    #     'B': 3.0, 
    #     'C': 2.0,
    #     'D': 1.0,
    #     'F': 0.0
    # }
    
    total_credit_units = 0
    total_grade_points = 0
    
    # Get input for each course
    for i in range(6):
        print(f"\nCourse {i+1}:")
        
        while True:
            course_name = input("Enter course name: ")
            if course_name:
                break
            print("Course name cannot be empty. Please try again.")
        
        while True:
            try:
                credit_units = float(input("Enter credit units: "))
                if credit_units > 0:
                    break
                print("Credit units must be positive. Please try again.")
            except ValueError:
                print("Please enter a valid number for credit units.")
        
        while True:
            grade = input("Enter grade (A, B, C, D, E, F): ").upper()
            if grade in grade_points:
                break
            print(f"Invalid grade. Please enter one of: {', '.join(grade_points.keys())}")
        
        # Calculate grade points for this course
        course_grade_points = credit_units * grade_points[grade]
        
        # Update totals
        total_credit_units += credit_units
        total_grade_points += course_grade_points
        
        # Display course summary
        print(f"Course: {course_name}, Units: {credit_units}, Grade: {grade}, Points: {course_grade_points:.2f}")
    
    # Calculate CGPA
    if total_credit_units > 0:
        cgpa = total_grade_points / total_credit_units
        print(f"\nTotal Credit Units: {total_credit_units}")
        print(f"Total Grade Points: {total_grade_points:.2f}")
        print(f"CGPA: {cgpa:.2f}")
    else:
        print("\nNo valid courses entered.")

# Run the program
if __name__ == "__main__":
    calculate_cgpa()
