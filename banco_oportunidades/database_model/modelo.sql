-- Script SQL para criação do banco de dados no MySQL Workbench.
CREATE DATABASE banco_oportunidades CHARACTER SET utf8mb4;
USE banco_oportunidades;

-- Tabela de usuários
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  cpf VARCHAR(11) UNIQUE,
  senha VARCHAR(255),
  tipo ENUM('prestador','cliente')
);

-- Tabela de categorias
CREATE TABLE categorias (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  descricao VARCHAR(255)
);

-- Tabela de serviços
CREATE TABLE servicos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100),
  descricao TEXT,
  valor DECIMAL(10,2),
  categoria_id INT,
  prestador_id INT,
  FOREIGN KEY (categoria_id) REFERENCES categorias(id),
  FOREIGN KEY (prestador_id) REFERENCES usuarios(id)
);

-- Tabela de transações
CREATE TABLE transacoes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  servico_id INT,
  valor DECIMAL(10,2),
  status ENUM('pendente','concluido','cancelado'),
  FOREIGN KEY (cliente_id) REFERENCES usuarios(id),
  FOREIGN KEY (servico_id) REFERENCES servicos(id)
);

-- Tabela de avaliações
CREATE TABLE avaliacoes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  transacao_id INT,
  nota INT,
  comentario TEXT,
  FOREIGN KEY (transacao_id) REFERENCES transacoes(id)
);
