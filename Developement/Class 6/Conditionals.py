# code in if runs  
# x = 20
# y = 15
# if x > y:
#     print(x)  # prints x because x is greater then y

# code in if does not run
# x = 20
# y = 20
# if x > y:
#     print(x) # Code doesn't run because x is not greater then y

# find odd or even
# num = 7
# numx = (num % 2) # checks to see if the number is divisble by 2.
# if numx == 1: # if number is equal to 1 this number is off
#     print(f'This number is odd')
# else: # if its divisble by 2 and returns 0 the number is even
#     print(f'This number is even')

# user = 7
# if (user % 2) == 1:
#     print('This is odd')

# x = 40
# y = 40
# if x > y:
#     print('x is bigger') # in case x is bigger
# elif y > x:
#     print('y is bigger') # incase y is bigger
# elif x == y:
#     print('x and y are the same') # in case x is equal to y

# ternary Operators

# x = 40
# y = 30

# result = "x is bigger" if x > y else "y is bigger then x" if y > x else "They are the same"
# print(result)


# user_input = 9.2
# if (user_input % 2) == 1: # remainder of 1 means it is odd
#     print('The number', (user_input), 'is odd')
# elif (user_input % 2) == 0: # remainder of 0 is even
#     print('The number', (user_input), 'is even')
# else: # this is unknown
#     print('The number', (user_input), 'is unknown')
# try:
#     user_input = int(input("what is your number?: "))
#     if (user_input % 2) == 1: # remainder of 1 means it is odd
#         print('The number', (user_input), 'is odd')
#     elif (user_input % 2) == 0: # remainder of 0 is even
#         print('The number', (user_input), 'is even')
#     else:
#         print('Unknown')
# except ValueError:
#      print('input a whole number')
# user_input = (input('what is your number?:'))
# if '.' in user_input:
#     print("unknown")
# elif (int(user_input) % 2) != 0: # remainder of 1 means it is odd
#      print('The number', (user_input), 'is odd')
# elif (int(user_input) % 2) == 0: # remainder of 0 is even
#      print('The number', (user_input), 'is even')

# user_input = input("please input something here: ")
# print(type(user_input))
# if user_input.isdigit():
#     print("This is a number")
# elif user_input.isalpha():
#     print("This is a string")
# else:
#     print("This is something else")

# Our Temp
# temp_f = 75

# if temp_f > 70:
#     print("Its hot outside")
# elif temp_f > 40:
#     print("It's moderate outside")
# else:
#     print("It's cold outside!!")

# temp_f = 75

# if temp_f > 70:
#     print("Its hot outside")
# if temp_f > 40:
#     print("It's moderate outside")
# if temp_f <= 40:
#     print("It's cold outside!!")


# temp_f = 75

# if temp_f > 70:
#     print("Its hot outside")
# elif temp_f > 40 and temp_f <= 70:
#     print("It's moderate outside")
# else:
#     print("It's cold outside!!")

# me = 'I Exist'
# if me:
#     print('I Exist')


# not > and > or

# print(True or False and False) # and gets evaluated first
# print((True or False) and False) # parentheses take precedence

# x = True

# print(not x)

# num = 5

# if num % 2 == 1:
#     if num < 10:
#         if num > 0:
#             print("This is a single digit odd number")

# num = 5
# if num % 2 == 1 and num < 10 and num > 0:
#     print("This is a single digit odd number.")

# num = 6
# if num % 2 == 0 and num < 10 and num > 0:
#     print("This is a single digit even number")


username_input = input("username: ")
password_input = input("Password: ")


username = 'admin'
password = 'password'

if username_input == username and password_input == password:
    print("login is Successful")
else:
    print("Incorrect username and password")

