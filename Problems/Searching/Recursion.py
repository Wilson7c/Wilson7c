# Recursion - Function calling itself

def f():
    print("f")
   # f()
    print("END")

f()

def g():
    print("g")
    f()

g()

# Controlling recursion with depth


def controlled(depth, max_depth):
    print("Recursion depth:", depth)
    if depth < max_depth:
        controlled(depth + 1, max_depth)
    print("Recursion depth", depth, "has closed.")

controlled(0, 10)



# Turle recursion


import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

my_screen = turtle.Screen()
my_screen.bgcolor('white')

my_turtle.fillcolor('red')
my_turtle.begin_fill()
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()


my_turtle.up()
my_turtle.goto(-200, -200)
my_turtle.down()
my_turtle.fillcolor('blue')
my_turtle.begin_fill()
my_turtle.goto(0, 0)
my_turtle.goto(0, -200)
my_turtle.goto(-200, -200)
my_turtle.end_fill()


my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(4)


my_turtle.fillcolor('yellow')
my_turtle.begin_fill()
my_turtle.setheading(90)

for i in range(12):
    my_turtle.forward(50)
    my_turtle.left(30)
my_turtle.end_fill()

my_screen.clear()
my_turtle.home()

# def recursive_rect(width, height, depth):
   # if depth > 0:
     #   my_turtle.up()
      #  my_turtle.goto(width / 2, height / 2)
      #  my_turtle.down()
      #  my_turtle.goto(width / 2, -height / 2)
      #  my_turtle.goto(-width / 2, -height / 2)
      #  my_turtle.goto(-width / 2, height / 2)
      #  my_turtle.goto(width / 2, height / 2)
       # recursive_rect(width / 2, height / 2, depth - 1)

#recursive_rect(300, 300, 5)


def ncaa(x, y, width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x, y + height / 2)
        my_turtle.goto(x + width, y + height / 2)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x, y - height / 2)
        my_turtle.goto(x + width, y - height / 2)
        ncaa(x + width, y + height / 2, width, height /2, depth - 1)
        ncaa(x + width, y - height / 2, width, height /2, depth - 1)

my_turtle.width(1)
ncaa(-300, 0, 100, 200 , 6)

my_screen.exitonclick()

