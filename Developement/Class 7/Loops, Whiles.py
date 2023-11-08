import math
# result = (2+5) * 6
# print(result)
# answer = 5+4*3
# print(answer)
# birth_year = 1990
# current_year = 2023
# age_in_a_decade = (current_year - birth_year) + 10
# print(age_in_a_decade)

# circumference_of_a_circle = 2 * math.pi * 3
# print(circumference_of_a_circle)

# test_1 = 95
# test_2 = 82
# test_3 = 90

# # test_average = (test_1 + test_2 + test_3)/3
# # print(f'Congrats your average test score {test_average}')

# dog_name = 'fido'
# print(type(dog_name))

# age = 27
# print(type(age))

# temp_is_hot = True
# print(type(temp_is_hot))

# average_weight = 165.54
# print(type(average_weight))

# last_name = 'jenkins'
# print(type(last_name))

# phrase = 'I love coding'
# print(type(phrase))

# scores = [75, 45, 23, 99]
# print(type(scores))

# values = { }

# num_one = 6
# num_one -= 3 ==  num_one - 3
# print(num_one)

# num_two = 10
# num_two += 2
# print(num_two)

# num_three = 12
# num_three /= 2.5
# print(num_three)

# num_four = 3
# num_four += 12
# print(num_four)

# num_five = 8
# num_five *= 2
# print(num_five)

# esult = 5 < 7
# print(f' is 5 less than 7', {result})

# result = (16/2) == 8
# print(f' is 16/2 = 8 {result}')

# result = 12 > 19
# print(f' is 12 greater then 19 {result}')

# ice_cream_tasty = True
# print(not ice_cream_tasty)

# food = 'spaghetti'
# print('g' in food)
# print('z' in food)

# print('dog' == 'cat')

# fname = 'mike'
# lname = 'Rap'
# full_name = fname + ' ' + lname
# print(full_name)

# day = 'saturday '
# month = day * 4
# print(month)

# my_food = len('peanut butter')
# print(f'The length of my string is {my_food}')

# food = 'coffee'
# print(len(food))

# word = 'hello'
# result = word.capitalize()
# print(result)

# furniture = 'chair'
# seat = furniture.upper()
# print(furniture)

# word = 'amazing'
# result = word.isupper() # checks if word is upper case
# print(result)

# day = 'wed'
# result = day.find('d')
# print(result)

# title = 'welcome to earth'
# result = title.istitle()
# print(result) # false because letters that start words are snake case

# sport = 'baseball'
# result = sport.count('b')
# print(result)

# word = 'grapes'
# result = word.find('g') # g is at the index 0
# print(result)

# word = 'crayon'
# result = word.index('y')
# print(result)

# age = (input('What is your age? '))
# age = int(age)
# print(type(age))

# user_input = input("What is your name? ")
# user_input2 = input("What is your last name?")
# print(f'Your name is {user_input} {user_input2}')

# num_one = int(input("what is your first number?"))
# num_two = int(input("what is your second number?"))
# product = num_one * num_two
# print(f'The product of {num_one} and {num_two} is {product}')

# food = 'burger'
# food1 = [0:4]
# print(food1)


# furniture = 'couch'

# stop = len(furniture)
# print(stop)
# start = stop - 3
# furniture = furniture[-3:]
# print(start)
# result = furniture[start:stop]
# print(result)

# dessert = 'apple pie'
# woah = dessert[0::2]
# print(woah)

# game = 'dodgeball'
# taco = game[::-1]
# print(taco)

# print(1,2,3,4,5, sep="*") # replaces space with *

# print("lets", end= " ")
# print("party")

# myname = "Mike"

# if myname == "Mike":
#     print(f'Hello {myname}')

# current_year = 2022

# if (current_year % 2) == 1:
#     print(f'{current_year} is an odd number')
# else:
#     print(f'{current_year} is an even  year')


# good_weather = True

# if good_weather == True:
#     print("No jacket needed")
# else:
#     print("Better bring an umbrella")

# gas_tank = 30
# if gas_tank <= 30:
#     print("Get Gas")
# else:
#     print("No gas needed")

# counter = 0

# while counter <= 5: # Our condition
    
#     print("Happy Halloween", counter) # prints halloween until counter = 5
#     counter += 1 # adds 1 to variable counter 

# counter = 1
# while counter <=10:
#     print(counter)
#     counter += 1

day_of_the_week = input("What day is it today? ")
while day_of_the_week == '':
    print("You have to tell me the day")
    day_of_the_week = input("What day is today? ")

print(f'Happy {day_of_the_week}')