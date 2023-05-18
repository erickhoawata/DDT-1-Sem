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
            nota_usada = 0
            nota_prof = float(request.form.get('nota_prof'))
            nota_prof = int(nota_prof)
            for linha in range(1,8):
                #pegando nome:
                nome = str(request.form.get(f"nome{linha}"))

                #pegando as notas:
                nota_proat = float(request.form.get(f"nota_proat{linha}"))
                nota_auto = float(request.form.get(f"nota_auto{linha}"))
                nota_colab = float(request.form.get(f"nota_colab{linha}"))
                nota_entreg = float(request.form.get(f"nota_entreg{linha}"))

                #somando as notas utilizadas
                soma_notas = nota_proat + nota_auto + nota_colab + nota_entreg
                nota_usada =  nota_usada + soma_notas
                

                #lista para criar tabela:
                pessoas.append([nome, int(nota_proat), int(nota_auto), int(nota_colab), int(nota_entreg)])


            
                
            # devolvendo o d para seu lugar   
            nota_usada = int(nota_usada)
            return render_template("Avaliações.html", pessoas=pessoas, metodo=metodo, nota_usada=nota_usada, nota_prof=nota_prof)
        except ValueError:
            return render_template("Avaliações.html", metodo=metodo)
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