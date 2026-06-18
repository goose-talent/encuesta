from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route("/")
def encuesta():
    return render_template("encuesta_formadores.html")


@app.route("/enviar", methods=["POST"])
def enviar():

    centro = request.form.get("centro")
    formador = request.form.get("formador")

    respuestas = {
    "calidad_formacion": request.form.get("calidad_formacion"),
    "alineacion": request.form.get("alineacion"),
    "duracion_formato": request.form.get("duracion_formato"),
    "preparacion_alumnos": request.form.get("preparacion_alumnos"),
    "aspectos_utiles": request.form.get("aspectos_utiles"),
    "mejoras_formacion": request.form.get("mejoras_formacion"),
    "calendario_formacion": request.form.get("calendario_formacion"),

    "organizacion_general": request.form.get("organizacion_general"),
    "comunicacion_previa": request.form.get("comunicacion_previa"),
    "coordinacion_evento": request.form.get("coordinacion_evento"),


    "formato_participantes": request.form.get("formato_participantes"),
    "temas_mociones": request.form.get("temas_mociones"),
    "tiempos_intervencion": request.form.get("tiempos_intervencion"),

    
    "calidad_jueces": request.form.get("calidad_jueces"),
    "feedback": request.form.get("feedback"),
    "transparencia": request.form.get("transparencia"),


    "experiencia_equipo": request.form.get("experiencia_equipo"),
    "impacto_positivo": request.form.get("impacto_positivo"),
    "frustracion": request.form.get("frustracion"),

    
    "mejoras_futuras": request.form.get("mejoras_futuras"),
    "recomendacion": request.form.get("recomendacion"),

   
    "interes": request.form.getlist("interes"),

    "comentarios_adicionales": request.form.get("comentarios_adicionales")
    }

    import sqlite3

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "encuestas.db")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO encuestas_formadores
        (centro, formador, respuestas)
        VALUES (?, ?, ?)
    """, (
        centro,
        formador,
        json.dumps(respuestas, ensure_ascii=False)
    ))

    conn.commit()
    conn.close()

    return render_template("gracias.html")
if __name__ == "__main__":
    app.run(debug=True)