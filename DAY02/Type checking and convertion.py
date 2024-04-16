'''
Type Error, Type Checking and Type Conversion

New concept learned if you use the type() check function you know what kind of  data is


Type convertion or type casting this turns a data type to another like using a str()
'''

import string


num_char=len(input("what is your name?"))

#print(type(num_char))

new_num_char= str(num_char)

print("Your name has "+ new_num_char+" characters")