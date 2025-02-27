# class     blueprint for creating objects

#           it is a design pattern for object

#           collection of objects

# syntax

# class class_name:

        # attribute1

# object    is an instance of class





# class Clasaname: >> creating a userdefined class

    # def method1(par1,par2): >> creating methods(functions inside a class) in the class

        # statement

        # return statement

# obj = classname()       >>> creating a object in the class

# obj.method1(par1=1,par2=3) >> only a class object can call its method





class Calculater:

    add = lambda self,*args : print(sum(args))

    sub = lambda self,x,y : print(x-y)

    def multiple(self,*args):

        product = 1

        for i in args:
            
            product *= i

        print(product)

    div = lambda self,x,y : print(x/y)

new = Calculater()

new.add(5,2,3)

new.sub(4,2)

new.multiple(2,4,2)

new.div(10,2)




