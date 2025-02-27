# LIST
# =====

# items = [1, 2, 3, 4, 5]

# print(items[0])  # 1

# print(items[-1])  # 5

# List       : collection, python used to assign more than one element to a variable

# List       : is heterogenous, mutable , ordered(indexed), allows duplicate, and iterable

# items = ['name','ram','place','palakkad','pin',679515]

# print(items)

# print(len(items))

# print(items.index('ram'))

# print(items[-1])

# for i in range(1, 11):

# for i in "hari"

# items = [1,2,3,4,5] # itrable

# for i in items:

#     print(i)





# LIST METHODS
# =============



# 1. append() : adds an element to the end of the list

# items = [1,2,3,4,5]

# new = [10,9,8,7]

# items.append(new)

# items.append('hari')

# print(items)





# 2. insert() : inserts an element at a specified position

# items = [1,2,3,4,5]

# items.insert(2,'hari')

# print(items)





# 3. extend() : adds multiple elements to the end of the list

# items = [1,2,3,4,5]

# new = [10,9,8,7]

# items.extend(new)

# items.extend('hari')

# items.extend([1,2,3])

# print(items)





# 4. remove() : removes the first occurrence of the specified element

# items = [1,2,3,4,5]

# items.remove(3)

# print(items)





# 5. pop() : removes and returns the element at the specified position
#            if no index is specified, it removes and returns the last element

# items = [1,2,3,4,5]

# items.pop(2)

# items.pop()

# print(items)

# print(items.pop())

# print(items.pop(0))





# 7. index() : returns the index of the first occurrence of the specified element

# only print the index of the first occurrence of the specified element

# items = [1,2,3,4,5,1]

# print(items.index(1))

# print(items.index(5))





# 6. sort() : sorts the list in ascending order

#             if reverse is true, it sorts in descending order

items = [5,2,8,1,9]

items.sort()

# items.sort(reverse=True)

print(items)





# 7. remmove() : removes the first occurrence of the specified element

# items = [1,2,3,4,5]

# items.remove(2)

# print(items)

# print(items.remove(2))





# 8. couont() : returns the number of occurrences of the specified element

# items = [1,2,3,4,5,1]

# print(items.count(1))




# 9. clear() : removes all elements from the list

# items = [1,2,3,4,5]

# items.clear()

# print(items)

# print(items.clear())
