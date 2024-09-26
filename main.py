

import turtle
turtle.speed(10)
turtle.teleport(-305, -180)
def draw_grass (left_length, forward_length, right_length):
    for i in range (12):
        turtle.left(left_length)
        turtle.forward(forward_length)
        turtle.right(right_length)
draw_grass(5.5, 50, 6.5)
turtle.teleport(-175, -172)
turtle.left(102)
def windmill(x, y):
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
    base (200, 40, 80, 136)
    turtle.teleport(x, y)
    turtle.dot(5)
    turtle.left(90)
    def entire_triangle():
        def right_triangle(x):
            turtle.forward(x*(3**0.5))
            turtle.right(90)
            turtle.forward(x)
            turtle.right(120)
            turtle.forward(x*2)
        right_triangle(75)
        def triangle_lines(line_length, line_distance):
            turtle.up()
            turtle.back(30)
            turtle.right(60)
            turtle.forward(line_length)
            turtle.right(180)
            for i in range(6):
                turtle.up()
                turtle.left(90)
                turtle.forward(line_distance)
                turtle.right(90)
                turtle.down()
                line_length=line_length + 3/7*line_distance
                turtle.forward(line_length)
                turtle.back(line_length)
        triangle_lines(15, 15)
    for i in range (12):
        entire_triangle()
        turtle.teleport(x,y)
        turtle.left(120)
windmill(-147, 68)
turtle.teleport(130, -170)
turtle.left(90)
windmill(155, 68)
#150, 

#104.3, -87
#118.3, -81
#slope=3/7

#print (turtle.pos())
#draw windmill piece has both lines and triangle drawing. Then I also have one that draws the entire 4 triangles for the windmill

#-215, 28. -215, 108 Average is -215, 68
#-79, 108 and -79, 28. -79, 68
#Average of everythign is -147, 68
turtle.exitonclick()