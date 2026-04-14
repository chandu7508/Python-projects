name = input('What is your name ? ').capitalize()
fav_color = input('What is your favorite color ? ').lower()
name_last_letter_index = len(name)-1
if name[name_last_letter_index] != 's':
    print(name + "'s favorite color is " + fav_color)
else:
    print(name + "' favorite color is " + fav_color)


"""
Topics Learnt: variables, arithmetic & assignment operators, 
strings(functions, indexing, manipulation), input() function
"""