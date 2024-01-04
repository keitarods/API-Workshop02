from typing import List, Dict

class Produtos:
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

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produtos(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return "Falha na busca do produto. Favor insira um produto válido"
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto