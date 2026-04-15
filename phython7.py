#Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension

#Looping Through Lists
numbers = [2,6,8,9,4]
total = 0
for num in numbers:
    total += num
print("Total sum is: ",total)


# Doubling each number in a list
number = [4,5,6,7,2]
doubled = []
for num in number:
    doubled.append(num*2)
print("Doubled list: ",doubled)

#Looping Through Dictionaries
student_marks = {
    "Anand":79,
    "koushalya":90,
    "koushik":99
}
for student in student_marks:
    print(student)

# Iterating over dictionary values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)

#Iterating over both keys and values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")


#for Loops with range()
students = ["pavan","naveen","pranav"]
marks = [30,60,90]
student_marks = {}
for i in range(len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)

#List Comprehension
numbers = [3,4,6,7,8,9]
squares = [num ** 2 for num in numbers]
print(squares)

#Filtering even numbers
numbers = [3,4,6,7,8,9]
even_numbers = [num for num in numbers if num%2==0]
print(even_numbers)

#Dictionary Comprehension
numbers = [3,4,7,8,9]
square_dict = {num:num*2 for num in numbers}
print(square_dict)

#Converting a list of names to a dictionary of name lengths
names=["Anand","priya","kamala"]
names_lengths={name:len(name) for name in names}
print(names_lengths)

#Filtering cities with population above 10 lakhs
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)

#Splitting Strings to Create Lists
sentence="my name is koushalya"
words=sentence.split(" ",2)
print(words)

#List Manipulation
foods = ["rotti","palav","dosa","idli"]
upper_case=[food.upper() for food in foods]
print(upper_case)


#Sum of Prices
items = {
    "pen":5,
    "book":60,
    "pencil":10
}
amount = items.values()
print(sum(amount))

## Step 1: Create a list of dictionaries
students = [
    {"name": "Kiran", "age": 20, "marks": 85},
    {"name": "Anu", "age": 19, "marks": 90},
    {"name": "Rahul", "age": 21, "marks": 78}
]

for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Marks:", student["marks"])
    print("-------------------")

#Nested List Challenge
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print(row)

for row in matrix:
    print(sum(row))