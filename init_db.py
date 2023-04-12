import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cursor = conn.cursor()

cursor.execute("INSERT INTO mon (dex, monName) VALUES(?, ?)",
               (1,'Bulbasaur')
               )

cursor.execute("INSERT INTO mon (dex, monName) VALUES(?, ?)",
               (151,'Mew')
               )
conn.commit()
conn.close()
