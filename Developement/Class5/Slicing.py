# my_fave_music = 'classical'
# backwards=my_fave_music[::-1] # Enters string backwards
# print(backwards)

# print(my_fave_music[1::-1])
# print(my_fave_music[2::-1]) 
# print(my_fave_music[3::-1])
# print(my_fave_music[4::-1])
# print(my_fave_music[5::-1])

# user_input = input("Please write a word here:  ") # user input
# length = int(len(user_input)) # length on input
# middle = int(length / 2) # splits word in half
# print(middle)

# first_half = user_input[:middle:]
# second_half = user_input[middle:]
# print("First half is", first_half)
# print("second half is", second_half)

# def second_half(word):
#     start_val = int((len(word) / 2))
#     stop_val = len(word)
#     print(word[start_val:stop_val])
# second_half('robin')
# second_half = input("what is your word: ")

# Start_val = int(len(second_half) / 2)
# print(start_val)
# stop_val = int(len(second_half))
# print(stop_val)
# print(second_half[start_val:stop_val])

# Get email address from the user
user_input = input("Please enter your email address: ")

# sanitize with .strip()
input = user_input.strip() # removes the spaces before and after input
# test 1 - '.' is third-to-last

test_1 = len(input) >= 3 and input[-4] == '.' # length of email is greater then 3 and fourth mark from end is '.'
print('Test 1 is',{test_1})

# test 2 - one '@' symbol at the fifth to last index or earlier
test_2 = len(input) >=5 and input[:-4] >= '@'  # length of email is greater then 5 and has @ at fifth from end or before
print('Test_2 is', {test_2})
# test 3 - At least one charecter before the '@'
split_email = input.split('@')  # splits email at the @ symobl

test_3 = len(split_email) >= 2 and len(split_email[0]) > 0  # email before @ symbol is 2 or more and its the space infront of @ isnt 0 
print('Test 3 is', {test_3})
# test_4 - No spaces within the string itself
test_4 = user_input.count(' ') == 0
print('Test 4 is', {test_4})
# test 5 - Confirm boolean statement that all tests pass or fail
print({test_1} and {test_2} and {test_3} and {test_4})



# user_email = 'Rappa@gm ail.com'

# user_email = input("what is your email?")  # user inputs email address

# user_email = user_email.strip()  # strips spaces before and after email

# test_1 = (user_email[-4] == '.') # Checks for dot before top level domain
# print("test 1: check for '.' before top level domain:", test_1)

# test_2 = ('@' in user_email[0:-5]) # checks if @ is located between index 0 to -5 index
# print("test 2: Check for one @ symbol before your '.' in top level domain:", test_2)

# stop_val = user_email.index('@') # index position of my @ symbol
# test_3 = (len(user_email[0:stop_val]) >=1) #checks if lenght before @ is greater then 1
# print("Test 3: At least 1 charecter before the @ symbol:", test_3)
# # test_3 = (user_email.find() >= 1)

# test_4 = user_email.count(' ') == 0 # counts the number of spaces. if they find 1 or more it fails
# print("Test 4: Checking to see if there's no space in your email:", test_4)
# final_result = (test_1 and test_2 and test_3 and test_4)
# print("Did your email pass all testing:", final_result)









