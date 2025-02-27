# create a class 

# method1(name,place,course)

# method2 >> display name and place

# class Details:

#     def meth1(self,name,place,course):

#         self.name = name

#         self.place = place

#         print(f"Hi {name}, you are doing {course} at {place}")

#     def meth2(self):

#         print(f"{self.name} is from {self.place}")

# person1 = Details()

# person1.meth1("Arthur","Dicathen","Mage")

# person1.meth2()




class Details:

    def user(self,name,place,course):

        self.name = name

        self.place = place

        print("Hi, how are you?")

    def greeting(self):

        print(self.name,self.place)


obj1 = Details()

obj2 = Details()

obj1.user(name="Arthur",place="Dicathen",course="Mage")

obj1.greeting()

obj2.user("Tessia","Elvendor","Mage")

obj2.greeting()


"""
self will keep values as attributes for the respectives objects.
whenever called it will fetch the corresponding values
"""