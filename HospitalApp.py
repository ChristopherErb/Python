from Hospital import Employee
from Hospital import Patient
employee_file = open("HospitalEmployees.txt", "a")

employee1 = Employee("Melanie", "Kline", 1, True, 25.00)
employee2 = Employee("Chris", "Erb", 3, False, 25.00)

Foofy = Patient("Foofy", "Dog", "West", "Good Boy", "Chris and Melanie", 7655887816)

employee3 = Employee(input("Please Enter the employee's name"), input("Please Enter last name"),
                    input("Please Enter shift worked"), input("Please enter whether registered"),
                     input("Please enter  pay rate"))

employee_file.write(employee1.nameFirst)
employee_file.write(" ")
employee_file.write(employee1.nameLast)
employee_file.write(" ")
employee_file.write(str(employee1.shift))
employee_file.write(" ")
employee_file.write(str(employee1.isRegistered))
employee_file.write(" ")
employee_file.write(str(employee1.pay))

employee_file.close()

print(employee1.nameFirst, employee1.nameLast, " Works on",  employee1.shift, " shift and makes", employee1.pay,
      " per hour.")
print(employee2.nameFirst, employee2.nameLast, " Works on",  employee2.shift, " shift and makes", employee2.pay,
      " per hour.")
print(Foofy.ptName, Foofy.ptDiagnosis, Foofy.ptLocation, Foofy.ptDiagnosis, Foofy.ptOwners, Foofy.ptOwnersNumber)

print(employee3.nameFirst)
