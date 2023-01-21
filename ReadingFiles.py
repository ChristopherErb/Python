#opening file, opening as "r" = read only, "w" = write,"a" = append, "r+" read/write

employee_file = open("employees", "r")

#is file readable?
print(employee_file.readable())
#prints all info in file
#print(employee_file.read())

#Reads first line
#print(employee_file.readline())


#Circulates through file and prints each line
for employee in employee_file.readlines():
    print(employee)


#Reads multiple lines into a list
#print(employee_file.readlines()[1])



employee_file.close()