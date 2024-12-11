from flask import Flask, request, render_template
from model.conexao import listar_formularios,listar_tarefas,listar_usuarios, con
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota principal
@app.route("/")
def main():
    return render_template("main.html")

# Rota para criar formulário
@app.route("/criar")
def criar_formulario():
    return render_template("criar_formulario.html")

# Rota para o dashboard (meus formulários)
@app.route("/dashboard")
def dashboard():
    formularios = [
        {"nome": "Eu já, eu nunca", "codigo": "abc123"},
        {"nome": "Formulário 2", "codigo": "def456"},
        {"nome": "Formulário 3", "codigo": "ghi789"},
    ]  # Substitua por dados reais do banco de dados
    return render_template("dashboard.html", formularios=formularios)

# Rota para login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Aqui você processaria os dados do formulário de login
        # ...
        return redirect(url_for("dashboard"))  # Redireciona para o dashboard após o login
    return render_template("login.html")
