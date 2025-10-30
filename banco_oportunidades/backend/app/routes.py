# routes.py
# Rotas da aplicação FastAPI


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from pydantic import BaseModel
from .models import Usuario, Servico, Transacao, Categoria

router = APIRouter()

@router.get("/")
def home():
    return {"msg": "API Banco de Oportunidades funcionando!"}

# ================================== CRUD USUARIOS =================================

@router.get("/usuarios")
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()
#------------------------------------------------------------------------------

class CreateUsuario(BaseModel):
    nome: str
    email: str
    senha_hash: str
    cpf_cnpj: str
    tipoUsuario: str
    telefone: str
    endereco: str
    cidade: str
    uf: str

@router.post("/usuarios")
def create_usuario(usuario: CreateUsuario, db: Session = Depends(get_db)):
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=usuario.senha_hash,
        cpf_cnpj=usuario.cpf_cnpj,
        tipoUsuario=usuario.tipoUsuario,
        telefone=usuario.telefone,
        endereco=usuario.endereco,
        cidade=usuario.cidade,
        uf=usuario.uf
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"msg": "Usuário criado", "id": novo_usuario.idUsuario, "nome": novo_usuario.nome}

#------------------------------------------------------------------------------
@router.get("/usuarios/{id}")
def get_usuario(id: int, db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.idUsuario == id).first()
#------------------------------------------------------------------------------
@router.put("/usuarios/{id}")
def update_usuario(id: int, usuario: dict):
    return {"msg": "Usuário atualizado", "id": id, "usuario": usuario}
#------------------------------------------------------------------------------
@router.delete("/usuarios/{id}")
def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.idUsuario == id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return {"msg": "Usuário deletado", "id": id}
    return {"msg": "Usuário não encontrado", "id": id}


# ================================== FIM CRUD USUARIOS =============================

# ================================== CRUD SERVIÇOS =================================

@router.get("/servicos")
def get_servicos(db: Session = Depends(get_db)):
    return db.query(Servico).all()
#------------------------------------------------------------------------------

class CreateServico(BaseModel):
    idServico: str
    idUsuario: str
    idCategoria: str
    titulo: str
    descricao: str
    preco: str
    cidade: str
    status: str

@router.post("/servicos")
def create_servico(servico: CreateServico, db: Session = Depends(get_db)):
    novo_servico = Servico(
        idServico=servico.idServico,
        idUsuario=servico.idUsuario,
        idCategoria=servico.idCategoria,
        titulo=servico.titulo,
        descricao=servico.descricao,
        preco=servico.preco,
        cidade=servico.cidade,
        status=servico.status
    )
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return {"msg": "Serviço criado", "id": novo_servico.idServico, "titulo": novo_servico.titulo}
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
def delete_servico(id: int, db: Session = Depends(get_db)):
    servico = db.query(Servico).filter(Servico.idServico == id).first()
    if servico:
        db.delete(servico)
        db.commit()
        return {"msg": "Serviço deletado", "id": id}
    return {"msg": "Serviço não encontrado", "id": id}

# ================================== FIM CRUD SERVIÇOS =============================

# ================================== CRUD TRANSAÇÕES =============================

@router.get("/transacoes")
def get_transacoes(db: Session = Depends(get_db)):
    return db.query(Transacao).all()
#------------------------------------------------------------------------------
class CreateTransacao(BaseModel):
    idTransacao: str
    idServico: str
    idCliente: str
    dataSolicitacao: str
    valorPago: str
    status: str
    avaliacao: str

@router.post("/transacoes")
def create_transacao(transacao: CreateTransacao, db: Session = Depends(get_db)):
    nova_transacao = Transacao(
        idTransacao=transacao.idTransacao,
        idServico=transacao.idServico,
        idCliente=transacao.idCliente,
        dataSolicitacao=transacao.dataSolicitacao,
        valorPago=transacao.valorPago,
        status=transacao.status,
        avaliacao=transacao.avaliacao
    )
    db.add(nova_transacao)
    db.commit()
    db.refresh(nova_transacao)
    return {"msg": "Transação criada", "id": nova_transacao.idTransacao}
#------------------------------------------------------------------------------
@router.get("/transacoes/{id}")
def get_transacao(id: int, db: Session = Depends(get_db)):
    return db.query(Transacao).filter(Transacao.idTransacao == id).first()
#------------------------------------------------------------------------------
@router.put("/transacoes/{id}")
def update_transacao(id: int, transacao: dict):
    return {"msg": "Transação atualizada", "id": id, "transacao": transacao}
#------------------------------------------------------------------------------
@router.delete("/transacoes/{id}")
def delete_transacao(id: int, db: Session = Depends(get_db)):
    transacao = db.query(Transacao).filter(Transacao.idTransacao == id).first()
    if transacao:
        db.delete(transacao)
        db.commit()
        return {"msg": "Transação deletada", "id": id}
    return {"msg": "Transação não encontrada", "id": id}

# ================================== FIM CRUD TRANSAÇÕES ==========================

# ================================== CRUD CATEGORIAS =============================
@router.get("/categorias")
def get_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()
#------------------------------------------------------------------------------
class CreateCategoria(BaseModel):
    idCategoria: str
    nomeCategoria: str
    descricaoCategoria: str

@router.post("/categorias")
def create_categoria(categoria: CreateCategoria, db: Session = Depends(get_db)):
    nova_categoria = Categoria(
        idCategoria=categoria.idCategoria,
        nomeCategoria=categoria.nomeCategoria,
        descricaoCategoria=categoria.descricaoCategoria
    )
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return {"msg": f"Categoria {nova_categoria.nomeCategoria} criada", "id": nova_categoria.idCategoria}
#------------------------------------------------------------------------------
@router.get("/categorias/{id}")
def get_categoria(id: int, db: Session = Depends(get_db)):
    return db.query(Categoria).filter(Categoria.idCategoria == id).first()
#------------------------------------------------------------------------------
@router.put("/categorias/{id}")
def update_categoria(id: int, categoria: dict):
    return {"msg": "Categoria atualizada", "id": id, "categoria": categoria}
#------------------------------------------------------------------------------
@router.delete("/categorias/{id}")
def delete_categoria(id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.idCategoria == id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
        return {"msg": "Categoria deletada", "id": id}
    return {"msg": "Categoria não encontrada", "id": id}

# ================================== FIM CRUD CATEGORIAS ==========================