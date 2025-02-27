# student management system

# add(id,name,age,grade)

# delete a student

# display grade of a student

# update grade of a student

class SMS():

    def __init__(self):
        
        self.new = {}

    def add(self,id,name,age,grade):

        self.grade = grade

        self.name = name

        self.id = id

        self.new[id] = {"name":name,"age":age,"grade":grade}

    def delete(self,id):

        self.new.pop(id)

        # print(f"The following Student has been deleted : {self.new[id][self.name]}")

    def display(self,id):

        print(self.new[id]["grade"])

    def update(self,id,grade):

        self.new[id]["grade"] = grade

        print(f"Newly updated grade is : {self.new[id]["grade"]}")



Mage = SMS()

Mage.add(id=1,name="Arthur Leywin",age=19,grade=98)

Mage.add(id=2,name="Tessia Eralith",age=19,grade=99)

Mage.display(1)

Mage.update(1,100)

Mage.delete(id=1)

Mage.display(1)