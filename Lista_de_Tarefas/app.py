from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas (apenas em memória, não usa banco de dados ainda)
tarefas = []

@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    tarefa = request.form.get("tarefa")
    if tarefa:
        tarefas.append(tarefa)
    return redirect(url_for("index"))

@app.route("/remover/<int:index>")
def remover(index):
    if 0 <= index < len(tarefas):
        tarefas.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
