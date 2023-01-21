#from student file, import student class
from Student import Student

#creates the object "student" with the params
student1 = Student("Chris", "Psychology", 3.8, False)
student2 = Student("Pam", "Art", 1.5, True)


print(student1.gpa, student1.name)
print(student2.gpa)