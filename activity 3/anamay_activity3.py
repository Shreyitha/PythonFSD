'''
Date - 25/01/24
Written by - Anamay Dubey
Title - Solution of activity 3 using file-handling and exception handling
Task - TO readh "grades.txt" and caluculate avg marks and mentioning rank1 and last rank student name
and storing these details in a seprate "report.txt" file
'''

def get_key_from_value(dictionary, value): # finds key to specific value from dict
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def genrate_report(file_name): # method to genrate report with required details
    try:  # exception handling
        with open(file_name, "r") as file: # opening the grades.txt file
            student_data = {} # empty dictionary
            for line in file:
                name, marks_str = line.strip().split() # seprating name and marks from each line
                marks = int(marks_str) # converting marks string to marks int type
                student_data[name] = marks

            if student_data:  # Check if the dictionary is not empty
                max_marks = max(student_data.values())
                min_marks = min(student_data.values())

                student_max_marks_name = get_key_from_value(student_data, max_marks)
                student_min_marks_name = get_key_from_value(student_data, min_marks)
                avg_grade = sum(student_data.values()) / len(student_data)

                with open("anamay_report.txt", "a") as report: # creating report.txt file
                    report.write(f"Average Grade: {avg_grade}\n")
                    report.write(f"Highest Grade: {student_max_marks_name} ({max_marks})\n")
                    report.write(f"Lowest Grade: {student_min_marks_name} ({min_marks})\n")
            else: # if dict is empty 
                print("No student data available. Cannot generate report.")
                
    except FileNotFoundError as f:
        print(f"{f} File can not be found")
    except ValueError as ve:
        print(f"{ve} Grades are not numeric values")
    except Exception as e:
        print(f"{e} Error")

genrate_report("grades.txt") # calling the report_genrate method
