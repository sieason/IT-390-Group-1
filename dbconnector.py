import sqlite3
class dbResult:
    def __init__(self):
        self.con = sqlite3.connect("Team_1_Project.db")
        self.cursor = self.con.cursor()

    def __del__(self):
        self.con.close()

    def getAllRows(self):
        return self.cursor.execute("SELECT * FROM Graphics_Cards1").fetchall()

    def getLength(self):
        return len(self.getAllRows())

    def getRow(self, rowNum):
        return self.getAllRows()[rowNum]
