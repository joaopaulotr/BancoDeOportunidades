USE BancoOportunidades;

INSERT INTO Categorias (nomeCategoria, descricaoCategoria) VALUES
('Jardinagem', 'Serviços de manutenção de jardins, poda de árvores e gramados.'),
('Pintura', 'Pintura residencial, comercial e decorativa.'),
('Segurança', 'Serviços de vigilância e ronda em áreas residenciais.'),
('Costura', 'Conserto e confecção de roupas em geral.'),
('Limpeza', 'Serviços de limpeza doméstica e pós-obra.');


INSERT INTO Usuarios (nome, email, senha_hash, cpf_cnpj, tipoUsuario, telefone, endereco, cidade, uf)
VALUES
('Carlos da Silva', 'carlos@gmail.com', 'hash123', '12345678901', 'prestador', '11987654321', 'Rua das Flores, 100', 'Maringá', 'PR'),
('Maria Souza', 'maria@gmail.com', 'hash456', '23456789012', 'cliente', '44912345678', 'Av. Brasil, 200', 'Maringá', 'PR'),
('João Oliveira', 'joao@gmail.com', 'hash789', '34567890123', 'prestador', '44987654321', 'Rua das Palmeiras, 300', 'Sarandi', 'PR'),
('Ana Pereira', 'ana@gmail.com', 'hash321', '45678901234', 'cliente', '11999887766', 'Rua Central, 150', 'Maringá', 'PR'),
('Fernanda Lima', 'fernanda@gmail.com', 'hash654', '56789012345', 'prestador', '44991234567', 'Rua das Acácias, 50', 'Maringá', 'PR');


INSERT INTO Servicos (idUsuario, idCategoria, titulo, descricao, preco, cidade, status)
VALUES
(1, 1, 'Manutenção de Jardim', 'Poda de árvores, corte de grama e adubação mensal.', 150.00, 'Maringá', 'ativo'),
(3, 2, 'Pintura Residencial', 'Pintura completa de casas até 100m² com tinta fornecida.', 1200.00, 'Sarandi', 'ativo'),
(1, 5, 'Limpeza Pós-Obra', 'Serviço completo de limpeza após reforma ou construção.', 300.00, 'Maringá', 'ativo'),
(5, 4, 'Conserto de Roupas', 'Ajustes, bainhas e consertos diversos em roupas.', 50.00, 'Maringá', 'ativo'),
(3, 3, 'Ronda Noturna', 'Serviço de vigilância residencial das 22h às 6h.', 800.00, 'Maringá', 'ativo');


INSERT INTO Transacoes (idServico, idCliente, valorPago, status, avaliacao)
VALUES
(1, 2, 150.00, 'concluido', 5),
(2, 4, 1200.00, 'pendente', NULL),
(4, 2, 50.00, 'concluido', 4),
(5, 4, 800.00, 'em_andamento', NULL),
(3, 2, 300.00, 'cancelado', NULL);

SELECT * FROM Transacoes;
SELECT * FROM Servicos;
SELECT * FROM Usuarios;
SELECT * FROM Categorias;
