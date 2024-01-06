from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException

from .schema import ProdutosSchema
from .config import Session_local, get_db
from .model import Produto

router = APIRouter()

@router.get("/") #Request
def ola_mundo(): #Response
    return {"Olá":"Mundo"}

@router.get("/produtos", response_model = list[ProdutosSchema])
def listar_produtos(db:Session = Depends(get_db)):
    return db.query(Produto).all() #Select * FROM produtos

@router.get("/produtos/{produto_id}", response_model = ProdutosSchema)
def buscar_produtos(produto_id: int, db:Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    else:
        HTTPException(status_code=404, detail = "Produto não encontrado")

@router.post("/produtos", response_model= ProdutosSchema)
def inserir_produto(produto: ProdutosSchema, db:Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.delete("/produtos/{produto_id}", response_model = ProdutosSchema)
def remover_produto(produto_id: int, db:Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto.id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else:
        raise HTTPException(status_code=404, detail= "Produto não encontrado")
    
@router.put("/produtos/{produto_id}", response_model = ProdutosSchema)
def atualizar_produto(produto_id: int, produto_data: ProdutosSchema, db:Session = Depends(get_db)):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto,key,value) if value else None
        db.commit()
        db.refresh(db_produto)
        return db_produto
    else:
        HTTPException(status_code=404, detail="Produto não encontrado")