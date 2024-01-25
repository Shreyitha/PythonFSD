import os

def read_grades(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"{file_name} does not exist.")
    
    grades = {}
    with open(file_name, 'r') as file:
        for line in file:
            try:
                name, grade = line.strip().split()
                grades[name] = float(grade)
            except ValueError:
                raise ValueError("Each line should contain a name and a grade.")
    return grades

def analyze_grades(grades):
    if not grades:
        raise ValueError("No grades to analyze.")
    
    total = sum(grades.values())
    average = total / len(grades)
    highest = max(grades, key=grades.get)
    lowest = min(grades, key=grades.get)
    return average, highest, lowest

def generate_report(file_name, average, highest, lowest):
    with open(file_name, 'w') as file:
        file.write(f"Average Grade: {average:.2f}\n")
        file.write(f"Highest Grade: {highest} ({grades[highest]})\n")
        file.write(f"Lowest Grade: {lowest} ({grades[lowest]})\n")

try:
    grades = read_grades("grades.txt")
    average, highest, lowest = analyze_grades(grades)
    generate_report("saksha_report.txt", average, highest, lowest)
except Exception as e:
    print(f"An error occurred: {e}")
