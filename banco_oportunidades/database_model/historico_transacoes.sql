-- Mostrar ao cliente os serviços que ele já contratou, com o nome do prestador e status.

SET @idCliente = 2;

SELECT 
    t.idTransacoes,
    s.titulo AS servico,
    u.nome AS prestador,
    t.valorPago,
    t.status,
    t.dataSolicitacao
FROM Transacoes AS t
INNER JOIN Servicos AS s ON t.Servicos_idServicos = s.idServicos
INNER JOIN Usuarios AS u ON t.Usuarios_idUsuarios = u.idUsuarios
WHERE t.Usuarios_idUsuarios = @idCliente;
