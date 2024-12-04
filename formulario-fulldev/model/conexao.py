from .database import conexao_abrir,conexao_fechar

con = conexao_abrir("junction.proxy.rlwy.net", "root", "DOiZqfbvIhEgcxMoXFqPpMPotoXKgdrC", "railway",58843)

def listar_usuarios(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall()
        resultado = ""
        for usuario in usuarios:
            resultado += (
                f"ID: {usuario['ID']} <br> "
                f"Nome: {usuario['Nome']} <br> "
                f"Email: {usuario['Email']} <br><br>"
            )
        return resultado

def listar_formularios(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Formulario")
        formularios = cursor.fetchall()
        resultado = ""
        for formulario in formularios:
            resultado += (
                f"ID: {formulario['ID']} <br> "
                f"Título: {formulario['Titulo']} <br> "
                f"Descrição: {formulario['Descricao']} <br> "
                f"Data de Criação: {formulario['DataCriacao']} <br> "
                f"ID do Usuário: {formulario['ID_Usuario']} <br><br>"
            )
        return resultado

def listar_tarefas(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Tarefa")
        tarefas = cursor.fetchall()
        resultado = ""
        for tarefa in tarefas:
            resultado += (
                f"ID: {tarefa['ID']} <br> "
                f"Descrição: {tarefa['Descricao']} <br> "
                f"Status: {tarefa['Status']} <br> "
                f"Data de Criação: {tarefa['DataCriacao']} <br> "
                f"Data de Conclusão: {tarefa['DataConclusao']} <br> "
                f"ID do Formulário: {tarefa['ID_Formulario']} <br><br>"
            )
        return resultado