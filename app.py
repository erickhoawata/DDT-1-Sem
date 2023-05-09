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
    if request.method == "POST":
        
        try:
            # Para os nomes:
            n1 = str(request.form.get("n1"))
            n2 = str(request.form.get("n2"))
            n3 = str(request.form.get("n3"))
            n4 = str(request.form.get("n4"))
            n5 = str(request.form.get("n5"))
            n6 = str(request.form.get("n6"))
            n7 = str(request.form.get("n7"))
            # Pegando a b c da linha 1 
            a1 = int(request.form.get("a1"))
            b1 = int(request.form.get("b1"))
            c1 = int(request.form.get("c1"))
            # achando o d da linha 1
            d1 = a1*0.3+b1*0.3+c1*0.4
            d1 = int(d1)
            
            # Pegando a b c da linha 2
            a2 = int(request.form.get("a2"))
            b2 = int(request.form.get("b2"))
            c2 = int(request.form.get("c2"))
            # achando o d da linha 2
            d2 = a2*0.3+b2*0.3+c2*0.4
            d2 = int(d2)

            # Pegando a b c da linha 3 
            a3 = int(request.form.get("a3"))
            b3 = int(request.form.get("b3"))
            c3 = int(request.form.get("c3"))
            # achando o d da linha 3
            d3 = a3*0.3+b3*0.3+c3*0.4
            d3 = int(d3)

            # Pegando a b c da linha 4
            a4 = int(request.form.get("a4"))
            b4 = int(request.form.get("b4"))
            c4 = int(request.form.get("c4"))
            # achando o d da linha 4
            d4 = a4*0.3+b4*0.3+c4*0.4
            d4 = int(d4)

            # Pegando a b c da linha 5
            a5 = int(request.form.get("a5"))
            b5 = int(request.form.get("b5"))
            c5 = int(request.form.get("c5"))
            # achando o d da linha 5
            d5 = a5*0.3+b5*0.3+c5*0.4
            d5 = int(d5)

            # Pegando a b c da linha 6
            a6 = int(request.form.get("a6"))
            b6 = int(request.form.get("b6"))
            c6 = int(request.form.get("c6"))
            # achando o d da linha 1
            d6 = a6*0.3+b6*0.3+c6*0.4
            d6 = int(d6)
  
            # Pegando a b c da linha 7
            a7 = int(request.form.get("a7"))
            b7 = int(request.form.get("b7"))
            c7 = int(request.form.get("c7"))
            # achando o d da linha 7
            d7 = a7*0.3+b7*0.3+c7*0.4
            d7 = int(d7)
            
            # devolvendo o d para seu lugar                    
            return render_template("Avaliações.html", d1 =d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7,a1 =a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, b1 =b1, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, b7=b7,c1 =c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, n7=n7)
        except ValueError:
            return render_template("Avaliações.html", n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, n7=n7)
    else:
        # if no POST method is requested render only the page.
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