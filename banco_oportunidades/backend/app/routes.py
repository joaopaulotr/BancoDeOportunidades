# routes.py
# Rotas da aplicação FastAPI


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from pydantic import BaseModel
from .models import Usuario, Servico, Transacao, Categoria

router = APIRouter()

@router.get("/")
def home():
    return {"msg": "Bem vindo a API Banco de Oportunidades"}


@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == data.email).first()
    if not usuario or usuario.senha_hash != data.senha_hash:
        raise HTTPException(status_code=401, detail="E-mail ou senha inválidos")
    return {"msg": "Login realizado com sucesso", "id": usuario.idUsuario, "nome": usuario.nome}

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

    # Verificação simples de email, CPF/CNPJ e nome únicos
    if (novo_usuario.email == db.query(Usuario).filter(Usuario.email == usuario.email).first()):
        return {"msg": "Erro: Email já cadastrado."}
    
    if (novo_usuario.cpf_cnpj == db.query(Usuario).filter(Usuario.cpf_cnpj == usuario.cpf_cnpj).first()):
        return {"msg": "Erro: CPF/CNPJ já cadastrado."}
    
    if (novo_usuario.nome == db.query(Usuario).filter(Usuario.nome == usuario.nome).first()):
        return {"msg": "Erro: Nome de usuário já cadastrado."}
    # Verificação simples de email, CPF/CNPJ e nome únicos

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"msg": "Usuário criado", "id": novo_usuario.idUsuario, "nome": novo_usuario.nome}

#------------------------------------------------------------------------------
@router.get("/usuarios/{id}")
def get_usuario(id: int, db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.idUsuarios == id).first()
#------------------------------------------------------------------------------
@router.put("/usuarios/{id}")
def update_usuario(id: int, usuario: dict):
    from fastapi import Body
    @router.put("/usuarios/{id}")
    def update_usuario(id: int, usuario: dict = Body(...), db: Session = Depends(get_db)):
        usuario_db = db.query(Usuario).filter(Usuario.idUsuarios == id).first()
        if not usuario_db:
            return {"msg": "Usuário não encontrado", "id": id}
        for key, value in usuario.items():
            if hasattr(usuario_db, key):
                setattr(usuario_db, key, value)
        db.commit()
        db.refresh(usuario_db)
        return {"msg": "Usuário atualizado", "id": id, "usuario": usuario}
#------------------------------------------------------------------------------
@router.delete("/usuarios/{id}")
def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.idUsuarios == id).first()
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
    Categorias_idCategorias: int
    titulo: str
    descricao: str
    preco: float
    cidade: str
    status: str

@router.post("/servicos")
def create_servico(servico: CreateServico, db: Session = Depends(get_db)):
    novo_servico = Servico(
        Categorias_idCategorias=servico.Categorias_idCategorias,
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
    return db.query(Servico).filter(Servico.idServicos == id).first()
#------------------------------------------------------------------------------
@router.put("/servicos/{id}")
def update_servico(id: int, servico: dict, db: Session = Depends(get_db)):
    servico_db = db.query(Servico).filter(Servico.idServicos == id).first()
    if not servico_db:
        return {"msg": "Serviço não encontrado", "id": id}
    for key, value in servico.items():
        if hasattr(servico_db, key):
            setattr(servico_db, key, value)
    db.commit()
    db.refresh(servico_db)
    return {"msg": "Serviço atualizado", "id": id, "servico": servico}
#------------------------------------------------------------------------------
@router.delete("/servicos/{id}")
def delete_servico(id: int, db: Session = Depends(get_db)):
    servico = db.query(Servico).filter(Servico.idServicos == id).first()
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
    Usuarios_idUsuarios: int
    Servicos_idServicos: int
    valorPago: float
    status: str
    avaliacao: int = None

@router.post("/transacoes")
def create_transacao(transacao: CreateTransacao, db: Session = Depends(get_db)):
    nova_transacao = Transacao(
        Usuarios_idUsuarios=transacao.Usuarios_idUsuarios,
        Servicos_idServicos=transacao.Servicos_idServicos,
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
    return db.query(Transacao).filter(Transacao.idTransacoes == id).first()
#------------------------------------------------------------------------------
@router.put("/transacoes/{id}")
def update_transacao(id: int, transacao: dict, db: Session = Depends(get_db)):
    transacao_db = db.query(Transacao).filter(Transacao.idTransacoes == id).first()
    if not transacao_db:
        return {"msg": "Transação não encontrada", "id": id}
    for key, value in transacao.items():
        if hasattr(transacao_db, key):
            setattr(transacao_db, key, value)
    db.commit()
    db.refresh(transacao_db)
    return {"msg": "Transação atualizada", "id": id, "transacao": transacao}
#------------------------------------------------------------------------------
@router.delete("/transacoes/{id}")
def delete_transacao(id: int, db: Session = Depends(get_db)):
    transacao = db.query(Transacao).filter(Transacao.idTransacoes == id).first()
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
    nomeCategoria: str
    descricaoCategoria: str

@router.post("/categorias")
def create_categoria(categoria: CreateCategoria, db: Session = Depends(get_db)):
    nova_categoria = Categoria(
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
    return db.query(Categoria).filter(Categoria.idCategorias == id).first()
#------------------------------------------------------------------------------
@router.put("/categorias/{id}")
def update_categoria(id: int, categoria: dict, db: Session = Depends(get_db)):
    categoria_db = db.query(Categoria).filter(Categoria.idCategorias == id).first()
    if not categoria_db:
        return {"msg": "Categoria não encontrada", "id": id}
    for key, value in categoria.items():
        if hasattr(categoria_db, key):
            setattr(categoria_db, key, value)
    db.commit()
    db.refresh(categoria_db)
    return {"msg": "Categoria atualizada", "id": id, "categoria": categoria}
#------------------------------------------------------------------------------
@router.delete("/categorias/{id}")
def delete_categoria(id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.idCategorias == id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
        return {"msg": "Categoria deletada", "id": id}
    return {"msg": "Categoria não encontrada", "id": id}

# ================================== FIM CRUD CATEGORIAS ==========================