# You’re working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.

# ●Create two variables called username and password and set them to any valid string values.
# ●Prompt the user to enter their username and password using the input()function.
# ●Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
# ●If they match, print “Login successful.” If they don’t, print “Incorrect username or password.”


# username = 'cheese'
# password = 'fries'

# user_input1 = input("What is your username?: ")
# if user_input1 != username: # if you enter the wrong username it prints wrong username
#     print("You entered wrong username")
# user_input2 = input("What is your password?: ")
# if user_input2 != password: #if you print wrong password it tells you wrong password
#     print("You entered incorrect password")
# elif user_input1 == username and user_input2 == password: # If you entered both correctly it 
#     print("Logging in now")




username = 'cheese'
password = 'fries'

user_input1 = input("What is your username?: ")
if user_input1 != username: # if you enter the wrong username it prints wrong username
    print("You entered wrong username try again")
elif user_input1 == username: # If the input is equal to username move on to next input for password
    user_input2 = input("What is your password?: ")
    if user_input2 != password: #if you print wrong password it tells you wrong password
        print("You entered incorrect password start over")
    elif user_input1 == username and user_input2 == password: # If you entered both correctly it will log you in
        print("Login successful")