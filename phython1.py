fruits=["Apple","banana","Cherry"]
print(fruits[1])         #Accessing list element
print(fruits[-1]) 


fruits=["Apple","banana","Cherry"]
fruits[1]="orange"       #Modifying list element
print(fruits) 


fruits=["Apple","banana","Cherry"]
fruits.append("Kiwi")       #Adding element
print(fruits) 

fruits=["Apple","banana","Cherry"]
fruits.insert(0,"kiwi")        #Adding list element to specific index
print(fruits) 

fruits=["Apple","banana","Cherry"]
fruits.remove("Apple")        #removing element
print(fruits) 

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  
print(numbers[:4])      #Slicing Lists
print(numbers[2:])  
print(numbers[::2])  

#Common functions
numbers = [0, 1, 2, 3, 4, 5, 6]
print(len(numbers))

numbers=[4,2,6,5,3,9,7]
print(sorted(numbers))


numbers=[4,2,6,5,3,9,7]
numbers.sort(reverse=True)
print(numbers)

numbers=[4,2,6,5,3,9,7]
print(sum(numbers))

#Nested list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][2])

#List Manipulation Exercise:

items=["onion","potato","beans","beetroot","radish"]
items.append("carrot")
print(items)
items.pop(3)
print(items)

numbers=[9,4,5,3,2,7,8]
print(sorted(numbers))
numbers.sort(reverse=True)
print(numbers)






