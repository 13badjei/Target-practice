# Import library code
from p5 import *
from random import randint

# The mouse_pressed function goes here
def mouse_pressed():
     if hit_colour == Color('blue').hex:  # Like the code in functions, the code in 'if' statements is indented
        print('You hit the outer circle, 50 points!')
     elif hit_colour == Color('red').hex:
        print('You hit the inner circle, 200 points!')
     elif hit_colour == Color('yellow').hex:
        print('You hit the middle, 500 points!')
     else:
        print('You missed! No points!')
    
# The shoot_arrow function goes here
def shoot_arrow():
    global hit_colour  # Can be used in other functions
    arrow_x = randint(100, 300)  # Store a random number between 100 and 300
    arrow_y = randint(100, 300)  # Store a random number between 100 and 300
    hit_colour = get(arrow_x, arrow_y).hex  # Get the hit colour
    fill('sienna')  # Set the arrow to fill colour to brown
    circle(arrow_x, arrow_y, 15)  # Draw a small circle at random coordinates

def setup():
# Setup your game here
    size(400, 400)  # width and height of screen
    no_stroke()

def draw():
# Things to do in every frame
    fill('cyan')  # Set the fill color for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height    
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height
    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle
    fill('red')  # Set the colour for the circle fill to red
    circle(200, 200, 110)  # Draw the inner circle using x, y, width
    fill('yellow')  # Set the colour for the circle fill to yellow
    circle(200, 200, 30)  # Draw the middle circle using x, y, width
    shoot_arrow()

# Keep this to run your code
run(frame_rate=2)
