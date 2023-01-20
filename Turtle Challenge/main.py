from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
# end_of_square = tim.position()

# for _ in range(4):
    # tim.forward(100)
    # tim.right(angle)

sides = [{'triangle':3, 'square':4, 'pentagon':5, 'hexagon':6, 'heptagon':7, 'octagon':8, 'nonagon':9, 'decagon':9}]
angles = {k:360/v for k,v in sides[0].items()}

for shape, angle in angles.items():
    print("shape: ", shape, "| angle: ", angle)
    for turn in sides[0]:
        tim.forward(100)
        tim.right(angle)

# for _ in range(30):
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()

screen = Screen()
screen.exitonclick()