# Types and Syntax of loop in python 
# There are two types of loop in python 
# 1. while Loop
# 2. for Loop

# while Loop
# while loop is used to execute a block of code as long as the condition is true.
''' while condition:
    code to be executed
'''

# write a python program to print numbers from 1 to 10 using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# write a python program to print the content of list using while loop
fruits = ['apple', 'banana', 'cherry']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
    
    
# for loop
# for loop is used to execute a block of code for each item in a sequence (such as a list, tuple, dictionary, set, or string).
# The syntax of for loop is as follows:
''' for variable in sequence:
    code to be executed
'''
# write a python program to print numbers from 1 to 10 using for loop
for i in range(1, 11): # here i starts from 0 by default
    print(i)
    
for i in range(10): # here i starts from 0 by default
    print(i+1)
    
# write a python program to print the content of list using for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit) 
    
    
# range () function
# The range() function returns a sequence of numbers, starting from the first specified number up to, but not including, the second specified number.
# The syntax of range() function is as follows:
# range(start, stop, step-size)
# start: The starting number of the sequence. Default is 0.
# stop: The end number of the sequence. Default is the maximum limit of the data type.
# step-size: The difference between each number in the sequence. Default is 1.

# write a python program to print numbers from 1 to 10 using range() function
for i in range(1, 11):
    print(i)

# write a python program to print numbers from 10 to 1 using range() function
for i in range(10, 0, -1):
    print(i)
# write a python program to print numbers from 1 to 10 with a step size of 2
for i in range(1, 11, 2):
    print(i)
# write a python program to print numbers from 10 to 1 with a step size of 2
for i in range(10, 0, -2):
    print(i)
# write a python program to print numbers from 1 to 10 without start and step-size
for i in range(10):
    print(i+1)
#write a python program to print numbers from 10 to 1 without start and step-size
for i in range( 10, -1): 
    print("Check")
    print(i)
'''this code will not work beacuse we want to print from 10 to 1 and 
    there is missing step size, we need to put step size as -1 beause step size 
    by default consider as 1 and if we don't put step size then it will consider
    1 as step size which doesn't make sense in this case
'''    
    
    
# for loop with else clause
# The else clause is used with for loop to execute a block of code when the loop finishes normally
# The syntax of for loop with else clause is as follows:
# for variable in sequence:
#     code to be executed
# else:
#     code to be executed when loop finishes normally
# write a python program to print the content of list using for loop with else clause
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
else:
    print("Loop finished normally")

# Break statement
# The break statement is used to terminate the loop prematurely
# The syntax of break statement is as follows:
# break
# write a python program to print the content of list using for loop with break statement
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    if fruit == 'banana':
        break
    print(fruit)
else :
    print("Loop finished normally") 
'''here else clause will not execute because we use break statement which terminate the loop prematurely
so else clause will not execute in this case, else clause will execute only when loop finishes normally
'''

# continue statement
print("continue statement")
# The continue statement is used to skip the current iteration and move to the next iteration
# The syntax of continue statement is as follows:
# continue
# write a python program to print the content of list using for loop with continue statement
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    if fruit == 'banana':
        continue # here it will not print banana beacuse we use continue statement which skip the current iteration
    print(fruit)
'''here continue statement will skip the current iteration and move to the next iteration'''

# pass statement
# The pass statement is a null operation in python  — when it is executed, nothing happens
# It is a placeholder when a statement is required syntactically but no execution of code is necessary
# The syntax of pass statement is as follows:

# write a python program to print the content of list using for loop with pass statement
fruits = ['apple', 'banana', 'cherry']
print("Pass Statement")
for fruit in fruits:
    if fruit == 'banana':
        pass # here it will not print anything because we use pass statement which is a null operation
print(fruit)  # this will execute the last value stored in this var
