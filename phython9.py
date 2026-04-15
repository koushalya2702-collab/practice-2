#Functions - Advanced Concepts
def display_info(name,age):
    print(f"name:{name} age:{age}")
display_info(name="koushalya",age=19)


# Variable-Length Arguments
def total_sum(*numbers):
    result=0
    for num in numbers:
        result+=num
    return result
print(total_sum(1,3,4,5,6,6))

#Using **kwargs
def student_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
student_info(name="koushalya",age=89,course="phython")


#Lambda Functions
double=lambda x:x*2
print(double(5))

#Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


#Lambda Function:
multiply=lambda x,y:x*y
print(multiply(3,4))

# #Recursive Function: 
# def sum(n):
#     if n==1:
#         return 1
    
#     return n + sum(n-1)
# print(sum(5))



#Variable-Length Arguments
def find_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

# Example
print(find_average(10, 20, 30))
print(find_average(5, 15))