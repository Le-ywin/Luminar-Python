items = [1,True,"Arthur",5.6]

file = open("text.txt","w")

for i in items:
    
    file.write(str(i))

