SET @idUsuario = 1;

SELECT 
    s.idServicos,
    s.titulo,
    s.preco,
    c.nomeCategoria,
    s.status
FROM Servicos AS s
LEFT JOIN Categorias AS c ON s.Categorias_idCategorias = c.idCategorias
INNER JOIN Transacoes AS t ON s.idServicos = t.Servicos_idServicos
WHERE t.Usuarios_idUsuarios = @idUsuario;