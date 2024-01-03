from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone que é inteligente",
        "preco": 1500.0,
        "disponível": True,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um computador que é movel",
        "preco": 3500.0,
        "disponivel": False,
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um computador que é movel",   
        "preco": 2500.0,
        "disponivel": True,
    }
]


@app.get("/") #Request
def ola_mundo(): #Response
    return {"Olá":"Mundo"}

@app.get("/produtos")
def listar_produtos():
    return produtos