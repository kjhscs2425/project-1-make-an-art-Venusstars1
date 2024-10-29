

import turtle
turtle.speed(10)
turtle.teleport(-305, -180)
left_length=5.5
#If this variable is increased, the grass will go higher and not go back down
forward_length=50
#If this variable is increased, the same thing will happen
right_length=6.5
#This variable being increased makes the grass go down
def draw_grass ():
#Makes the grass zigzag and makes it look more natural. Moves the turtle left, then forward, 
#then right and so on
    for i in range (12):
        turtle.left(left_length)
        turtle.forward(forward_length)
        turtle.right(right_length)
#left_length, forward_length, and right_length can take a lot of different variables
#depending on how smooth or rough you want the grass, and how high it goes.
draw_grass()
#Give the parameters a variable and draws the grass
turtle.teleport(-175, -172)
#Teleports the turtle to draw the backbone/base of the windmill
turtle.left(102)
#Turns the turtle to prepare it to draw the windmill
def windmill(x, y):
#Put as x, y so that I can put the coordinates for the second windmill as well
#x, y can be any coordinate in theory, depending on what the coordinates are it might look funky
    def base(side_forward, box_bottom, square_side, square_top):
        turtle.forward(side_forward)
        turtle.left(90)
        turtle.forward(box_bottom)
        turtle.right(90)
        turtle.forward(square_side)
        turtle.right(90)
        turtle.forward(square_top)
        turtle.right(90)
        turtle.forward(square_side)
        turtle.right(90)
        turtle.forward(box_bottom)
        turtle.left(90)
        turtle.forward(side_forward)
#The four variables can be whatever you want depending on how big and symmetrical you want it to be. 
    base (200, 40, 80, 136)
    turtle.teleport(x, y)
#Teleports to the middle of the windmill
    turtle.dot(5)
#Makes a dot, can be any size.
    turtle.left(90)
    def entire_triangle():
        def right_triangle(x):
#x is the variable of the side length of the triangle
#By changing x you can make the triangle bigger or smaller because it will change the side lengths.
            turtle.forward(x*(3**0.5))
            turtle.right(90)
            turtle.forward(x)
            turtle.right(120)
            turtle.forward(x*2)
        right_triangle(75)
        def triangle_lines(starting_line_length, line_distance):
#Makes the triangle lines inside of the triangle
            turtle.up()
            turtle.back(30)
            turtle.right(60)
            turtle.forward(starting_line_length)
            turtle.right(180)
#Sets up the beginning of the triangle lines
            for i in range(1,7):
                turtle.up()
                turtle.left(90)
                turtle.forward(line_distance)
                turtle.right(90)
                turtle.down()
                line_length =starting_line_length + i*3/7*line_distance
#Changes the line length every time it goes through the for loop so that
#the line gets longer as the triangle gets bigger.
                turtle.forward(line_length)
#Uses the new line length to draw the line inside of the triangle. 
                turtle.back(line_length)
        triangle_lines(15, 15)
    for i in range (12):
        entire_triangle()
#Draws the triangle with lines and everything
        turtle.teleport(x,y)
#Puts it back to the center of the windmill
        turtle.left(120)
#Sets up for the next triangle
windmill(-147, 68)
turtle.teleport(130, -170)
turtle.left(90)
#Sets up for a new windmill
windmill(155, 68)


#150, 

#104.3, -87
#118.3, -81
#slope=3/7

#-215, 28. -215, 108 Average is -215, 68
#-79, 108 and -79, 28. -79, 68
#Average of everythign is -147, 68
turtle.exitonclick()