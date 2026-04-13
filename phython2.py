fruits = ("apple", "banana", "cherry")
print(fruits[0])  
print(fruits[-1])  #Accessing Tuple Elements


#Tuple Operations
tuple1=(1,2,3)
tuple2=(4,5,6)
combine_tuple=tuple1 + tuple2
print(combine_tuple)

repeated_tuple = (1, 2) * 3
print(repeated_tuple)  


#Checking Membership
fruits=["apple","cherry","banana"]
print("apple" in fruits)
print("banana" not in fruits)


#Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  
intersection_set = set1 & set2  
difference_set = set1 - set2  
sym_diff_set = set1 ^ set2  