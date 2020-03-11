'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''

import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_screen = turtle.Screen()
my_screen.bgcolor('white')

def htree (x, y, width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x, y + height / 2)
        my_turtle.goto(x + width, y + height / 2)
        my_turtle.up()
        
        htree(x + width, y + height / 2, width, height / 2, depth - 1)
        htree(x + width, y - height / 2, width, height / 2, depth - 1)

my_screen.exitonclick()


