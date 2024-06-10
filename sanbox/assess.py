import string
"""
# CLASSWORK
------------------------------------------------------------
Create a list of names of 8 books. Then create another list
that only holds the books that have names shorter than 8.
"""
books =['Ephesians', 'Genesis', 'Mark', 'Acts', 'Zephaniah', 'Exodus', 'Leviticus', 'John']
# Using for loop
new_list = []
for book in books:
    if len(book) < 8:
        new_list.append(book)
print(new_list)

new_list =[book for book in books if len(book) < 8]
print(new_list)

"""
# Question #1
-----------------------------------------------------------------
Write a function that asks a user for his first name and then his 
last name and print last name before first name.
------------------------------------------------------------------
"""


# Solution
# def ask_name():
    # first_name = input('What is your first name: ')
    # last_name = input('What is your last name: ')
    # return last_name, first_name


#print(ask_name())

"""
Question #2
-----------------------------------------------------------------
# A function with no return value
-----------------------------------------------------------------
A function that does not return any value.
This function will return None - A special data type in Python 
used to indicate that things are empty or that they returned 
nothing.

# Wirte a function that takes your name and PRINTS "Welcome John". 
If your name is "John" for example.
-------------------------------------------------------------------
"""


# Solution
def take_name(name):
    return f'Welcome {name}'


print(take_name('Youdee'))


"""
Question #3
------------------------------------------------------------------
The principle of code reuse achived with functions. Functions helps
in reducing code repeatation.
------------------------------------------------------------------
# Convert the following code into a function called `lucky_number`.
# The function will take only one argument, `name`.
name = "Keme"
number = len(name) * 7
print("Hello " + name + ". Your lucky number is " + str(number))
"""


# Solution
def lucky_number(name):
    number = str(len(name) * 7)
    return f'Hello {name}. Your lucky number is {number}'


print(lucky_number('Keme'))

"""
Question #4
------------------------------------------------------------------
Identify the repeated pattern in the code below and replace it with
a function called month_days, that receives the name of the month 
and the number of days in that month as arguments.
june_days = 30
print("June has " + str(june_days) + " days.")
"""


# Solution
def month_days(month_name, days_of_month):
    return f'{month_name} has {str(days_of_month)} days'


print(month_days('June', 30))

"""
Question #1
----------------------------------------------------------------------
Research 10 methods used with list object operations and show at least
two examples of each of the methods.
"""

"""
Question #2
----------------------------------------------------------------------
Using the list ['Alice', 'was', 'not', 'a', 'bit', 'hurt'], construct the
following lists:
(a) ['not', 'a', 'bit', 'hurt']
(b) ['Alice', 'was', 'hurt']
(c) ['Alice', 'hurt', 'a', 'bit']
(d) ['a', 'bit', 'hurt', 'Alice', 'not']
"""
# Solution
phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [2, 3, 4, 5]
n_list = [phrases[i] for i in order]
print(n_list)

phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [0, 1, 5]
n_list = [phrases[i] for i in order]
print(n_list)

phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [0, 5, 3, 4]
n_list = [phrases[i] for i in order]
print(n_list)

phrases = ['Alice', 'was', 'not', 'a', 'bit', 'hurt']
order = [3, 4, 5, 0, 2]
n_list = [phrases[i] for i in order]
print(n_list)

"""
Question #3
------------------------------------------------------------------------
Use only pop and append functions to turn the list ['many', 'a', 'strange', 'tale']
into ['many', 'a', 'tale']
"""

# Solution
word_list = ['many', 'a', 'strange', 'tale']
word_list.pop(2)
print(word_list)

"""
Question #4
------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers from 1 to 100
with 100 inclusive.
"""

# Solution
even_list = [num for num in range(1, 101) if num % 2 == 0]
print(even_list)

"""
# Question #5
-------------------------------------------------------------------------
Using list comprehension, create a list of only even numbers raised to the
second power.
"""

# Solution
even_numbers = [num ** 2 for num in range(0, 101) if num % 2 == 0]
print(even_list)

"""
Question #6
-------------------------------------------------------------------------
Using list comprehension, create a list of only vowel letters from the list
of all the letters A-Z.
"""
# Solution
alphabets = string.ascii_uppercase
print(alphabets)
vowels = ['A', 'E', 'I', 'O', 'U']
V = [alph for alph in alphabets if alph in vowels]
print(V)