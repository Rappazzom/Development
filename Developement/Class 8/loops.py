'''
Loops
1. While loops - Run as long as a given condition is true
2. Example - Create a while loop that prints every integer from 1 to 10
3. Create a while loop that will keep asking a user for their user id, until they type 'stop'.
4. Improved login system - Rewrite the username and login program. If the user enters the
incorrect username or login, they will keep receiving a prompt.
5. For Loops - Iterate through strings, lists, tuples, dictionaries, sets....
'for item in collection'
6. Write a loop that loops through a string, counts all the letters, and then print how long the
string is.
7. Take a string from the user, verify that it's a number. Write a loop that adds all the digits
together, then print the total.
8. Adding conditionals to loops - Write some code that will loop through a string and print
whether each letter is a vowel or a consonant.
9. You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.

'''

'''
1. While loops - Run as long as a given condition is true
2. Example - Create a while loop that prints every integer from 1 to 10
'''
# i = 1 # Iinitilization

# while i <= 10:
#     print(i) # Output
#     i += 1 # increment by 1

# print("I am out of the loop") # We are out the loop 
'''
3. Create a while loop that will keep asking a user for their user id, until they type 'stop'.
'''

# prompt the user
# user_id = input("User Id: ") #If I type stop I jump to line 44

# while user_id != "stop": # while the user id is anything but "stop" it will continue asking for user id.
#     user_id = input("User Id: ") #if you enter stop here 
#     print("This is where we are")

# print("Have a nice day") # This is outside the loop


'''
4. Improved login system - Rewrite the username and login program. If the user enters the
incorrect username or login, they will keep receiving a prompt.
'''

# System Id and Password
# sys_id = 'admin'
# sys_password = 'pass'

# user_id = input("user_id: ")
# user_password = input("Password: ")

# while sys_id != user_id and sys_password != user_password:
#     print("incorrect User ID or Password")

#     user_id = input("user_id: ")
#     user_password = input("Password: ")
    
# print("Login successful!")


'''
5. For Loops - Iterate through strings, lists, tuples, dictionaries, sets....
'for item in collection'
'''

# my_string = "Hello World"
# for item in my_string: # for item in collection
#     print(item, end=' ')

'''
Lets loop through the string "Hello World"

'''



'''
Lets loop through a list of colors
# my_colors = ['red', 'green', 'orange', 'yellow']
'''
# my_colors = ['red', 'green', 'orange', 'yellow']
# for i in my_colors:
#     print(i, end= ' ')

'''Lets loop through a tuple
my_fav_food = ('pizza', 'subs', 'chicken')
'''
# my_fav_food = ('pizza', 'subs', 'chicken')
# for food in my_fav_food:
#     print(food, end= '*')

# ranges   range(start, stop, step)
# for i in range(15):
#     print(i)

# for i in range(5,26):
#     print(i)

# for i in range(0,25,5):
#     print(i)
'''
6. Write a for loop that loops through a string, counts all the letters, and then print how long
the string is.
'''
# current_feeling = 'onward and upward'
# i = 0
# for char in current_feeling:
#     if char.isalpha:
#         i += 1
#     print(i)

# current_feeling = 'onward and upward'
# i = 0
# for c in current_feeling:
#     i += 1
# print(i)

'''
7. Take a string from the user, verify that it's a number. Write a loop that adds all the digits
together, then print the total.
'''
# test_string = '14253'

# total = 0

# for t in test_string: # we need to test to make sure its a number
#     if t.isalnum(): # our test
#         t = int(t) # cast in integer
#         total += t
# print(total)


'''
8. Adding conditionals to loops - Write some code that will loop through a string and print
whether each letter is a vowel or a consonant.
'''

# my_string = 'Hello Class'
# v_count = 0
# c_count = 0
# vowel = "aeiou"
# for i in my_string:
#     if i in vowel:
#         v_count += 1
#     else:
#         c_count += 1
# print(f'Total vowels is:',v_count)
# print(f'Total consonant is:',c_count)

# list reference
# my_vowel_list = ['a','e','i','o','u']
# my_vowel_tuple = ('a','e','i','o','u')
# my_vowel_string = 'aeiou'

# my_string = 'hello'

# for letter in my_string:
#     if letter in my_vowel_list:
#         print(letter, "is a vowel")
#     else:
#         print(letter, "is a consonant")



'''
9. You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''

user_input = input("Enter a text here?: ") # user enters phrase

test_string = user_input # links userinput to be able to test
test_string.strip() # cleans string
new_string = '' # this will be our new string
for i in test_string: 
    if i.isalpha(): # checks for anything that isn't a letter
        new_string += i # if its a letter add it to new_string
print(new_string)
        


