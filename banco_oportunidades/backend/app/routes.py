# routes.py
# Rotas da aplicação FastAPI

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"msg": "API Banco de Oportunidades funcionando!"}

# ================================== CRUD USUARIOS =================================

@router.get("/usuarios")
def get_usuarios():
    return [{"id": 1, "nome": "João"}, {"id": 2, "nome": "Maria"}]
#------------------------------------------------------------------------------
@router.post("/usuarios")
def create_usuario(usuario: dict):
    return {"msg": "Usuário criado", "usuario": usuario}
#------------------------------------------------------------------------------
@router.get("/usuarios/{id}")
def get_usuario(id: int):
    return {"id": id, "nome": "Usuário Exemplo"}
#------------------------------------------------------------------------------
@router.put("/usuarios/{id}")
def update_usuario(id: int, usuario: dict):
    return {"msg": "Usuário atualizado", "id": id, "usuario": usuario}
#------------------------------------------------------------------------------
@router.delete("/usuarios/{id}")
def delete_usuario(id: int):
    return {"msg": "Usuário deletado", "id": id}


# ================================== FIM CRUD USUARIOS =============================

# ================================== CRUD SERVIÇOS =================================

@router.get("/servicos")
def get_servicos():
    return [{"id": 1, "titulo": "Serviço Exemplo", "valor": 100.00}]
#------------------------------------------------------------------------------
@router.post("/servicos")
def create_servico(servico: dict):
    return {"msg": "Serviço criado", "servico": servico}
#------------------------------------------------------------------------------
@router.get("/servicos/{id}")
def get_servico(id: int):
    return {"id": id, "titulo": "Serviço Exemplo", "valor": 100.00}
#------------------------------------------------------------------------------
@router.put("/servicos/{id}")
def update_servico(id: int, servico: dict):
    return {"msg": "Serviço atualizado", "id": id, "servico": servico}
#------------------------------------------------------------------------------
@router.delete("/servicos/{id}")
def delete_servico(id: int):
    return {"msg": "Serviço deletado", "id": id}

# ================================== FIM CRUD SERVIÇOS =============================

# ================================== CRUD TRANSAÇÕES =============================

@router.get("/transacoes")
def get_transacoes():
    return [{"id": 1, "servico_id": 1, "valor": 100.00, "status": "pendente"}]
#------------------------------------------------------------------------------
@router.post("/transacoes")
def create_transacao(transacao: dict):
    return {"msg": "Transação criada", "transacao": transacao}
#------------------------------------------------------------------------------
@router.get("/transacoes/{id}")
def get_transacao(id: int):
    return {"id": id, "servico_id": 1, "valor": 100.00, "status": "pendente"}
#------------------------------------------------------------------------------
@router.put("/transacoes/{id}")
def update_transacao(id: int, transacao: dict):
    return {"msg": "Transação atualizada", "id": id, "transacao": transacao}
#------------------------------------------------------------------------------
@router.delete("/transacoes/{id}")
def delete_transacao(id: int):
    return {"msg": "Transação deletada", "id": id}

# ================================== FIM CRUD TRANSAÇÕES ==========================

# ================================== CRUD CATEGORIAS =============================
@router.get("/categorias")
def get_categorias():
    return [{"id": 1, "nome": "Categoria Exemplo"}]
#------------------------------------------------------------------------------
@router.post("/categorias")
def create_categoria(categoria: dict):
    return {"msg": "Categoria criada", "categoria": categoria}
#------------------------------------------------------------------------------
@router.get("/categorias/{id}")
def get_categoria(id: int):
    return {"id": id, "nome": "Categoria Exemplo"}
#------------------------------------------------------------------------------
@router.put("/categorias/{id}")
def update_categoria(id: int, categoria: dict):
    return {"msg": "Categoria atualizada", "id": id, "categoria": categoria}
#------------------------------------------------------------------------------
@router.delete("/categorias/{id}")
def delete_categoria(id: int):
    return {"msg": "Categoria deletada", "id": id}

# ================================== FIM CRUD CATEGORIAS ==========================