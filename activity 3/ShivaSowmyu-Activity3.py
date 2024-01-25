#Checking whether the file exists or not
try:
    with open('grades.txt','r') as fp:
        stu_data =dict()
        total_data=fp.readlines()
        for d in total_data:
            single_data=d.split(' ')
            stu_data.update({single_data[0]:int(single_data[1])})
        fp.close()
except FileNotFoundError:
    print("File does not exist") 
    exit()


#Average,Max,Min evaluation
    
def average_grade_evaluation(data):
    total_students=len(data)
    avg=format(sum(data.values())/total_students, '.2f')
    maximum= max(data.values())
    minimum= min(data.values())
    max_values=dict()
    min_values=dict()
    for k,v in data.items():
        if(v==maximum):
            max_values.update({k:v})
        if(v==minimum):
            min_values.update({k:v})
    report_generation(avg,max_values,min_values)

#Report generation Function
    
def report_generation(avg,max_values,min_values):   
    with open('ShivaSowmyaReport.txt','w') as fp:
        fp.write("Average Grade : {}\n".format(avg, '.2f'))
        print("Highest Grade students :\n")
        for k,v in max_values.items():
            fp.write("Highest Grade : {} ({})\n".format(k,v))
            print("{}\n".format(k))
        print("Lowest Grade students :\n")
        for k,v in min_values.items():
            fp.write("Lowest Grade : {} ({})\n".format(k,v))
            print("{}\n".format(k))
    fp.close()


average_grade_evaluation(stu_data)