for i in range(5, 51, 5):
    print(i, end=" ")

my_list = [x for x in range(100)]
print(my_list)


my_list = list(range(100))
print(my_list)


for number in my_list:
    if number > 10:
        break
    print(number, end="Wilson")

print("End of loop")

# Continue

for number in my_list:
    if number % 7 == 0:
        continue
    print(number, end=" ")

for number in my_list:
    print(number, end=" ")
    if number == 80:
        break
else:
    print("The loop completed naturally")

