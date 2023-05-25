from fastapi import FastAPI


app = FastAPI()


vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 10},
    2: {"item": "garrafa_2L", "preco_unitario": 15, "quantidade": 20},
    3: {"item": "colher", "preco_unitario": 5, "quantidade": 100},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 150},
}


# Criando a rota do API/base
@app.get("/")
def home():
    return {
        'message': 'Olá, FastAPI está no ar!!!'
}


# Rota de Contar Vendas
@app.get("/vendas")
def contar_vendas():
    return {
        'Vendas': len(vendas)           
}


# Rota de  Pegar Vendas
@app.get("/vendas/{id_venda}")
def pegar_vendas(id_venda: int):
    return vendas[id_venda]