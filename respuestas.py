import sqlite3

conn = sqlite3.connect("encuestas.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM encuestas_formadores")

for fila in cursor.fetchall():
    print(fila)

conn.close()