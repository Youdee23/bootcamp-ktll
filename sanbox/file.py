try:
    pointer = open('hello.txt')
    pointer.write('Please create the file and add this file for me')
except FileNotFoundError:
    pass

print('Can you please print me?')





