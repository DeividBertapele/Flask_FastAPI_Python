import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


# Construir as funcionalidades
@app.route("/")
def homepage():
    return "API está no ar!!!"


# Pegas as vendas
@app.route("/pegarvendas")
def pegarvendas():
    tabela = pd.read_csv("pegarvendas.csv")
    total_vendas = tabela["Vendas"].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


# rodar o servidor da API
if __name__ == "__main__":
    app.run(debug=True)