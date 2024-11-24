from flask import Flask, request, render_template
from model.conexao import listar_formularios,listar_tarefas,listar_usuarios, con

app = Flask(__name__)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return listar_formularios(con)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/criar_formulario', methods=['GET', 'POST'])
def criar_formulario():
    return render_template('criar_formulario.html')

@app.route('/formulario/<int:id>')
def visualizar_formulario(id):
    return render_template('visualizar_formulario.html', id=id)

@app.route('/formulario/<int:id>/editar', methods=['GET', 'POST'])
def editar_formulario(id):
    return render_template('editar_formulario.html', id=id)

@app.route('/formulario/<int:id>/excluir', methods=['POST'])
def excluir_formulario(id):
    return render_template('excluir_formulario.html', id=id)

@app.route('/formulario/<int:id>/responder', methods=['GET', 'POST'])
def responder_formulario(id):
    return render_template('responder_formulario.html', id=id)

@app.route('/formulario/<int:id_formulario>/tarefa/<int:id_tarefa>/editar', methods=['GET', 'POST'])
def editar_tarefa(id_formulario, id_tarefa):
    return render_template('editar_tarefa.html', id_formulario=id_formulario, id_tarefa=id_tarefa)

@app.route('/formulario/<int:id_formulario>/tarefa/<int:id_tarefa>/excluir', methods=['POST'])
def excluir_tarefa(id_formulario, id_tarefa):
    return render_template('excluir_tarefa.html', id_formulario=id_formulario, id_tarefa=id_tarefa)

if __name__ == '__main__':
    app.run(debug=True)

if __name__=='__main__':
  app.run(debug=True)