# 1. Data Types in Python

### a) numeric data types

a = 10     
b = 3.14   
c = 2 + 3j  

print(type(a))  
print(type(b))  
print(type(c))  

### b) Sequence Data Types

name = "Python"  
numbers = [1, 2, 3, 4]  
coordinates = (10.5, 20.3) 

print(type(name)) 
print(type(numbers))
print(type(coordinates))  

### c) Set and Dictionary Data Types

unique_numbers = {1, 2, 3, 3} 
person = {'name': 'John', 'age': 25}

print(type(unique_numbers)) 
print(type(person))  

# 2. Operators in Python

### a) Arithmetic Operators
a = 10
b = 3

print(a + b)  
print(a - b) 
print(a * b) 
print(a / b)  
print(a % b) 
print(a ** b)  
print(a // b)

### b) Comparison Operators
x = 5
y = 10

print(x == y)  
print(x != y)  
print(x > y)   
print(x < y)  
print(x >= y)  
print(x <= y)  

### c) Logical Operators

a = 5
b = 10

print(a > 2 and b < 15)  
print(a > 10 or b < 15)  
print(not (a > 2))  

### d) Assignment Operators

x = 10
x += 5  
x -= 3  
x *= 2 
x /= 4  

print(x)  # 6.0

### e) Membership Operators

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  
print("grape" not in fruits)  

# 3. Conditional Statements in Python

### a) if Statement

age = 18

if age >= 18:
    print("You are eligible to vote.")

### b) if-else Statement

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

### c) if-elif-else Statement

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")

### d) Nested if Statement

num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")