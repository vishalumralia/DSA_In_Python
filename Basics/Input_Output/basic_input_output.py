print('Hello')
# Output: Hello

# print(object= separator= end= file= flush=)

print('Good Morning!')
print('Welcome')
# Good Morning!
# Welcome


print('Good Morning!', end=' ')
print('Welcome')
# Good Morning! Welcome

print("New Year", "2025", sep='. ')
# New Year. 2025

number = 123
name = "abc"

# print literals     
print(5)

# print variables
print(number)
print(name)

# 5
# 123
# abc

print('Hello ' + 'Welcome.')
# Hello Welcome.

x = 1
y = 2
print('The value of x is {} and y is {}'.format(x,y))
# The value of x is 1 and y is 2

# using input() to take user input
name = input('Enter a name: ')
print('You Entered:', name)
print('Data type of num:', type(name))

# Enter a name: abc
# You Entered: abc
# Data type of num: <class 'str'>

# To convert user input into a number we can use int() or float() functions as:
num = int(input('Enter a number: '))