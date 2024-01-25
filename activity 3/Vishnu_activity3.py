grades = ""
try:
    file = open("grades.txt", 'r')
    lines = file.readlines()
    grades = [line.strip() for line in lines]
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error occurred while reading file: {e}")

dict_grades = {}
for i in range(len(grades)):
  dict_grades[grades[i][:-3]] = int(grades[i][-2:])
Averagegrade = (sum(dict_grades.values()))/len(dict_grades.values())

highestgrade = []
lowestgrade = []
Max = max(dict_grades.values())
Min = min(dict_grades.values())

for name,grades in dict_grades.items():
    if grades == Max:
        highestgrade.append(name)
    if grades == Min:
        lowestgrade.append(name)
highestgrade = [highestgrade]
lowestgrade = [lowestgrade]
highestgrade.append(Max)
lowestgrade.append(Min)

try:
    report_file = open("Vishnu_activity3_report.txt", 'w')
    report_file.write(f"Average Grade: {Averagegrade:.2f}\n")
    for j in range(len(highestgrade[0])):
        report_file.write(f"Highest Grade: {highestgrade[0][j]} ({highestgrade[1]})\n")
    for k in range(len(lowestgrade[0])):
        report_file.write(f"Lowest Grade: {lowestgrade[0][k]} ({lowestgrade[1]})\n")
    print("Report file is created.")
except Exception as e:
    print(f"Error while creating report file: {e}")




