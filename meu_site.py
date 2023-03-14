from flask import Flask, render_template

meu_site = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@meu_site.route("/")
def homepage():
    return render_template("homepage.html")

@meu_site.route("/contatos")
def contatos():
    return render_template("contatos.html")

@meu_site.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# site local
if __name__ == "__main__":
    meu_site.run(host ='0.0.0.0', port = 7001, debug = True)
   
"""   
# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku
"""
