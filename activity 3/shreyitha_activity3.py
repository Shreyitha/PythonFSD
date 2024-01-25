def read_grades(filename):
    """
    Read grades from a text file and return a dictionary with student names as keys and grades as values.
    """
    grades = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) != 2:
                    raise ValueError("Incorrect file format")
                name, grade = data
                if not grade.isdigit():
                    raise ValueError("Non-numeric grade found")
                grades[name.strip()] = int(grade)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist")
    except ValueError as ve:
        raise ValueError(f"Error in file: {ve}")
    return grades

def generate_report(grades):
    """
    Generate a report with average grade, highest grade, and lowest grade.
    """
    if not grades:
        return "No grades found."

    average_grade = sum(grades.values()) / len(grades)
    highest_grade = max(grades.items(), key=lambda x: x[1])
    lowest_grade = min(grades.items(), key=lambda x: x[1])

    report = f"Average Grade: {average_grade:.2f}\n"
    report += f"Highest Grade: {highest_grade[0]} ({highest_grade[1]})\n"
    report += f"Lowest Grade: {lowest_grade[0]} ({lowest_grade[1]})\n"

    return report

def main():
    try:
        grades = read_grades("grades.txt")
        report = generate_report(grades)
        with open("report.txt", "w") as file:
            file.write(report)
        print("Report generated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
