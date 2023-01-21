from Chef import Chef
#creates new chinesechef class that contains all of the things a normal chef can do.. (chef)
#uses Inheritance and Chef files
class ChineseChef(Chef):
#give ChineseChef all functionality of normal chef

#overwrites the normal special dish thing
    def make_Special_dish(self):
        print("The chef makes orange chicken2")
#makes fried rice
    def make_Fried_rice(self):
        print("The chef makes fried rice")
