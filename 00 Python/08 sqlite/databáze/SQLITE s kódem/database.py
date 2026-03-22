import sqlite3

#spojení s databází
connection = sqlite3.connect("game.db")

#vytvoření kurzoru, který nám umožňuje navigaci po databázi
cursor = connection.cursor()

# user_input = input("Add a character to the database: ")
# user_input2 = input("Which class he's in: ")

#zápis do db
# cursor.execute("INSERT INTO characters (name, class) VALUES (?, ?)", (user_input, user_input2))
cursor.execute("SELECT * FROM characters")

#uložení dat
data = cursor.fetchall()
# print(data)

for row in data:
    print(row)

#POTVRZENÍ VLOŽENÍ DAT DO DB
connection.commit()

connection.close()