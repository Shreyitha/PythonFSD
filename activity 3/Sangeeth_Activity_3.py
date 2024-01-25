#open the given file grades.txt

try:
    file= open('grades.txt','r')

except FileNotFoundError:
    print("File does not exist")   

#extracting the requirements
    
content=file.read() 
list= content.split()
sum=0
convert_dict= map(lambda i: (list[i], int(list[i+1])), range(len(list)-1)[::2])
dict= dict(convert_dict)
for i in dict.values():
    sum+=i
avg=format(sum/len(dict.values()), '.2f')
max= max(dict.values())
min= min(dict.values())
max_dict={}
min_dict={}
for i in dict.items():
    if i[1]==max:
        max_dict[i[0]]=i[1]
    elif i[1]==min:
        min_dict[i[0]]=i[1]


#writing the results to result.txt
with open("Sangeeth_Report.txt", 'w') as result:  
    result.write("Average Grade: "+ str(avg)+"\n")
    for key, value in max_dict.items():  
        result.write('Highest Grade: %s (%s)\n' % (key, value))
    for key, value in min_dict.items():  
        result.write('Lowest Grade: %s (%s)\n' % (key, value))    









