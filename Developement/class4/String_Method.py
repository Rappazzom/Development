#String methods

# Capitalize

animal = 'dog'
print(animal.capitalize()) #capitlizes First letter in a string

# Count
vehicle = 'toyota'
print(vehicle.count('t')) # counts number of lower case t's in a string

#casefold
animal = 'Dog'
print(animal.casefold()) # lowercases the string
# center
string = 'Michael'
print(string.center(22))  # uses intergers to measure the distance you center your word

# find
name = 'Tommy_boy'
print(name.find('m'))  # Finds how many m's you have in the string
#find = only to string
#index = tuples, intergers strings
burger = 'Boston_Burger'
print(burger.index('Burger')) # Gives you the index position where the string starts. 

# Expandtabs
name = 'Jimmy\tJohns'
print(name.expandtabs(15)) # inserts tab spacing in string

#isalnum
cheese = 'provolone'
print(cheese.isalnum()) # to see is its alhpanumerical

result = '@#%^#@' # Is false
print(result.isalnum())

#isalpha
meat = 'steak'
print(meat.isalpha()) # Is alphabetical
 result = '123432'
print(result.isalpha())

#isdecimal
plane = 'helicopter2'
print(plane.isdecimal()) # checks for all integers False
code ='3' # This returns True
print(code.isdecimal())

#isdigit
result = '12345'
print(result.isdigit()) # True is all digits

#islower
result = ' alllower'
print(result.islower()) # Is True

#isupper
result = ' ALLUPPER'
print(result.isupper()) # Is True

#isnumeric
result = '12345'
print(result.isnumeric()) # Checks for numbers

#isspace
result = '   '
print(result.isspace()) #checks to see if is just a space

#istitle
result = 'Welcome to Intro to Programming'
print(result.istitle()) # Every word haws to start with capital letter

#Join
our_class = ['Sam', 'Judith', 'Robin'] # This is out list
result = ', '.join(our_class)  # join our list  together with our seperator
print(result) # Prints a string

#lower
string = 'HELLO world'
print(string.lower()) #Turns capital letters lowercased
#partition
my_day = ' I had a pretty good day today' #This is a string
result = my_day.partition('pretty') # Breaks at the part you choose, I chose pretty
print(result) # Prints a list
#replace
string = 'Wassaaabi my brothah'
result =  string.replace('brothah', 'Brother') # Chooses a word and replaces it
print(result)

dog_name = 'fido'
result = dog_name.replace('o', 'b')# replace charecters 
print(result)

product_key = 'abc123kb'
result = product_key[3:6] #Slicing
print(result)

result = product_key[0:6:2] # slices every other index in string
print(result) 

#split
string = 'I hope your day is well'
result = string.split('your')
print(result)

my_string = ' today is monday'
result = my_string.split() #splits at break()
print(result)

#splitlines
string = ' I hope you had a good day'
result = string.splitlines('you')
print(result)

string = 'Hello, everyone. \nHope the week is going by quickly.\n Tomorrow is Tuesday'
result = string.splitlines() # Breaks a line at every \n
print(result)

#startswith
country = 'America'
result = country.startswith('B') # Its false because it doesn't start with B
print(result)

#strip
string = '      Tuesday     '
print(string.strip())

x = 'hello'
print(x)
str2 = 'HELLO'.lower()
print(str2)
print(x == str2) # True value is the same
print( x is str2) # False both strings are written differently
print(id(x))
print(id(str2)) # shows where they are located




