CREATE SCHEMA BancoOportunidades;
USE BancoOportunidades;

CREATE TABLE Usuarios (
    idUsuarios INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha_hash VARCHAR(255),
    cpf_cnpj VARCHAR(20),
    tipoUsuario ENUM('prestador','cliente','admin'),
    telefone VARCHAR(20),
    endereco VARCHAR(255),
    cidade VARCHAR(100),
    uf CHAR(2),
    dataCadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Categorias (
    idCategorias INT AUTO_INCREMENT PRIMARY KEY,
    nomeCategoria VARCHAR(100),
    descricaoCategoria VARCHAR(255)
);

CREATE TABLE Servicos (
    idServicos INT AUTO_INCREMENT PRIMARY KEY,
    Categorias_idCategorias INT,
    titulo VARCHAR(100),
    descricao TEXT,
    preco DECIMAL(10,2),
    cidade VARCHAR(100),
    status ENUM('ativo','inativo'),
    dataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Categorias_idCategorias) REFERENCES Categorias(idCategorias)
);

CREATE TABLE Transacoes (
    idTransacoes INT AUTO_INCREMENT PRIMARY KEY,
    Usuarios_idUsuarios INT,
    Servicos_idServicos INT,
    dataSolicitacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    valorPago DECIMAL(10,2),
    status ENUM('pendente','em_andamento','concluido','cancelado'),
    avaliacao INT,
    FOREIGN KEY (Usuarios_idUsuarios) REFERENCES Usuarios(idUsuarios),
    FOREIGN KEY (Servicos_idServicos) REFERENCES Servicos(idServicos)
);
