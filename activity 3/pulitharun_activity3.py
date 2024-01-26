# Function to read grades from a file and store them in a dictionary
def read_grades(file_path):
    grades = {}
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Process each line and extract student name and grade
            for parts in lines:
                parts = parts.strip().split()
                # Check if the line has exactly two parts (student name and grade)
                if len(parts) == 2:
                    student_name, grade_str = parts
                    # Check if the grade is a valid integer
                    if grade_str.isdigit():
                        grades[student_name] = int(grade_str)
                    else:
                        raise ValueError("Invalid grade format.")
                else:
                    raise ValueError("Invalid line format.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    return grades

# Function to calculate the average grade 
def calculate_average(grades):
    return sum(grades.values()) / len(grades)

# Function to find the student with the highest grade
def find_highest_grade_student(grades):
    max_student = max(grades, key=grades.get)
    return max_student, grades[max_student]

# Function to find the student with the lowest grade
def find_lowest_grade_student(grades):
    min_student = min(grades, key=grades.get)
    return min_student, grades[min_student]

def generate_report(grades, report_file_path):

    # Calculate average, find highest and lowest grades
    average_grade = calculate_average(grades)
    highest_student, highest_grade = find_highest_grade_student(grades)
    lowest_student, lowest_grade = find_lowest_grade_student(grades)

    # Create the report 
    report =  f"Average Grade : {average_grade:.2f}\n"
    report += f"Highest Grade : {highest_student} ({highest_grade})\n"
    report += f"Lowest Grade  : {lowest_student} ({lowest_grade})"

    # Write the report to a file
    with open(report_file_path, 'w') as report_file:
        report_file.write(report)

if __name__ == "__main__":
    grades_file_path = "E:/@tricon/phase 1/practices/grades.txt"
    report_file_path = "E:/@tricon/phase 1/practices/report.txt"
    grades_data = read_grades(grades_file_path)
    
    # If grades data is available, generate and print the report
    if grades_data:
        generate_report(grades_data, report_file_path)
        print(f"Report generated successfully: {report_file_path}")
    else:
        print("Report generation failed.")
