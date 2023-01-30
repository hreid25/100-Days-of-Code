import sqlite3
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial',20,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.user = ""
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()

    def user_scored(self):
        # increase score
        self.score += 100
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def create_table(self):
        conn = sqlite3.connect('snakescores.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE scoredata (
            record_id INTEGER NOT NULL PRIMARY KEY,
            username text,
            score,
            UNIQUE(username)
            )""")
        conn.commit()
        conn.close()

    def check_table_exists(self,dbcon,table_name):
    # Function takes in a tuple containing the variable name you wish to pass into the SQL statement
        dbcur = dbcon.cursor()
        dbcur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", table_name)
        if dbcur.fetchone()[0] == 1 :
            table_exist = True
            print(f"{table_name} exists")
        else:
            table_exist = False
            print(f"{table_name} does not exist")
        return table_exist

    def game_ended(self):
        # compare the latest score with the score from the DB
        # if score is higher, update the DB score
        pass

