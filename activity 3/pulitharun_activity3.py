def analyze_grades():
    """Analyzes student grades from a text file and generates a report.

    Raises:
        FileNotFoundError: If the grades file is not found.
        ValueError: If the file format is invalid.
    """

    grades_file = "E:\@tricon\phase 1\practices\grades.txt"  # Path to the grades file

    try:
        with open(grades_file, "r") as file:
            # Read student data into a dictionary
            students = {}
            for line in file:
                name, grade_str = line.strip().split(",")
                try:
                    grade = float(grade_str)
                    students[name] = grade
                except ValueError:
                    raise ValueError(f"Invalid grade format for student: {name}")

        # Calculate average grade
        total_grades = sum(students.values())
        average_grade = total_grades / len(students)

        # Find student with highest and lowest grades
        highest_grade = max(students.values())
        lowest_grade = min(students.values())
        highest_scorer = [name for name, grade in students.items() if grade == highest_grade][0]
        lowest_scorer = [name for name, grade in students.items() if grade == lowest_grade][0]

        # Generate report text
        report_text = f"""Average Grade: {average_grade:.2f}
Highest Grade: {highest_scorer} ({highest_grade})
Lowest Grade: {lowest_scorer} ({lowest_grade})"""

        # Write report to file
        with open("report.txt", "w") as report_file:
            report_file.write(report_text)

        print("Report generated successfully!")

    except FileNotFoundError:
        print(f"Error: File '{grades_file}' not found. Please ensure the file exists in the specified path.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_grades()  # Execute the analysis
