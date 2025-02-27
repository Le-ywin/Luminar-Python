class Student:

    def __init__(self,name,place):  # calls automatically when an object is being created >> construcor

        self.name = name

        self.place = place

        print("Uploaded Successfully")

    def display(self):

        print(self.name)

obj1 = Student(name="Grey",place="Dicathen")

obj1.display()