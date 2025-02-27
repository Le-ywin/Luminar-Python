# create a class REctsangle

# method 1 length and breadth

# method 2 perimeter

# method 3 area

class Rectangle:

    def __init__(self,length,breadth):

        self.length = length

        self.breadth = breadth
        
        print("Value uploaded")

    def perimeter(self):

        print(2*(self.length + self.breadth))

    def area(self):

        print(self.length*self.breadth)

obj1 = Rectangle(5,4)

obj1.perimeter()

obj1.area()