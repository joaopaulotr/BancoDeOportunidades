-- Painel do prestador — mostrar todos os serviços cadastrados por ele.

SET @idUsuario = 1;

SELECT 
  s.idServico,
  s.titulo,
  s.preco,
  c.nomeCategoria,
  s.status
 FROM Servicos s
LEFT JOIN Categorias c ON s.idCategoria = c.idCategoria
WHERE s.idUsuario = @idUsuario; 