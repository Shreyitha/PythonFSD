import sys
def read_grades(filename):
    grades = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 2:
                    raise ValueError("Invalid file format")
                student_name, grade = parts
                grades[student_name] = float(grade)
        return grades
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        file.close()
def generate_report(grades, output_filename="report.txt"):
    try:
        average_grade = sum(grades.values()) / len(grades)
        highest_student, highest_grade = max(grades.items(), key=lambda x: x[1])
        lowest_student, lowest_grade = min(grades.items(), key=lambda x: x[1])

        with open(output_filename, 'w') as file:
            file.write(f"Average Grade: {average_grade:.2f}\n")
            file.write(f"Highest Grade: {highest_student} ({highest_grade:.2f})\n")
            file.write(f"Lowest Grade: {lowest_student} ({lowest_grade:.2f})\n")

        print(f"Report generated successfully. Check '{output_filename}' for the results.")
    except ZeroDivisionError:
        print("Error: No valid data found in the file.")
        sys.exit(1)

if __name__ == "__main__":
    grades_file = r"grades.txt"
    grades_data = read_grades(grades_file)
    generate_report(grades_data)
