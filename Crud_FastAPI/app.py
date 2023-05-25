from datetime import datetime

import uvicorn
from pydantic import BaseModel

from fastapi import FastAPI


# Criando User Model
class User(BaseModel):  # Schema
    id: int
    name: str
    lastname: str
    phone: int
    create_user: datetime = datetime.now()


class UserId(BaseModel):
    id: int


app = FastAPI()
usuarios = []


# Criando a rota do FastAPI
@app.get("/home")
def home():
    return {"message": "Welcome, I am FastAPI"}


# Criando usuário no método GET
@app.get("/user")
def get_users():
    return usuarios


# Criando usuário no método POST
@app.post("/user")
def create_user(user: User):
    usuario = user.dict()
    usuarios.append(usuario)
    return {"response": "User created successuflly"}


# Obter os usuários por ID
@app.post("/user/{user_id}")
def get_user(user_id: int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario": user}
    return {"response": "User not successfully listed"}


# Buscando outro o usuário
@app.post("/other_user")
def other_user(user_id: UserId):
    for user in usuarios:
        if user["id"] == user_id.id:
            return {"usuario": user}
    return {"response": "User not found"}


# Deletar o usuário por ID
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios.pop(index)
            return {"message": "User successfully deleted"}
    return {"response": "User not found"}


# Atualizado a informação por usuário
@app.put("/user/{user_id}")
def update_user(user_id: int, updateUser: User):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios[index]["id"] == updateUser.dic()["id"]
            usuarios[index]["name"] == updateUser.dic()["iname"]
            usuarios[index]["lastname"] == updateUser.dic()["lastname"]
            usuarios[index]["phone"] == updateUser.dic()["phone"]
            return {"message": "User successfully update"}
    return {"response": "User not found"}


# rodar o servidor da API
if __name__ == "__main__":
    uvicorn.run("app:app", port=8000)
