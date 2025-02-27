# class Student

# meth = nmae, age, mark

# meth2 = mark update

# meth3 delete a student record

class Student:

    def __init__(self):
        
        self.student = {}

    def new_id(self,name,age,mark):

        self.mark = mark

        self.student[name] = {"age" : age,"mark" : mark}

    def update(self,new,name):

        self.student[name]["mark"] = new

        print(f"New mark is {self.mark}")

    def delete(self,name):

        self.student.pop(name)

    def display(self):

        print(self.student)


class_A= Student()

class_A.new_id(name="Ram",age=20,mark=75)

class_A.new_id(name="Leywin",age=20,mark=75)

class_A.display()

class_A.update(new=80,name="Leywin")

class_A.display()