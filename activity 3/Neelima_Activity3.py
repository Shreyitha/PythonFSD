import sys
def read_grades(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip().split() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def calculate_average(grades):
    if not grades:
        return 0.0
    total = sum(float(grade) for _, grade in grades)
    return total / len(grades)

def generate_report(average, highest, lowest):
    with open("report.txt", 'w') as report_file:
        report_file.write(f"Average Grade: {average:.2f}\n")
        report_file.write(f"Highest Grade: {highest[0]} ({highest[1]})\n")
        report_file.write(f"Lowest Grade: {lowest[0]} ({lowest[1]})\n")

def analyze_grades(data):
    if not data:
        print("Error: No data found in the file.")
        sys.exit(1)

    grades = [(name, float(grade)) for name, grade in data]

    average_grade = calculate_average(grades)
    highest_grade = max(grades, key=lambda x: x[1])
    lowest_grade = min(grades, key=lambda x: x[1])

    generate_report(average_grade, highest_grade, lowest_grade)

if __name__ == "__main__":
    try:
        grades_data = read_grades("C:\\Users\hp\grades.txt")
        analyze_grades(grades_data)
        print("Report generated successfully. Check 'report.txt'")
    except ValueError:
        print("Error: Invalid grade format in the file.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)