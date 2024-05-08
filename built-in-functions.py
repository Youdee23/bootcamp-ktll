"""
You want to ask a user for a name.
Change the name to upper case letters.
Add a greeting to the name.
And then ask the person, if he wants to continue.
"""
# name = input('Type your name here: ')
# name = name.upper()
# "Hello " + name
# "Do you want to continue?"

def greetings():
    name = input('Type your name here: ')
    name = name.upper()
    print("Hello " + name)
    print("Do you want to continue?")

# greetings()
# greetings()

def age_check(age, name):
    if age < 18:
        return "Hello "  + name + " you are qualified!"
        print("Done")
    else:
        return "Hello " + name + " your are unqualified!"

# result = age_check(15, 'ima')
# result = age_check(name='ima', age=15)
# print(result)

def var_number_of_argument_function(*args):
    for arg in args:
        print(arg)
    return "Done"

res = var_number_of_argument_function('wilson', 89, 'js1', 'male')
print(res)

"""
# parameters - are defined when you are creating the function
# arguments - are the values you provide when you are calling the function
# *args - this is when you would want your function to accepts any number of positional arguments
# **kwargs - this is when you want your function to accept any number of keyword arguments
"""

"""
# LAMBDA FUNCTION
The lambda function is used to write anonymous functions in python program.
When you have a need to use a function but you don't want to first of all
define the function before using it, you may need to write a lambda function.
A lambda function cannot be used in more than one place.
Using the lambda function is a quick way of writing functions on the fly.
"""
def raise_to_power_2(number):
    return number ** 2

ret = raise_to_power_2(4)
print(type(ret))

rest = lambda number: number ** 2
print(type(rest))
print(rest(4))

multilpy = lambda x, y: x*y
print(multilpy(7,1))

colors = ['red', 'white', 'blue', 'brown', 'black', 'cyan']
"""
Write a program that returns a list with the colors in upper case letters.
"""
def capital_letters(word):
    return word.upper()

print([color.upper() for color in colors])
print([capital_letters(color) for color in colors])

print([(lambda color: color.upper())(color) for color in colors])

magic_nums = [12, 6, 3, 16, 21, 5]
[(lambda num: num**2)(num) for num in magic_nums]

"""
# MAP FUNCTION
------------------------------------------------------------------
This is a built in function that takes two arguments, a function
and an iterable. It applies each element of an iterable to a function.
"""
# map(func, iterable)
reslt = map(lambda num: num**2, magic_nums)
print(type(reslt))
print(list(reslt))

col = list(map(str.upper, colors))
print(col)

"""
ZIP FUNCTION
-------------------------------------------------------------------
The zip function takes a number of a iterables and returns a tuple containing
each element of the iterables.
"""
# zip(*iterable)
# index = [1, 2, 3, 4, 5, 6]
zip_colors = list(zip(range(len(colors)), colors, range(6), [0,1,2,3,4,5]))
print(type(zip(colors)))
print(zip_colors)


[0,1,2,3,4,5]
['red', 'white', 'blue', 'brown', 'black', 'cyan']
[0,1,2,3,4,5]

"""
# ENUMERATE FUNCTION
---------------------------------------------------------------------
A built in function that takes an iterable and returns a tuple of
the index and each of the elements of the iterable.
"""
print(list(enumerate(colors)))
