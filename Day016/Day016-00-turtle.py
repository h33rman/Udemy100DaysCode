import turtle

timmy = turtle.Turtle()
"""
 Initially there are the following polygon shapes: 
 “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
 """
timmy.shape("turtle")
timmy.color("coral")
# Move the turtle 100 steps
timmy.forward(100)

my_screen = turtle.Screen()
my_screen.exitonclick()
