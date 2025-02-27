def duplicate(elements):

    new = []
    
    for i in elements:

        if i not in new:

            new.append(i)

    print(new)

duplicate([1,2,1,3,4,5,4,2])