# wap to identify the most recursive element in the list

element = [1,4,3,5,1,3,2,6,7,2]

most = 0

count = 0

for i in element:

    if element.count(i) > most:

        count = element.count(i)
        
        most = i

print(f"The most recursive number is {most} and the count is {count}")