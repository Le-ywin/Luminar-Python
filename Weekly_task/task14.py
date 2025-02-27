# wap that reverses each word in a given sentence while keeping their order the same

# hello world -> olleh dlrow

word = input("Enter a Sentence : ")

new = [i[::-1] for i in word.split()]

for i in new:

    print(i,end=" ")

