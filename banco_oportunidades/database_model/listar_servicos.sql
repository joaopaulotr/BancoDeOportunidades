-- Mostrar na tela inicial todos os serviços disponíveis com o nome do profissional e a categoria a que pertencem.

SELECT 
    s.idServicos,
    s.titulo,
    s.descricao,
    s.preco,
    u.nome AS prestador,
    c.nomeCategoria AS categoria
FROM Servicos AS s
INNER JOIN Categorias AS c ON s.Categorias_idCategorias = c.idCategorias
INNER JOIN Transacoes AS t ON s.idServicos = t.Servicos_idServicos
INNER JOIN Usuarios AS u ON t.Usuarios_idUsuarios = u.idUsuarios
WHERE s.status = 'ativo';
