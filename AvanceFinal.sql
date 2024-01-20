-- ===========================REPORTES============================
-- Detalles del pedido y  Calificacion del Repartidor
CREATE VIEW DetallesPedidoCalificacion AS
SELECT P.numpedido AS NumeroPedido, P.estado AS Estado, P.precio as Precio, C.direccion as Direccion, C.fecha_nacimiento AS FechaNacimiento, R.calificacion as Calificacion
FROM Pedido P
JOIN Cliente C ON P.telefono = C.telefono
JOIN Repartidor R ON P.cedula = R.cedula;


-- Historial de Compras con Detalle del Producto
CREATE VIEW HistorialCompras AS
SELECT C.Telefono, C.email AS Correo, P.numpedido, P.estado, PR.nombre AS NombreProducto, PR.precio
FROM Cliente C
JOIN Pedido P ON C.Telefono = P.telefono
JOIN Producto PR ON P.idproducto = PR.idproducto;


-- Pedidos Pendientes con Detalles de Establecimiento y Cliente
CREATE VIEW PedidosPendientes AS
SELECT P.numpedido, P.estado, E.ubicacion, E.tipoEstablecimiento, C.direccion, C.fecha_nacimiento
FROM Pedido P
JOIN Establecimiento E ON P.establecimiento = E.idEstablecimiento
JOIN Cliente C ON P.telefono = C.telefono
WHERE P.estado = 'Pendiente';



-- Pedidos Cancelados
CREATE VIEW PedidosCancelados AS
SELECT P.numpedido, C.motivo, C.estadoDelPedido, Cl.direccion, Cl.fecha_nacimiento
FROM Pedido P
JOIN Cancelacion C ON P.numpedido = C.numpedido
JOIN Cliente Cl ON P.telefono = Cl.telefono
WHERE C.estadoDelPedido = 'Cancelado';


SELECT * FROM DetallesPedidoCalificacion;
SELECT * FROM HistorialCompras;
SELECT * FROM PedidosPendientes;
SELECT * FROM PedidosCancelados;


-- ===========================TRIGGERS============================



