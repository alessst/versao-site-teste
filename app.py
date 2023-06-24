from flask import Flask, render_template, request
#from Planilha import planilha

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST": 
        nome = request.form.get("nome", False)
        email = request.form.get("email", False)
        numero = request.form.get("numero", False)
        mensagem = request.form.get("mensagem", False)
        if request.form.get("nome") and request.form.get("email") and  request.form.get("numero") and  request.form.get("mensagem") :
            #planilha.planilha(nome, email, numero, mensagem)
            print("manda formulario")
    return render_template("index.html")

@app.route("/sobre_mim")
def sobre():
    return render_template("about.html")

@app.route("/promo")
def promo():
    return render_template("pricing.html")

@app.route("/contato")
def contato():
    return render_template("contact.html")

@app.route("/serviços")
def servico():
    return render_template("we-do.html")

@app.route("/mural_beleza")
def mural():
    return render_template("mural.html")


if __name__ == "__main__":
    app.run(debug=True)


