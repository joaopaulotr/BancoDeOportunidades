CREATE SCHEMA BancoOportunidades CHARACTER SET utf8mb4;
USE BancoOportunidades;

CREATE TABLE Usuarios (

	idUsuario INT AUTO_INCREMENT PRIMARY KEY,
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

	idCategoria int not null auto_increment primary key,
	nomeCategoria varchar (100),
    descricaoCategoria varchar (255)
    
);

CREATE TABLE Servicos (

  idServico INT AUTO_INCREMENT PRIMARY KEY,
  idUsuario INT,
  idCategoria INT,
  titulo VARCHAR(100),
  descricao TEXT,
  preco DECIMAL(10,2),
  cidade VARCHAR(100),
  status ENUM('ativo','inativo'),
  dataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (idUsuario) REFERENCES Usuarios(idUsuario),
  FOREIGN KEY (idCategoria) REFERENCES Categorias(idCategoria)
  
);

CREATE TABLE Transacoes (

  idTransacao INT AUTO_INCREMENT PRIMARY KEY,
  idServico INT,
  idCliente INT,
  dataSolicitacao DATETIME DEFAULT CURRENT_TIMESTAMP,
  valorPago DECIMAL(10,2),
  status ENUM('pendente','em_andamento','concluido','cancelado'),
  avaliacao INT,
  FOREIGN KEY (idServico) REFERENCES Servicos(idServico),
  FOREIGN KEY (idCliente) REFERENCES Usuarios(idUsuario)
  
);



