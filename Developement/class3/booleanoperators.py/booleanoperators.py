# # Boolean Operators

# # Is 7 less than 5?

# print(7 < 5)

# # Is 4 less than or equal to 4?

# print(4 <= 4)

# # Is 6 greater than 2?

# print(6 > 2)

# # Is 5 greater than or equal to 6?

# print(5 >= 6)

# # Is 5 equal to 5?

# print(5 == 5)

# # and
# print(5 == 5 and 4 == 4)
# #Both variables must be true to be true
# print(5 == 5 and 4 == 3)
# #This is false because one is false
# print(5 == 3 and 4 == 3)
# #False because both are false

# # or
# print(5 == 5 or 5 == 3) # only 1 has to be true to be True
# x = 5
# y = 7
# #Is x less then y?

# #not
# print(not x < y)#not makes True turn to False

# # is
# print(4 is 4)
# x = ['apple', 'banana', 'cherry']
# y = x
# print( x is y)

# #This will be false
# x = ['apple', 'banana', 'cherry']
# y = ['apple', 'banana', 'cherry']
# print( x is y)

# # in 

# print('j' in 'Tanja') # True
# print('y' in 'Tanja') # False

# eval
is_hot = 'True'
is_wednesday = 'False'

eval(is_hot)
eval(is_wednesday)
