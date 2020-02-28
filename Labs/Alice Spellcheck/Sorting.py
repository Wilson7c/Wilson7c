# Sorting

# Swap Values

a = 1
b = 2

temp = a
a = b
b = temp

print(a, b)

# pythonic way

a, b = b, a

# make a random list of 100 number with values of 1 to 99
# use list comp
import random

rando_list = [random.randrange(1, 100) for x in range(100)]
rando_list2 = rando_list[:]
print(rando_list)



total_iterations = 0

for cur_pos in range(len(rando_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(rando_list)):
        total_iterations += 1
        if rando_list[scan_pos] < rando_list[min_pos]:
            min_pos = scan_pos
    rando_list[cur_pos], rando_list[min_pos] = rando_list[min_pos], rando_list[cur_pos]

print(rando_list)
print(total_iterations)


for key_pos in range(1, len(rando_list2)):
    key_val = rando_list2[key_pos]
    scan_pos = key_pos - 1
    while scan_pos >= 0 and rando_list2[scan_pos] > key_val:
        rando_list2[scan_pos +1] = rando_list2[scan_pos]
        scan_pos -= 1
        rando_list2[scan_pos +1] = key_val

print(rando_list2)
print(total_iterations)


print("Hello", end=" ")
print("World", end="!\n")

def hello(name, time_of_day="morning"):
    print("Hello", name, "Good", time_of_day)

hello("Owen")

# Lambda Functions

double_me = lambda x: x * 2
print(double_me(5))


my_list = [random.randrange(1, 100) for x in range(100)]

print(my_list)
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_2dlist = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(100)]
print(my_2dlist)

my_2dlist.sort()
print(my_2dlist)

my_2dlist.sort(key=lambda x: x[1])
print(my_2dlist)

my_2dlist.sort(key=lambda x: sum(x))
print(my_2dlist)

my_2dlist.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
print(my_2dlist)

new_list = sorted(my_2dlist, key=lambda x: sum(x))
print(new_list)
print(my_2dlist)








