#Appending to file = adding text to the end  "a"
employee_file = open("employees", "a")

#Writing to file = adding text to the end  "W".. Write overwrites the entire file.. Added a new file if the name was different from opened one
employee_file = open("employees1", "w")


employee_file.write("\nKelly - Customer Service")

#print(employee_file.read())


employee_file.close()