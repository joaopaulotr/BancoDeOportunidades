-- Mostrar ao cliente os serviços que ele já contratou, com o nome do prestador e status.

SET @idCliente = 2;

SELECT 
	 t.idTransacao,
	s.titulo AS servico,
	u.nome AS prestador,
	t.valorPago,
	t.status,
	t.dataSolicitacao
 FROM Transacoes as t
INNER JOIN Servicos as s on t.idServico = s.idServico
INNER JOIN Usuarios as u on s.idUsuario = u.idUsuario
WHERE t.idCliente = @idCliente;
