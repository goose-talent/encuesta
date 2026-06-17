import sqlite3

conn = sqlite3.connect("encuestas.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS encuestas_formadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    centro TEXT,
    formador TEXT,
    respuestas TEXT
)
""")

conn.commit()
conn.close()

print("Base de datos creada correctamente")