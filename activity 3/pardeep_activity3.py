#!/usr/bin/env python
# coding: utf-8

# In[56]:


import os

def read_grades(file_path):
    grades = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    student_name, grade_str = parts
                    if grade_str.isdigit():
                        grades[student_name] = int(grade_str)
                    else:
                        raise ValueError("Invalid grade format.")
                else:
                    raise ValueError("Invalid line format.")
    except FileNotFoundError:
        print("Error: File 'grades.txt' not found.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
    return grades

def generate_report(grades, report_file_path):
    if grades is None:
        return
    
    avg_grade = sum(grades.values()) / len(grades)
    highest_stu, highest_grade = max(grades.items(), key=lambda x: x[1])
    lowest_stu, lowest_grade = min(grades.items(), key=lambda x: x[1])

    report_content = f"Average Grade: {avg_grade:.2f}\n"
    report_content += f"Highest Grade: {highest_stu} ({highest_grade})\n"
    report_content += f"Lowest Grade: {lowest_stu} ({lowest_grade})"

    with open(report_file_path, 'w') as report_file:
        report_file.write(report_content)

if __name__ == "__main__":
    grades_file_path = "grades.txt"
    report_file_path = "pradeep_report.txt"

    grades_data = read_grades(grades_file_path)
    
    if grades_data:
        generate_report(grades_data, report_file_path)
        print(f"Report generated successfully: {report_file_path}")


# In[ ]:




