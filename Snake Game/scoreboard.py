import sqlite3

class Scoreboard():
    def __init__(self):
        self.score = 0
        self.user = ""
        # initialize the database connection
        if self.check_table_exists():
            print("table created")
        else:
            self.create_table()

    
    def user_scored(self):
        pass
    # add a number to the users score

    def create_table(self):
        conn = sqlite3.connect('snakescores.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE scoredata (
            record_id INTEGER NOT NULL PRIMARY KEY,
            username text,
            score
            UNIQUE(username)
            )""")
        conn.commit()
        conn.close()

    def check_table_exists(dbcon, tablename):
        dbcur = dbcon.cursor()
        dbcur.execute(f"""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{tablename}'
        """)
        if dbcur.fetchone()[0] == 1:
            dbcur.close()
            return True
        dbcur.close()
        return False
    

