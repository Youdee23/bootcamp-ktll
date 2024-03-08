"""
# Question 1
-------------------------------------------------------
Create a variable for the string 'Python is Fun!' and
write the commands that will return the following
- 'ytho'
- 'Pytho'
- 'ython is Fun!'
- 'Python is Fun!'
- 'yhni u'
- 'yoiF'
- 'Pto sFn'
"""

"""
# Question 2
-------------------------------------------------------
Create 3 variables to store 
- 'hello'
- ','
- 'world'
and a fourth variable that will be a concatenation of 
the first and third variable.
Write a command that will give the following output
- 'ello'
- 'elloworl'
- 'elwr'
- 'dlrowolleh'
"""
statement = 'Python is Fun!'
print(statement[1:5:1])
print(statement[0:5:1])
print(statement[1:])
print(statement[:])
print(statement[1:12:2])
print(statement[1:11:3])
print(statement[0:13:2])
WordOne = 'hello'
WordTwo = ','
WordThree =  'world'
salutation = WordOne + WordThree
print(salutation)
print(salutation[1:5:1])
print(salutation[1:9:1])
print(salutation[1:8:2])
print(salutation[-1:-11:-1])