# user_input = input('Pick a word: ') # The word is Computer and pull out the and answer it as how many vowels you have
# print(user_input.lower())
# result = user_input.lower()
# e_count = result.count('e')
# o_count = result.count('o')
# u_count = result.count('u')
# a_count = result.count('a')
# i_count = result.count('i')
# final_result = e_count + o_count + u_count + a_count + i_count
# print(final_result)

# remove_a = result.replace('a','')
# remove_e = result.replace('e','')
# remove_o = result.replace('i','')
# remove_a = result.replace('o','')
# remove_i = result.replace('u','')
# remove_u 
# print(remove_vowels)

# def remove_vowels_and_count(word): # Defines what your action
#     vowels = 'aeiouAEIOU' # attaches the vowels
#     count = 0 # current vowel count set to 0
#     non_vowels = ''   # defines my non vowel string starting with nothing in it yet
#     for char in word:   # for letters that are in the word user picks
#         if char in vowels: # if the charecter is a vowel add 1 to your count
#             count += 1
#         else:
#             non_vowels += char # for charecters that are not your vowel add them to your string
#     return non_vowels, count # return the string without vowels and the number of vowels removed from string
# word = input("Enter your word here: ") # User writes in a wor
# result, count = remove_vowels_and_count(word) # defines your action with results of removing vowels as well as your final vowel count

# print('number of vowels', count) # Prints string + count
# print('Here is your new string', result) # prints string + result after removing vowels

# Write some code that will print a box around a a string   ******** \n ** (word) ** \n ******** 
# Words used hello and Programming is fun

# word = input("please write your word here: ")
# print('**********')
# print(f"***([word])***")
# print('**********')


word = input("please write your word here: ") # user enters word
top = "***************"   # defines top decorations
middle = (f"****({word})****") # defines middle decoration and word
bottom = ('***************') # defines bottom decorations
print(top.center(150))
print(middle.center(150))
print(bottom.center(150))



  