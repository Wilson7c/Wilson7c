#Searching

file = open('resources/super_villains.txt', 'r') # open to read
print(file)

for line in file:
    print(line)

file.close()

# .strip() method removes the extra characters at end of text
print("      Hello" .strip())
print("world\n".strip())
print("!")

# 'w' opens to write and overwrites the file
file = open('resources/super_villains.txt', "w")
file.write('Lee the Merciless')
file.write('Rohan the Destroyer')
file.close()

file = open('resources/heros.txt', 'w')
file.write('Owen the valiant\n')
file.close()

# Better way to open and close a file
# file automatically closes after execution of with
with open('resources/super_villains.txt') as f:
    for line in f:
        print(line.strip())

with open('resources/super_villains.txt') as f:
    read_data = f.read()

print("\n\nRead Method")
print(read_data)

# Reading data into an array (list)

with open('resources/super_villains.txt', 'r') as f:
    villains = [x.strip() for x in f]

print(villains)

# Linear Search
key = "Vidar the Manic".upper()

i = 0
while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < len(villains):
    print("Found it at position", i)
else:
    print(key, "is not in the list")

# try to make this into a function

def linear_search(key, list):
    """

    :param key: what you are looking for
    :param list: where are you looking
    :return: bool did you find it?
    """








