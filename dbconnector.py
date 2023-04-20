import sqlite3

con = sqlite3.connect("Team_1_Project.db")

cursor = con.cursor()

result = cursor.execute("SELECT * FROM Graphics_Cards1")

print(result.fetchall())
