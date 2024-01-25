def average_grades_cal(grades_data):
    try:
        total=sum(int(grade) for name, grade in grades_data)
        # print(average_grades)
        return total/len(grades_data)
    except TypeError as e:
        print('Type Error')

def highest_lowest_grades(grades):
    highest_grade=max(grades,key=lambda x:int(x[1]))[1]
    lowest_grade=min(grades,key=lambda x:int(x[1]))[1]
    # print(highest_grade)
    # print(lowest_grade)
    return highest_grade,lowest_grade

def write_report_file(grades,average,highest_grade,lowest_grade):
    write_file=open('Shreya_activity3_report.txt','w+')
    write_file.write(f"Average Grade: {average:.2f}\n")
    for name,grade in grades:
        if grade==highest_grade:
            write_file.write(f"Highest Grade: {name} ({grade})\n")
    for name,grade in grades:
        if grade==lowest_grade:
            write_file.write(f"Lowest Grade: {name} ({grade})\n")
            
try:
    file = open('grades.txt','r')
    lines = file.readlines()
    grades_data= [line.split() for line in lines]
    # print(grades_data)
except FileNotFoundError as e:
    print('File not Found')
    
average=average_grades_cal(grades_data)
highest_grade,lowest_grade=highest_lowest_grades(grades_data)
write_report_file(grades_data,average,highest_grade,lowest_grade)
