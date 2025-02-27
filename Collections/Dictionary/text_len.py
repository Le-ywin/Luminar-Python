text = "python is a good programming language"

# {"python":[6],................,"language":[8]}

new = {}

for i in text.split(" "):

    new[i] = [len(i)]

print(new)