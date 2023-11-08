'''
9. Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.
'''



'''
REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.
'''

# initializations
total = 0 
new_string = ''

while True:
    user_string = input("please enter data:")
    if len(user_string) == 0:
        print("String is enter, lets break the loop")
        break
    elif user_string.isalpha():
        new_string += user_string
        print("String is a set of letters, lets concatenate the string")
        print(new_string)
        continue
    elif not user_string.isalnum():
        print("looks like a special charecter, lets continue")
        continue
    elif user_string.isnumeric():
        new_val = float(user_string)
        total += new_val
        print(total)
        print("we are a number")