n = 0
while n != 105:
    print(n)
    n += 5


string = "She sells seashells by the seashore"
count_s = 0
count_S = 0
index = 0
while index < len(string):
    n = string[index]
    if n == 's':
            count_s += 1
    elif n == 'S':
            count_S += 1
    index += 1

total_s = count_s + count_S
print(f'There are {count_s} lower case s, there are {count_S} of capital S, while the total number of S is {total_s}')
