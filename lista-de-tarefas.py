from flask import Flask, render_template, request, url_for, redirect
from banco import conectar, tabela

app = Flask(__name__)

tabela()

@app.route("/")
def index():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return render_template("index.html", tarefas=tarefas)

@app.route("/addNova", methods=["GET", "POST"])
def addNova():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO tarefas (nome, descricao) VALUES (?, ?)", (nome, descricao))
        conexao.commit()
        conexao.close()
        return redirect(url_for("index"))
    return render_template("addTarefa.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conexao = conectar()
    cursor = conexao.cursor()
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        cursor.execute("UPDATE tarefas SET nome = ?, descricao = ? WHERE id = ?", (nome, descricao, id))
        conexao.commit()
        conexao.close()
        return redirect(url_for("index"))
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (id,))
    tarefa = cursor.fetchone()
    conexao.close()
    return render_template("editarTarefa.html", tarefa=tarefa)

@app.route("/excluir/<int:id>")
def excluir(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for("index"))

if __name__ == "__main__": 
    app.run(debug=True)