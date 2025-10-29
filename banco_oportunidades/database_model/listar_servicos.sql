-- Mostrar na tela todos os serviços disponíveis com o nome do profissional e a categoria a que pertencem.

SELECT 
	s.idServico,
	s.titulo,
	s.descricao,
	s.preco,
	u.nome AS prestador,
	c.nomeCategoria AS categoria
 FROM Servicos as s
INNER JOIN Usuarios as u on s.idUsuario = u.idUsuario
INNER JOIN Categorias as c on s.idCategoria = c.idCategoria
WHERE s.status = 'ativo';