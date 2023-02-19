from turtle import Turtle

class state_obj(Turtle):
    def __init__(self, x_pos, y_pos,user_answer):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto((x_pos,y_pos))
        self.write(user_answer, font=('Arial',8,'normal'))


