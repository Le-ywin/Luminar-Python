# *args,**kwargs

# *args allow you to pass mmultiple arguements to a function

def additon(*args):    

    sum = 0

    for i in args:

        sum += i

    print(sum)


additon(1,2,3)

additon(1,2,3,4,5)



# **kwargs allow you to pass multiple keyword arguements to a function

def details(**kwargs):

    print(kwargs)

details(name = "Arthur Leywin",location = "Dication",position = "Lance")

