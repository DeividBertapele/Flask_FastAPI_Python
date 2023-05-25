from flask import Flask, jsonify, request

app = Flask(__name__)


livros = [
    {
        "id": 1,
        "titulo": "Inteligência Emocional",
        "autor": "Daniel Coleman",
    },
    {
        "id": 2,
        "titulo": "Mindset: A nova psicologia do sucesso",
        "autor": "Carol S. Dweck",
    },
    {
        "id": 3,
        "titulo": "O poder do hábito",
        "autor": "Charles Duhigg",
    },
    {
        "id": 4,
        "titulo": "O homem mais rico da Babilônia",
        "autor": "George S Clason",
    },
]


# Consultar todos
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)


# Consultar o id
@app.route("/livros/<int:id>", methods=["GET"])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)


# Editar
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Criar
@app.route("/livros", methods=["POST"])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# Excluir
@app.route("livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            del livros[indice]

    return jsonify(livros)


if __name__ == "__main__":
    app.run(debug=True)
