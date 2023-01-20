from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
tim.color("blue")
# timmy.setpos(60,30)
end_of_square = tim.position()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

for _ in range(30):
    tim.forward(10)
    tim.pendown()
    tim.forward(10)
    tim.penup()




screen = Screen()
screen.exitonclick()