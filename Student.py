class Student:

    #initialize function to add attributes. is_on_probation is boolean
    def __init__(self, name, major, gpa):
    #Values that are being passed into the object..
    # Self.name = the objects name is equal to the name that we assign.. Name of student object is name we give it..
        self.name = name
    # Self.major = the objects major is equal to the major that we assign.. Name of major of the student we created etc
        self.major = major
        self.gpa = gpa
       # self.is_on_probation = is_on_probation
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False