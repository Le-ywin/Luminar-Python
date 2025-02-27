name = input("May i ask what your name is? : ")

print(f"{name} has now been invited to the party.")

count = 1

while(count >= 1):

    ask = input("Will you be bringing a guest? (y/n) : ")

    if ask.lower() == "y":
        
        guest = input("May i know the name of your guest? : ")
        
        count += 1
    
    elif ask.lower() == "n":
        
        print(f"So, it will be {count} people including you.")
        
        break
