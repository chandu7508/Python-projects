"""name = input('What is your name ? ').capitalize()
fav_color = input('What is your favorite color ? ').lower()
name_last_letter_index = len(name)-1
if name[name_last_letter_index] != 's':
    print(name + "'s favorite color is " + fav_color)
else:
    print(name + "' favorite color is " + fav_color)"""

# Positional Arguments

def _function(c1,c2,c3):
    print("a is: ",c1)
    print("b is: ",c2)
    print("c is: ",c3)

a = 1
b = 2
c = 3

_function(c2 = b,c1 = a,c3 = c)