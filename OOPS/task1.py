class Student:

    def marks(self,sub1,sub2,sub3):

        self.sub1 = sub1

        self.sub2 = sub2

        self.sub3 = sub3

    def avg(self):

        print(sum([self.sub1,self.sub2,self.sub3])/3)

obj1 = Student()

obj1.marks(70,80,75)

obj1.avg()
