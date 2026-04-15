#for loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)

#Using range() with for Loops
for i in range(1,11):
    print(i)


#Counting by 2s from 1 to 10
for i in range(1,11,2):
    print(i)


#Looping Over Strings
name = "Karnataka"
for letter in name:
    print(letter)


#Nested for Loops
for i in range(1,6):
    for j in range(1,6):
        print(f"{i} x {j} = {i*j}")  
    print() 


# Using break in a for Loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Mysuru":
        print(f"found {city}")
        break
    print(city)

# Using continue in a for Loop
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Mysuru":
        continue
    print(city)

# Looping Through a List with enumerate()
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f" city {index+1}:{city}")


#Multiples of 3:
for i in range(0,30,3):
    print(i)

#Sum of First 10 Numbers:
sum=0
number = [2,3,4,5,6]
for num in number:
    sum += num
print(sum)

#Count Vowels in a String:
count = 0
vowel = "aeiou"
str = input("Enter a string: ").lower()
for letter in str:
    if letter in vowel:
        count += 1
print(count)


