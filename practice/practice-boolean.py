color = input("What is your name? ")
print(color)

# elif allows you write multiple ifs which enables you to test for more conditions
if color == 'Yellow':
    print("I have been expecting you", color)
elif color == 'Blue':
    print("Where have you been", color, "my friend")
elif color == "Red":
    print("You have been so far away", color)
else:
    print("I have no colors left")

# PRACTICE

food = input('What is your favourite dish? ')
print(food)
if food == 'ekpang_nkukwo':
    print('I can\'t get enough of you,', food)
elif food == 'fried_rice':
    print('What a mind blowing meal you are', food)
elif food == 'moi_moi':
    print('Ah go chop you tire today', food)
elif food == 'beans':
    print('I could eat you everyday', food)
else:
    print('I won\'t eat any other dish')

'''
# I have to practice this repeatedly so that I can master it.
# It seems strange looking at it at first.
'''
clothing = input('What is your favourite outfit? ')
print(clothing)
if clothing == 'skirt':
    print(f'I love my {clothing} short')
elif clothing == 'shorts':
    print('I love to show off my legs in {clothing}.')
elif clothing == 'blouse':
    print('You\'re not really my cup of tea')
elif clothing == 'shirt':
    print(f'I only wear a {clothing} for work')
else:
    print('I can\'t go wrong in a gown')