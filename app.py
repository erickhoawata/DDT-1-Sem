from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/artefatos")
def artefatos():
    return render_template("artefatos.html")

@app.route("/avaliacao")
def avaliacao():
    return render_template("Avaliações.html")

@app.route("/equipe")
def equipe():
    return render_template("equipe.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html")

@app.route("/pilares")
def pilares():
    return render_template("pilares.html")

@app.route("/trilha")
def trilha():
    return render_template("trilha.html")