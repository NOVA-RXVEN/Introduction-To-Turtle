import turtle 

turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500,700)

polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(0, num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
