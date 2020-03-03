import random

print(round(243.2434235, 2))

a = 234.53465

b = 124.56446

print("My number id {} !!".format(a))
print("My numbers are {} and {}.".format(a, b))
print("My numbers are {1} and {0}. {1} is my favorite".format(a, b))

for i in range(20):
    c = random.randrange(2000)
    #print("{:6}".format(c))
    print("**{:>30}**".format(c))



for i in range(20):
    c = random.randrange(1000000)
    print("${:8,}".format(c))

for i in range(20):
    c = random.random() * 10000
    print("{:.3f}".format(c))

for i in range(20):
    c = random.randrange(1000)
    print("{:<10b}".format(c))

for i in range(20):
    c = random.randrange(1000)
    print("{:.2e}".format(c))


x = 6.77e11
print(x)

