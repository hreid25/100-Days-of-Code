from scoreboard import Scoreboard
import sqlite3
import os

cwd = os.getcwd()
path = (cwd) + "\Snake Game"
print(path)
os.chdir(path)

CONNECTION = sqlite3.connect('snakescores.db')

class User(Scoreboard):
    def __init__(self, username):
        super().__init__()
        self.username = username
        if not self.check_table_exists(CONNECTION, ('scoredata',)):
            print("table does not exist")
            self.create_table()
        self.check_user_exist(CONNECTION,('scoredata',))
           

    def check_user_exist(self,dbconn,table_name):
        c = CONNECTION.cursor()
        c.execute("SELECT username FROM scoredata WHERE username=?", (self.username,))
        results = c.fetchall()
        print(type(self.username),type(self.score))
        if not results:
            c.execute("INSERT INTO scoredata VALUES(:username,:score)",{'username': self.username,'score': self.score})
            CONNECTION.commit()
        # CONNECTION.close()


    def create_table(self):
        c = CONNECTION.cursor()
        c.execute("""CREATE TABLE scoredata (
            username text,
            score INTEGER,
            UNIQUE(username)
            )""")
        CONNECTION.commit()
        # CONNECTION.close()

    def check_table_exists(self,dbcon,table_name):
    # Function takes in a tuple containing the variable name you wish to pass into the SQL statement
        dbcur = CONNECTION.cursor()
        dbcur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", table_name)
        if dbcur.fetchone()[0] == 1 :
            table_exist = True
            print(f"{table_name} exists")
        else:
            table_exist = False
            print(f"{table_name} does not exist")
        CONNECTION.commit()
        # CONNECTION.close()
        return table_exist