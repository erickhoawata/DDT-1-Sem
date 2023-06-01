from flask import Flask, request ,render_template

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/artefatos")
def artefatos():
    return render_template("artefatos.html")

@app.route("/teste2")
def Teste2():
    return render_template("teste2.html")

@app.route("/avaliacao", methods=["GET","POST"])
def avaliacao():
    metodo = request.method
    if request.method == "POST":
        
        try:
            #pegando quantidade de integrantes:
            qtd_pessoas = float(request.form.get('qtd_pessoas'))
            qtd_pessoas = int(qtd_pessoas)
            #pegando notas da tabela menor:
            nota_proc = float(request.form.get('nota_proc'))
            nota_proc = int(nota_proc)

            nota_prodt = float(request.form.get('nota_prodt'))
            nota_prodt = int(nota_prodt)

            nota_compt = float(request.form.get('nota_compt'))
            nota_compt = int(nota_compt)
            if nota_compt*nota_proc*nota_prodt==1:
                nota_total1 = 25
                vali_sprint = 1
            else: 
                nota_total1 = 0
                vali_sprint = 0
            #encerrando tabela menor

            #tabela retangular
            nota_PO = float(request.form.get('nota_PO'))
            nota_PO=int(nota_PO)
            if nota_PO == 3: porcent_PO=25
            elif nota_PO == 2: porcent_PO=15
            elif nota_PO == 1: porcent_PO=5
            else: porcent_PO=0

            nota_SM = float(request.form.get('nota_SM'))
            nota_SM=int(nota_SM)
            if nota_SM == 3: porcent_SM=25
            elif nota_SM == 2: porcent_SM=15
            elif nota_SM == 1: porcent_SM=5
            else: porcent_SM=0

            nota_DT = float(request.form.get('nota_DT'))
            nota_DT=int(nota_DT)
            if nota_DT == 3: porcent_DT=25
            elif nota_DT == 2: porcent_DT=15
            elif nota_DT == 1: porcent_DT=5
            else: porcent_DT=0

            soma_porcent = porcent_DT+porcent_PO+porcent_SM+nota_total1
            if 75< soma_porcent <=100:
                nota_ind=12
            elif 50 < soma_porcent <= 75:
                nota_ind=8
            elif 25 < soma_porcent <= 50:
                nota_ind=4
            else:
                nota_ind=0

            nota_grupo = nota_ind*qtd_pessoas
            nota_grupo = int(nota_grupo)
            #tabela maior e nota utlizada
            pessoas = []
            nota_usada = 0
            for linha in range(1,11):
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


            
                
            # devolvendo tudo para seu lugar   
            nota_usada = int(nota_usada)
            return render_template("Avaliações.html", pessoas=pessoas, metodo=metodo, nota_usada=nota_usada, nota_total1=nota_total1, nota_prodt=nota_prodt, nota_proc=nota_proc, nota_compt=nota_compt, porcent_PO=porcent_PO, porcent_DT=porcent_DT, porcent_SM=porcent_SM, nota_DT=nota_DT, nota_PO=nota_PO, nota_SM=nota_SM, soma_porcent=soma_porcent, nota_grupo=nota_grupo, qtd_pessoas=qtd_pessoas, vali_sprint=vali_sprint)
        except ValueError:
            nota_usada=0
            return render_template("Avaliações.html", metodo=metodo, nota_usada=nota_usada)
    else:
        # if no POST method is requested render only the page.
        nota_usada=0
        nota_grupo=0
        return render_template("Avaliações.html", metodo=metodo, nota_usada=nota_usada, nota_grupo=nota_grupo)


@app.route("/equipe")
def equipe():
    return render_template("equipe.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html")

@app.route("/trilha")
def trilha():
    return render_template("trilha.html")

@app.route("/pilares")
def pilares():
    return render_template("pilares.html")

@app.route("/teste")
def teste():
    return render_template("teste.html")

# @app.route("/teste", methods=["GET","POST"])
# def avaliacao():
#     metodo = request.method
#     if request.method == "POST":
    
#         try:
#             fun_carlos=str(request.form.get('fun_carlos'))
#             fun_roberta=str(request.form.get('fun_roberta'))
#             fun_everton=str(request.form.get('fun_everton'))
#             fun_fabricio=str(request.form.get('fun_fabricio'))
#             fun_sara=str(request.form.get('fun_sara'))
# def teste():
#     return render_template("teste.html")
