import sqlite3
import pandas as pd
import json
from openpyxl import load_workbook

conn = sqlite3.connect("encuestas.db")

df = pd.read_sql_query(
    "SELECT * FROM encuestas_formadores",
    conn
)

filas = []

for _, row in df.iterrows():

    respuestas = json.loads(row["respuestas"])

    nueva_fila = {
        "fecha": row["fecha"],
        "centro": row["centro"],
        "formador": row["formador"],
        **respuestas
    }

    filas.append(nueva_fila)

resultado = pd.DataFrame(filas)

resultado.to_excel(
    "respuestas_encuesta.xlsx",
    index=False
)

wb = load_workbook("respuestas_encuesta.xlsx")
ws = wb.active

for column in ws.columns:
    max_length = 0
    column_letter = column[0].column_letter

    for cell in column:
        try:
            if cell.value:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )
        except:
            pass

    ws.column_dimensions[column_letter].width = min(max_length + 5, 60)

wb.save("respuestas_encuesta.xlsx")

conn.close()

print("Excel generado correctamente")