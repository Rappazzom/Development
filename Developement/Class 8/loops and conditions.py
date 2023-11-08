'''
Loops & Conditionals

1. What is the difference between a for and while loop?
2. Break keyword - Breaks out of the loop 
3. Write some code that takes in numbers from a user one at a time. This should keep going until
the user enters 0. Then print the sum of all the numbers.nIf the user inputs something that isn’t a
number, an error message should appear and the program should stop. (Hint: use break)
4. Continue - skips over the iteration
5. Exercise: Sum of Even Digits
Take a string as user input, and verify that it’s a number.
Loop through each digit of the number, and only add it to the sum if it’s even.
Print the sum of all the even digits at the end.
Make sure to use the continue keyword.
6. Break vs Continue
7. Pass
8. While-Else and For-Else
9. Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


'''

'''
1. What is the difference between a for and while loop? # for is for a codition, while is while a condition is met
'''
# for loop
# colors = ['red', 'green', 'blue']
# for c in colors:
#     print(c)

#while loop
# goal = 5
# num = 0
# while num <= goal:
#     print("Noth there yet", num)
#     num += 1


'''
Create a while loop that will prompt the user for the starting point and the ending point and
will count down from the user specified starting point to the user specified ending point, by 2.
'''
# starting_point = int(input("Pick a starting point?:"))
# ending_point = int(input("Pick a ending point"))

# start = int(starting_point)
# end = int(ending_point)
# num = start
# while start <= end:
#     print("We are going to finish in ", num)
#     num += 2
#     if start == end:
#         pass
#     else:
#         print("pick a starting number less then the ending number")

# while starting_point > ending_point:
#     starting_point -= 2
#     print(starting_point)


'''
Let's write a for loop that loops through our first name, output with one space between each letter
in the output
# '''
# first_name = 'mike'
# for f in first_name:
#     print(f, end=' ')


'''
2. Break keyword - Breaks out of the loop
'''
# userid = ""

# while userid != "stop":
#     userid = input("Enter something or hit stop: ")
# #     print(userid)

# while True: 
#     print("Hello World")
#     print("Hello World")
#     break
#     print("Hello World")

# Break
# userid = ""

# while True:
#     userid = input("Enter something or hit stop: ")
#     if userid == 'stop':
#         break
#     print(userid)

# userid = ""

# while userid != "stop":
#     userid = input("Enter something or hit stop: ")

#     for l in userid:
#         if l.isalpha():
#             print(l, end="")
#         else: 
#             break
#     print()

'''
Write a while loop that takes input from the user that will decrement by 3 and will break out
of the loop when  the number is even lets use a print statement to help show us where we break
the loop
'''
# num = int(input("Pick a number: "))

# while num != num % 2:
#     num -= 3
#     print(num)
#     if num % 2:
#         num -= 3
#         print("Your number is", num, "which is even")
#         break


'''
3. Write some code that takes in numbers from a user one at a time. This should keep going until
the
user enters 0. Then print the sum of all the numbers. If the user inputs something that isn’t a
number, an error message should appear and the program should stop. (Hint: use break)

Example (error):
5
7
c
Error: Not a number


Example (no error):
5
12
0
Sum: 17

Hint: "While True" is a looping construct in the Python programming language that allows a block of code
to be repeated indefinitely. It is often used in conjunction with a break statement, which allows
the loop to be exited under certain conditions.
'''
# num = int(input("Pick a number: "))
# count = 0 
# while num != '0':
#     for l in num:
#         if l.isdigit:
#             count += l
#             print()


# # Initializing
# total = 0

# # start my while loop
# while True:
#     user_input = input("Enter a number:    ")

# # if they enter a letteer
#     if not user_input.isnumeric(): # If user enters something that is NOT a number it BREAKS
#             print("Error: Not a number.")
#             break
# # if they enter a 0
#     elif user_input == '0': # if user enters 0 
#           print(f'sum: {total}')
#           break
#     else:
#           total += int(user_input)      
# # add to our total




'''
4. Continue - skips over the iteration
'''

'''
Use the continue keyword to loop through a string and only print the vowels.
'''
# vowels = 'aeiou'
# my_string = 'lets locate the vowels'

# for m in my_string:
#     if m in vowels:
#         print(m, end=",")
#     else:
#         continue

'''
Loop through the string 'The year really flew by' and only print the consonants
'''
# vowels = 'aeiou'
# my_string = 'The year really flew by'
# for m in my_string:
#     if m in vowels:
#         pass
#     else:
#         print(my_string)


'''
5. Exercise: Sum of Even Digits
Take a string as user input, and verify that it’s a number.
Loop through each digit of the number, and only add it to the sum if it’s even.
Print the sum of all the even digits at the end.
Make sure to use the continue keyword.

'''
# initiate
# total = 0
# user_input = input("Enter your number:  ")

# for n in user_input:
#     n = int(n)
#     if (n%2) == 1:
#         continue
#     else: 
#         total += n
# print(total)
# # verify its number
# total = 0

# while True:
#     user_input = input("Enter a number:  ")

#     for n in user_input:
#         if n.isnumeric():
#             continue
#         elif (n%2) == 1:
#             continue
#         else:
#             total += n
#             break
# print(total)
            
# loop through each digit and add if it

#print sum of all even digits

'''
6. Break vs Continue
'''
# vowels =  ['a', 'e','i','o','u']
# my_string = 'hello'

# for m in my_string:
#     if m in vowels:
#         continue
#     print(m)  

# vowels =  ['a', 'e','i','o','u']
# my_string = 'hello'

# for m in my_string:
#     if m in vowels:
#         break
#     print(m)  

# vowels =  ['a', 'e','i','o','u']
# my_string = 'hello'

# for m in my_string:
#     if m in vowels:
#         pass
#     print(m)  
'''
7. Pass
'''
# if 5 > 2:
#     pass
# else:
#     print("Testing")


# def add_two_nums(x,y):
#     pass
# print(add_two_nums(4,5))


'''
8. While-Else and For-Else
'''
# i = 6
# while i > 0:
#     print(i)
#     i-=1
#     if i == 4:
#         break
# else:
#     print('done')



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

'''
"While True" is a looping construct in the Python programming language that allows a block of code to be repeated indefinitely.
'''
user_input = input("Enter something here:  ")
total = 0
while True:

# If the string is empty, stop the loop.
    if len(user_input) == 0:
          break

# If the string is a number, convert it to a float and add it to a total.
    if user_input.isnumeric(): # If user enters something that is NOT a number it BREAKS
            total += int(user_input)
print(user_input)

# If the string is a set of letters, concatenate to the other letter strings passed in

# total = 0

# # start my while loop
# while True:
#     user_input = input("Enter a number:    ")

# # if they enter a letteer
#     if not user_input.isnumeric(): # If user enters something that is NOT a number it BREAKS
#             print(user_input+user_input)
#             break
# # if they enter a 0
#     elif user_input == '0': # if user enters 0 
#           print(f'sum: {total}')
#           break
#     else:
#           total += int(user_input)  