from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
from .database import Base 

from sqlalchemy import Column, Integer, String, Enum, DateTime, Text, DECIMAL, ForeignKey, CHAR
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "Usuarios"

    idUsuario = Column(Integer, primary_key=True, index=True)
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
    servicos = relationship('Servico', back_populates='usuario')
    transacoes_cliente = relationship('Transacao', back_populates='cliente', foreign_keys='Transacao.idCliente')

class Categoria(Base):
    __tablename__ = "Categorias"

    idCategoria = Column(Integer, primary_key=True, index=True)
    nomeCategoria = Column(String(100))
    descricaoCategoria = Column(String(255))
    servicos = relationship('Servico', back_populates='categoria')

class Servico(Base):
    __tablename__ = "Servicos"

    idServico = Column(Integer, primary_key=True, index=True)
    idUsuario = Column(Integer, ForeignKey('Usuarios.idUsuario'))
    idCategoria = Column(Integer, ForeignKey('Categorias.idCategoria'))
    titulo = Column(String(100))
    descricao = Column(Text)
    preco = Column(DECIMAL(10,2))
    cidade = Column(String(100))
    status = Column(Enum('ativo', 'inativo'))
    dataCriacao = Column(DateTime, default=datetime.utcnow)
    usuario = relationship('Usuario', back_populates='servicos')
    categoria = relationship('Categoria', back_populates='servicos')
    transacoes = relationship('Transacao', back_populates='servico')

class Transacao(Base):
    __tablename__ = "Transacoes"

    idTransacao = Column(Integer, primary_key=True, index=True)
    idServico = Column(Integer, ForeignKey('Servicos.idServico'))
    idCliente = Column(Integer, ForeignKey('Usuarios.idUsuario'))
    dataSolicitacao = Column(DateTime, default=datetime.utcnow)
    valorPago = Column(DECIMAL(10,2))
    status = Column(Enum('pendente', 'em_andamento', 'concluido', 'cancelado'))
    avaliacao = Column(Integer)
    servico = relationship('Servico', back_populates='transacoes')
    cliente = relationship('Usuario', back_populates='transacoes_cliente', foreign_keys=[idCliente])