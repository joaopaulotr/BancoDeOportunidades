
from sqlalchemy import Column, Integer, String, Enum, DateTime, Text, DECIMAL, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    idUsuarios = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    senha_hash = Column(String(255))
    cpf_cnpj = Column(String(20))
    tipoUsuario = Column(Enum('prestador', 'cliente', 'admin'))
    telefone = Column(String(20))
    endereco = Column(String(255))
    cidade = Column(String(100))
    uf = Column(CHAR(2))
    dataCadastro = Column(DateTime, default=datetime.utcnow)
    transacoes = relationship('Transacao', back_populates='usuario', foreign_keys='Transacao.Usuarios_idUsuarios')

class Categoria(Base):
    __tablename__ = "Categorias"

    idCategorias = Column(Integer, primary_key=True, index=True)
    nomeCategoria = Column(String(100))
    descricaoCategoria = Column(String(255))
    servicos = relationship('Servico', back_populates='categoria', foreign_keys='Servico.Categorias_idCategorias')

class Servico(Base):
    __tablename__ = "Servicos"

    idServicos = Column(Integer, primary_key=True, index=True)
    Categorias_idCategorias = Column(Integer, ForeignKey('Categorias.idCategorias'))
    titulo = Column(String(100))
    descricao = Column(Text)
    preco = Column(DECIMAL(10,2))
    cidade = Column(String(100))
    status = Column(Enum('ativo', 'inativo'))
    dataCriacao = Column(DateTime, default=datetime.utcnow)
    categoria = relationship('Categoria', back_populates='servicos', foreign_keys=[Categorias_idCategorias])
    transacoes = relationship('Transacao', back_populates='servico', foreign_keys='Transacao.Servicos_idServicos')

class Transacao(Base):
    __tablename__ = "Transacoes"

    idTransacoes = Column(Integer, primary_key=True, index=True)
    Usuarios_idUsuarios = Column(Integer, ForeignKey('Usuarios.idUsuarios'))
    Servicos_idServicos = Column(Integer, ForeignKey('Servicos.idServicos'))
    dataSolicitacao = Column(DateTime, default=datetime.utcnow)
    valorPago = Column(DECIMAL(10,2))
    status = Column(Enum('pendente', 'em_andamento', 'concluido', 'cancelado'))
    avaliacao = Column(Integer)
    usuario = relationship('Usuario', back_populates='transacoes', foreign_keys=[Usuarios_idUsuarios])
    servico = relationship('Servico', back_populates='transacoes', foreign_keys=[Servicos_idServicos])