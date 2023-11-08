An email address is valid if:
    It has a "." at the third-to-last index +5
    It has exactly one "@" symbol, at the fifth-to-last index or earlier +5
    There is at least one character before the "@" symbol +5
    It doesn’t have any spaces (doesn’t contain " ") +5
    If all these conditions are met, print True. Otherwise, print False. +5

To do this, use boolean statements on your string. Test your code on a few inputs to make sure it works!


user_email = rappa@gmail.com  #users email to use for testing code below

user_input = input("Enter email address here: ") # user enters their email address

user_input.strip() # strips spaces before and after email address

test_1 = user_input[-4] == '.'  # user has '.' in the right location
print(test_1)

test_2 = ('@' in user_input[0:-5]) # asks user if @ is located between index 0 though -5
print(test_2)

test_3 = user_input.find('@') >= 1 # finds the '@' symbol and checks to see if its at index 1. If it is answer is true
print(test_3)

test_4 = user_input.count(' ') == 0 # counts the number of spaces in email address if there is 0 the answer is True
print(test_4)

result = (test_1 and test_2 and test_3 and test_4)
print(result)

