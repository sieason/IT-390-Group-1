import sqlite3
class dbResult:
    def __init__(self):
        self.con = sqlite3.connect("Team_1_Project.db")
        self.cursor = con.cursor()

    def __del__(self):
        self.con.close()

    def getRow(self):
        return self.cursor.execute("SELECT * FROM Graphics_Cards1").fetchall()

r = dbResult()
print(r.getRow())
