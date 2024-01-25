import sys

def read_grades_file(file_path):
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
    total = sum(int(grade) for _, grade in grades)
    return total / len(grades)

def analyze_grades(grades):
    if not grades:
        return None, None
    highest_grade = max(grades, key=lambda x: int(x[1]))[1]
    lowest_grade = min(grades, key=lambda x: int(x[1]))[1]

    highest_students = [(name, grade) for name, grade in grades if grade == highest_grade]
    lowest_students = [(name, grade) for name, grade in grades if grade == lowest_grade]

    return highest_students, lowest_students

def generate_report(average, highest, lowest):
    report = f"Average Grade: {average:.2f}\n"

    if highest:
        report += f"Highest Grade(s): "
        report += ', '.join(f"{name} ({grade})" for name, grade in highest)
        report += '\n'

    if lowest:
        report += f"Lowest Grade(s): "
        report += ', '.join(f"{name} ({grade})" for name, grade in lowest)
        report += '\n'

    return report

def write_report_to_file(report, output_file="report.txt"):
    try:
        with open(output_file, 'w') as file:
            file.write(report)
        print(f"Report generated successfully. Check '{output_file}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    file_path = "/content/sample_data/grades.txt"
    grades = read_grades_file(file_path)
    for student, grade in grades:
        if not grade.isdigit():
            print(f"Error: Invalid grade for {student}. Grades must be numeric.")
            sys.exit(1)

    average_grade = calculate_average(grades)
    highest_students, lowest_students = analyze_grades(grades)  
    report = generate_report(average_grade, highest_students, lowest_students)
    write_report_to_file(report)

if __name__ == "__main__":
    main()
