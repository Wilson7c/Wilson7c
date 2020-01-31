# LISTS

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [5, 9, 12, 6, -3, 4]


# using indices
print(my_list[1])  # Bev
print(my_list[-1])  # Gus
print(my_list[1:4])  # Abe to Dan
print(my_list[-3:])  # Eve to Gus

my_copy = my_list # does not create a cope, just another line to the original
my_copy.append("Hal")
print(my_copy)
print(my_list)

my_copy = my_list[:]
my_copy.append("Ida")
print(my_copy)
print(my_list)

# 2d lists
my_2d = [["Abe", 0], ["Bev", 7], ["Cam", 4]]
print(my_2d[1][0])
my_2d[2].append("Wilson")
print(my_2d)


# If in
if "Abe" in my_list:
    print("Abe is there")

if "abe" in my_list:
    print("abe is there")

import random
if random.randrange(10) in [3, 5, 6, 8, 9]:
    print("yay!")

# List Functions

print(len(my_list))  # returns the length of a list
print(min(my_numlist))
print(max(my_numlist))
print(max(my_list))  # Highest Alphabet
print(sum(my_numlist))  # Sums list

print(my_list.index("Cam"))  # returns the index of the found object
my_list.append("Cam")
print(my_list.index("Cam"))
print(my_list.count("Cam"))
print(my_list.count("Abe"))

my_list.append("Deb")
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

# Manipulating

my_list.pop()  # pops one off the end of the list
print(my_list)
my_person = my_list.pop()  # returns the popped item
print(my_person)
print(my_list)
front_of_line = my_list.pop(0)
print(front_of_line)
print(my_list)

del my_list[1]
print(my_list)

first = "Francis"
last = "Parker"
print(first, last)
print(first + last)

print(my_list + my_numlist)


#  Iterating through a list
#  For each loop  [works with a copy]
for name in my_list:
    print(name)

#   Index Variable Loop
for i in range(len(my_list)):
    my_list[i] = my_list[i].upper()
    print(my_list[i])

print(my_list)

# List Comprehensions



# Make a list from 50-200

my_list = []

for i in range(50,101):
    my_list.append(i)

print(my_list)


my_list = [x for x in range(50, 101)]
print(my_list)

# make a list of powers of 2 from 0 to 100

my_list = []

for i in range(101):
    my_list.append(2 ** i)

print(my_list)

my_list = [2 ** x for x in range(51)]


# same list, but filter out any results greater than 100,000
my_list = []

for i in range(51):
    if 2 ** i < 100000:
        my_list.append(2 ** i)

print(my_list)

my_list = [2 ** x for x in range(51) if 2 ** x < 100000]
print(my_list)


# Roll a single die 100 times
roll = random.randrange(1, 7)


my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)

# roll two die 100 times and add it to a list (ex: [1, 6])
roll = random.randrange(1, 7)

my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_list)

# filter out so we only show doubles

roll = random.randrange(1, 7)

my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_list)



my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)

# all at once create a list of two die rolls, filter out the doubles
my_doubles = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] == x[1]]  #  generates two die rolls filter out the doubles
print(my_doubles)

# Working with strings is similar to the list
first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first)
print(first + last)
print(last[-3:])

for letter in first:
    print(letter)




