def smallest(x,y,z):

    print(x if x < y and x < z else y if y < x and y < z else z)

smallest(8,5,3)