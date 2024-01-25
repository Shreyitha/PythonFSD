# Reading the grades.text file

def read_file():
    try:
        file = open('grades.txt','r')
        lines = file.readlines()
        grades_data = [line.strip().split() for line in lines]
        #print(grades_data)
    except FileNotFoundError:
        print(f'File not found')
    except Exception as e:
        print(f"Can't read file {e}")
#read_file()


# Calculating average of the scores
def calc_average():
    try:
        total_score = sum(int(score) for name, score in grades_data)
        average_score = total_score / len(grades_data)
        #print(f'Average_score is {average_score}')
        return average_score
    except Exception as e:
        print(e)
#calc_average()

# Finding the student with highest score
def Highest_score():
    max_grade= 0
    student = ''
    
    for name, grade in grades_data:
        current_grade = int(grade)
        if current_grade > max_grade:
            max_grade = current_grade
            student = name
    #print(f'Highest grade is {max_grade} and the student is {student}')
    return max_grade, student
#Highest_score()

#Finding the student with lowest score
def Lowest_score():
    min_grade=None
    student = ''
   
    for name, grade in grades_data:
        current_grade = int(grade)
        if min_grade is None or current_grade < min_grade:
            min_grade = current_grade
            student = name
    #print(f'Lowest grade is {min_grade} and the student is {student}')
    return min_grade, student
#Lowest_score()

# Creating and writing to the report
def write_report(average, highest, lowest):
    try:

        file = open('report.txt','w')
        file.write(f"Average_score {average:.2f} \n" )
        file.write(f"Highest_score  {highest[0]} : {highest[1]}\n")
        file.write(f"Lowest_score {lowest[0]} : {lowest[1]}\n")
    except Exception as e:
        print(f"Can't create a file {e}")

average = calc_average()
highest = Highest_score()
lowest = Lowest_score()
write_report(average, highest, lowest)       

            