from flask import Flask, request ,render_template

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/artefatos")
def artefatos():
    return render_template("artefatos.html")
@app.route("/avaliacao", methods=["GET","POST"])
def avaliacao():
    metodo = request.method
    if request.method == "POST":
        
        try:
            pessoas = []
            for linha in range(1,8):
                n = str(request.form.get(f"n{linha}"))
                a = float(request.form.get(f"a{linha}"))
                b = float(request.form.get(f"b{linha}"))
                c = float(request.form.get(f"c{linha}"))
                d = float(request.form.get(f"c{linha}"))
                
                pessoas.append([n, a, b, c, d])

            # devolvendo o d para seu lugar               
            return render_template("Avaliações.html", pessoas=pessoas, metodo=metodo)
        except ValueError:
            return render_template("Avaliações.html",  pessoas=pessoas, metodo=metodo)
    else:
        # if no POST method is requested render only the page.
        return render_template("Avaliações.html", metodo=metodo)


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