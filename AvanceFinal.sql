-- ===========================CREACION DE USUARIOS============================
CREATE USER 'usuario1'@'localhost' IDENTIFIED BY '12345';
CREATE USER 'usuario2'@'localhost' IDENTIFIED BY '67890';
CREATE USER 'usuario3'@'localhost' IDENTIFIED BY '24680';
CREATE USER 'usuario4'@'localhost' IDENTIFIED BY '13579';
CREATE USER 'usuario5'@'localhost' IDENTIFIED BY '11235';

-- ===========================OTORGAR PERMISOS ============================
GRANT SELECT, INSERT, UPDATE, DELETE ON pedidosya.* TO 'usuario1'@'localhost';
GRANT SELECT, INSERT, DELETE ON pedidosya.* TO 'usuario2'@'localhost';
GRANT SELECT ON pedidosya.* TO 'usuario3'@'localhost';
GRANT INSERT, UPDATE ON pedidosya.* TO 'usuario4'@'localhost';
GRANT SELECT ON pedidosya.* TO 'usuario5'@'localhost';

-- ===========================PERMISOS A VISTAS============================
GRANT SELECT ON pedidosya.HistorialCompras TO 'usuario3'@'localhost';
GRANT SELECT ON pedidosya.PedidosCancelados TO 'usuario3'@'localhost';

-- ============================PERMISO A STORED PROCEDURE============================
GRANT EXECUTE ON PROCEDURE pedidosya.sp_agregar_cliente TO 'usuario5'@'localhost';
GRANT EXECUTE ON PROCEDURE pedidosya.sp_consultar_cliente TO 'usuario5'@'localhost';

-- =====================================INDICES======================================
CREATE INDEX idx_pedidos_fecha ON Pedido(fecha_pedido);Este índice acelera las consultas que buscan pedidos por fecha, optimiza las operaciones de ordenamiento y agrupación por fecha, y facilita la verificación de fechas duplicadas.
CREATE INDEX idx_pedido_numero ON Pedido(numeroPedido);Este índice puede acelerar las consultas que buscan información específica de un pedido, ya que numeroPedido es una clave primaria.
CREATE INDEX idx_cliente_telefono ON Cliente(Telefono);Dado que el teléfono se utiliza para unir las tablas Cliente y Pedido, un índice aquí mejorará la eficiencia de estas operaciones JOIN.
CREATE INDEX idx_producto_id ON Producto(idproducto);Este índice facilitará las consultas rápidas para obtener detalles específicos del producto.
CREATE INDEX idx_repartidor_cedula ON Repartidor(cedula);Este índice acelerará las consultas relacionadas con los repartidores, especialmente útil si se realizan búsquedas frecuentes o filtrados basados en la cédula del repartidor.
CREATE INDEX idx_establecimiento_id ON Establecimiento(idEstablecimiento);Este índice puede ser útil para recuperar rápidamente información sobre un establecimiento específico.

-- ===========================TRIGGER============================
-- TRIGGER PARA INSERTAR EN PEDIDO --
DELIMITER //
CREATE TRIGGER after_pedido_insert
AFTER INSERT ON Pedido
FOR EACH ROW
BEGIN
    
    UPDATE Pedido SET estado = 'Pendiente' WHERE numpedido = NEW.numpedido;
END;
//
DELIMITER ;

-- TRIGGER PARA ACTUALIZAR EN PRODUCTO --
DELIMITER //
CREATE TRIGGER after_producto_update
AFTER UPDATE ON Producto
FOR EACH ROW
BEGIN
    
    UPDATE Producto SET descripcion = CONCAT(descripcion, ' - Precio actualizado') WHERE idproducto = NEW.idproducto;
END;
//
DELIMITER ;

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








-- =========================PROCEDURE===============================
-- =================================================================
-- ======================TABLA CALIFICACION=========================
-- =================================================================
-- Agregar calificacion
DELIMITER //
CREATE PROCEDURE Agregar_calificacion(
    IN p_idpedido INT,
    IN p_calificacionEstablecimiento INT,
    IN p_calificacionRepartidor INT,
    IN p_calificacionProducto INT,
    IN p_numpedido INT
)
BEGIN
    DECLARE existe_registro INT;


    SELECT COUNT(*) INTO existe_registro FROM CALIFICACION WHERE idpedido = p_idpedido AND numpedido = p_numpedido;
    IF existe_registro > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Entrada duplicada para el ID y número de pedido especificados';
    ELSE
        -- Insertar datos
        INSERT INTO CALIFICACION VALUES (p_idpedido, p_calificacionEstablecimiento, p_calificacionRepartidor, p_calificacionProducto, p_numpedido);
        COMMIT;
    END IF;
END //
DELIMITER ;
-- Consultar calificacion
DELIMITER //
CREATE PROCEDURE Consultar_calificacion(
    IN p_idpedido INT
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM CALIFICACION WHERE idpedido = p_idpedido;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID de pedido especificado';
    ELSE
        SELECT * FROM CALIFICACION WHERE idpedido = p_idpedido;
    END IF;
END //
DELIMITER ;

-- Actualizar calificacion
DELIMITER //
CREATE PROCEDURE Actualizar_calificacion(
    IN p_idpedido INT,
    IN p_nueva_calificacionEstablecimiento VARCHAR(250),
    IN p_nueva_calificacionRepartidor VARCHAR(250),
    IN p_nueva_calificacionProducto VARCHAR(250)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM CALIFICACION WHERE idpedido = p_idpedido;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID de pedido especificado';
    ELSE
        UPDATE CALIFICACION
        SET calificacionEstablecimiento = p_nueva_calificacionEstablecimiento,
            calificacionRepartidor = p_nueva_calificacionRepartidor,
            calificacionProducto = p_nueva_calificacionProducto
        WHERE idpedido = p_idpedido;
        COMMIT;
    END IF;
END //
DELIMITER ;
-- Procedimiento para actualizar la calificación del repartidor
DELIMITER //
CREATE PROCEDURE Actualizar_calificacion_repartidor(IN idpedido_param INT, IN nueva_calificacion_param VARCHAR(255))
BEGIN
    UPDATE CALIFICACION SET calificacionRepartidor = nueva_calificacion_param WHERE idpedido = idpedido_param;
END //
DELIMITER ;
-- Procedimiento para actualizar la calificación del establecimiento
DELIMITER //
CREATE PROCEDURE Actualizar_calificacion_establecimiento(IN idpedido_param INT, IN nueva_calificacion_param VARCHAR(255))
BEGIN
    UPDATE CALIFICACION SET calificacionEstablecimiento = nueva_calificacion_param WHERE idpedido = idpedido_param;
END //
DELIMITER ;

-- Procedimiento para actualizar la calificación del producto
DELIMITER //
CREATE PROCEDURE Actualizar_calificacion_producto(IN idpedido_param INT, IN nueva_calificacion_param VARCHAR(255))
BEGIN
    UPDATE CALIFICACION SET calificacionProducto = nueva_calificacion_param WHERE idpedido = idpedido_param;
END //
DELIMITER ;




-- Eliminar Calificación desactivando restricciones de clave foránea
DELIMITER //
CREATE PROCEDURE Eliminar_calificacion(
    IN p_id_pedido INT
)
BEGIN
    -- Desactivar restricciones de clave foránea
    SET foreign_key_checks = 0;

    -- Eliminar la calificación
    DELETE FROM Calificacion WHERE idpedido = p_id_pedido;

    -- Activar restricciones de clave foránea nuevamente
    SET foreign_key_checks = 1;

    COMMIT;
END //
DELIMITER ;

-- =================================================================
-- ======================TABLA CLIENTE==============================
-- =================================================================

-- Agregar Cliente
DELIMITER //
CREATE PROCEDURE sp_agregar_cliente(
    IN p_telefono INT,
    IN p_email VARCHAR(255),
    IN p_fecha_nacimiento DATE,
    IN p_cedula VARCHAR(20),
    IN p_direccion VARCHAR(255),
    IN p_edad INT,
    IN p_numpedido INT,
    IN p_id_empleado INT
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Cliente WHERE Telefono = p_telefono AND numpedido = p_numpedido;
    IF existe_registro > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Entrada duplicada para el número de teléfono y número de pedido especificados';
    ELSE
        -- Insertar datos
        INSERT INTO Cliente (Telefono, email, fecha_nacimiento, cedula, direccion, edad, numpedido, id_empleado)
        VALUES (p_telefono, p_email, p_fecha_nacimiento, p_cedula, p_direccion, p_edad, p_numpedido, p_id_empleado);
        COMMIT;
    END IF;
END //
DELIMITER ;

-- Consultar Cliente
DELIMITER //
CREATE PROCEDURE sp_consultar_cliente(
    IN p_telefono INT
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Cliente WHERE Telefono = p_telefono;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el número de teléfono especificado';
    ELSE
        SELECT * FROM Cliente WHERE Telefono = p_telefono;
    END IF;
END //
DELIMITER ;

-- Actualizar Cliente
DELIMITER //
CREATE PROCEDURE sp_actualizar_cliente(
    IN p_telefono VARCHAR(15),
    IN p_nueva_email VARCHAR(255),
    IN p_nueva_fecha_nacimiento DATE,
    IN p_nueva_cedula VARCHAR(15),
    IN p_nueva_direccion VARCHAR(255),
    IN p_nueva_edad INT,
    IN p_nuevo_numpedido VARCHAR(250),
    IN p_nuevo_id_empleado VARCHAR(250)
)
BEGIN
    DECLARE v_email VARCHAR(255);
    DECLARE v_fecha_nacimiento DATE;
    DECLARE v_cedula VARCHAR(15);
    DECLARE v_direccion VARCHAR(255);
    DECLARE v_edad INT;
    DECLARE v_numpedido VARCHAR(250);
    DECLARE v_id_empleado VARCHAR(250);

    SELECT email, fecha_nacimiento, cedula, direccion, edad, numpedido, id_empleado
    INTO v_email, v_fecha_nacimiento, v_cedula, v_direccion, v_edad, v_numpedido, v_id_empleado
    FROM Cliente
    WHERE Telefono = p_telefono;

    IF v_email IS NOT NULL AND p_nueva_email IS NOT NULL THEN
        SET v_email = p_nueva_email;
    END IF;
    IF p_nueva_fecha_nacimiento IS NOT NULL THEN
        SET v_fecha_nacimiento = p_nueva_fecha_nacimiento;
    END IF;
    IF v_cedula IS NOT NULL AND p_nueva_cedula IS NOT NULL THEN
        SET v_cedula = p_nueva_cedula;
    END IF;
    IF v_direccion IS NOT NULL AND p_nueva_direccion IS NOT NULL THEN
        SET v_direccion = p_nueva_direccion;
    END IF;
    IF v_edad IS NOT NULL AND p_nueva_edad IS NOT NULL THEN
        SET v_edad = p_nueva_edad;
    END IF;
    IF v_numpedido IS NOT NULL AND p_nuevo_numpedido IS NOT NULL THEN
        SET v_numpedido = p_nuevo_numpedido;
    END IF;

    IF p_nuevo_id_empleado IS NOT NULL THEN
        SET v_id_empleado = p_nuevo_id_empleado;
    ELSE
        SET v_id_empleado = NULL;
    END IF;

    UPDATE Cliente
    SET email = v_email,
        fecha_nacimiento = v_fecha_nacimiento,
        cedula = v_cedula,
        direccion = v_direccion,
        edad = v_edad,
        numpedido = v_numpedido,
        id_empleado = v_id_empleado
    WHERE Telefono = p_telefono;
END //
DELIMITER ;


-- Eliminar Cliente desactivando restricciones de clave foránea
DELIMITER //
CREATE PROCEDURE sp_eliminar_cliente(
    IN p_telefono INT
)
BEGIN
    -- Desactivar restricciones de clave foránea
    SET foreign_key_checks = 0;

    -- Eliminar al cliente
    DELETE FROM Cliente WHERE Telefono = p_telefono;

    -- Activar restricciones de clave foránea nuevamente
    SET foreign_key_checks = 1;

    COMMIT;
END //
DELIMITER ;


-- =================================================================
-- ======================TABLA ESTABLECIMIENTO======================
-- =================================================================

-- Agregar Establecimiento
DELIMITER //
CREATE PROCEDURE sp_agregar_establecimiento(
    IN p_idEstablecimiento VARCHAR(255),
    IN p_numpedido INT,
    IN p_ubicacion VARCHAR(255),
    IN p_calificacion INT,
    IN p_distancia INT,
    IN p_telefono VARCHAR(20),
    IN p_tipoEstablecimiento VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Establecimiento WHERE idEstablecimiento = p_idEstablecimiento AND numpedido = p_numpedido;
    IF existe_registro > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Entrada duplicada para el ID del establecimiento y número de pedido especificados';
    ELSE
        -- Insertar datos
        INSERT INTO Establecimiento (idEstablecimiento, numpedido, ubicacion, calificacion, distancia, telefono, tipoEstablecimiento)
        VALUES (p_idEstablecimiento, p_numpedido, p_ubicacion, p_calificacion, p_distancia, p_telefono, p_tipoEstablecimiento);
        COMMIT;
    END IF;
END //
DELIMITER ;
-- Consultar Establecimiento
DELIMITER //
CREATE PROCEDURE sp_consultar_establecimiento(
    IN p_idEstablecimiento VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Establecimiento WHERE idEstablecimiento = p_idEstablecimiento;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID del establecimiento especificado';
    ELSE
        SELECT * FROM Establecimiento WHERE idEstablecimiento = p_idEstablecimiento;
    END IF;
END //
DELIMITER ;

-- Actualizar Establecimiento
DELIMITER //
CREATE PROCEDURE sp_actualizar_establecimiento(
    IN p_idEstablecimiento VARCHAR(255),
    IN p_numpedido INT,
    IN p_nueva_ubicacion VARCHAR(255),
    IN p_nueva_calificacion INT,
    IN p_nueva_distancia INT,
    IN p_nuevo_telefono VARCHAR(20),
    IN p_nuevo_tipoEstablecimiento VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Establecimiento WHERE idEstablecimiento = p_idEstablecimiento;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID del establecimiento especificado';
    ELSE
        UPDATE Establecimiento
        SET ubicacion = COALESCE(p_nueva_ubicacion, ubicacion),
            calificacion = COALESCE(p_nueva_calificacion, calificacion),
            distancia = COALESCE(p_nueva_distancia, distancia),
            telefono = COALESCE(p_nuevo_telefono, telefono),
            tipoEstablecimiento = COALESCE(p_nuevo_tipoEstablecimiento, tipoEstablecimiento)
        WHERE idEstablecimiento = p_idEstablecimiento;
        COMMIT;
    END IF;
END //
DELIMITER ;

-- Eliminar Establecimiento
DELIMITER //
CREATE PROCEDURE sp_eliminar_establecimiento(
    IN p_idEstablecimiento VARCHAR(255)
)
BEGIN
    -- Desactivar restricciones de clave foránea temporalmente
    SET foreign_key_checks = 0;

    -- Eliminar el establecimiento
    DELETE FROM Establecimiento WHERE idEstablecimiento = p_idEstablecimiento;
    COMMIT;

    -- Activar restricciones de clave foránea nuevamente
    SET foreign_key_checks = 1;
END //
DELIMITER ;


-- ================================================================
-- ======================TABLA METODO_DE_PAGO======================
-- ================================================================
-- Agregar Método de Pago
DELIMITER //
CREATE PROCEDURE sp_agregar_metodo_pago(
    IN p_IDmetodoPago VARCHAR(255),
    IN p_idcliente VARCHAR(255),
    IN p_NumPedido INT,
    IN p_tipo_tarjeta VARCHAR(20),
    IN p_numTarjeta VARCHAR(20),
    IN p_apodo VARCHAR(255),
    IN p_fechaExpi DATE
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM MetodoDePago WHERE IDmetodoPago = p_IDmetodoPago;
    IF existe_registro > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Entrada duplicada para el ID del método de pago especificado';
    ELSE
        -- Insertar datos en la tabla MétodoDePago
        INSERT INTO MetodoDePago (IDmetodoPago, idcliente, NumPedido) VALUES (p_IDmetodoPago, p_idcliente, p_NumPedido);

        -- Insertar datos en la tabla correspondiente según el tipo de tarjeta
        IF p_tipo_tarjeta = 'debito' THEN
            INSERT INTO TarjetaDebito (IDmetodoPago, numTarjeta, apodo, FechaExpi) VALUES (p_IDmetodoPago, p_numTarjeta, p_apodo, p_fechaExpi);
        ELSEIF p_tipo_tarjeta = 'credito' THEN
            INSERT INTO TarjetaCredito (IDmetodoPago, numTarjeta, apodo, FechaExpi) VALUES (p_IDmetodoPago, p_numTarjeta, p_apodo, p_fechaExpi);
        END IF;

        COMMIT;
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_consultar_metodo_pago(
    IN p_IDmetodoPago VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM MetodoDePago WHERE IDmetodoPago = p_IDmetodoPago;
    
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID del método de pago especificado';
    ELSE
        -- Consultar información de MétodoDePago y tarjetas vinculadas
        SELECT mp.*, td.numTarjeta AS tarjetaDebito, tc.numTarjeta AS tarjetaCredito
        FROM MetodoDePago mp
        LEFT JOIN TarjetaDebito td ON mp.IDmetodoPago = td.IDmetodoPago
        LEFT JOIN TarjetaCredito tc ON mp.IDmetodoPago = tc.IDmetodoPago
        WHERE mp.IDmetodoPago = p_IDmetodoPago;
    END IF;
END //

DELIMITER ;

-- ACTUALIZA METODO DE PAGO

DELIMITER //
CREATE PROCEDURE sp_actualizar_metodo_pago(
    IN p_IDmetodoPago VARCHAR(255),
    IN p_nuevo_idcliente VARCHAR(255),
    IN p_nuevo_NumPedido INT,
    IN p_tipo_tarjeta VARCHAR(20),
    IN p_nuevo_numTarjeta VARCHAR(20),
    IN p_nuevo_apodo VARCHAR(255),
    IN p_nueva_fechaExpi DATE
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM MetodoDePago WHERE IDmetodoPago = p_IDmetodoPago;
    
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID del método de pago especificado';
    ELSE
        -- Actualizar datos en la tabla MétodoDePago
        UPDATE MetodoDePago
        SET idcliente = COALESCE(p_nuevo_idcliente, idcliente),
            NumPedido = COALESCE(p_nuevo_NumPedido, NumPedido)
        WHERE IDmetodoPago = p_IDmetodoPago;

        -- Actualizar datos en la tabla correspondiente según el tipo de tarjeta
        IF p_tipo_tarjeta = 'debito' THEN
            UPDATE TarjetaDebito
            SET numTarjeta = COALESCE(p_nuevo_numTarjeta, numTarjeta),
                apodo = COALESCE(p_nuevo_apodo, apodo),
                FechaExpi = COALESCE(p_nueva_fechaExpi, FechaExpi)
            WHERE IDmetodoPago = p_IDmetodoPago;
        ELSEIF p_tipo_tarjeta = 'credito' THEN
            UPDATE TarjetaCredito
            SET numTarjeta = COALESCE(p_nuevo_numTarjeta, numTarjeta),
                apodo = COALESCE(p_nuevo_apodo, apodo),
                FechaExpi = COALESCE(p_nueva_fechaExpi, FechaExpi)
            WHERE IDmetodoPago = p_IDmetodoPago;
        END IF;

        COMMIT;
    END IF;
END //

DELIMITER ;






-- Eliminar Método de Pago 
DELIMITER //
CREATE PROCEDURE sp_eliminar_metodo_pago(
    IN p_IDmetodoPago VARCHAR(255)
)
BEGIN
    -- Eliminar tarjetas vinculadas (si existen)
    DELETE FROM TarjetaDebito WHERE IDmetodoPago = p_IDmetodoPago;
    DELETE FROM TarjetaCredito WHERE IDmetodoPago = p_IDmetodoPago;

    -- Eliminar entrada en la tabla MétodoDePago sin restricciones de clave foránea
    DELETE FROM MetodoDePago WHERE IDmetodoPago = p_IDmetodoPago;

    COMMIT;
END //
DELIMITER ;




-- ============================================================
-- ======================TABLA PRODUCTO========================
-- ============================================================

-- Agregar Producto
DELIMITER //
CREATE PROCEDURE sp_agregar_producto(
    IN p_idproducto VARCHAR(255),
    IN p_nombre VARCHAR(255),
    IN p_foto LONGBLOB,
    IN p_precio DECIMAL(10, 2),
    IN p_descripcion TEXT,
    IN p_descuento DECIMAL(5, 2),
    IN p_idEstablecimiento VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Producto WHERE idproducto = p_idproducto;
    IF existe_registro > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Entrada duplicada para el ID del producto especificado';
    ELSE
        INSERT INTO Producto (idproducto, nombre, foto, precio, descripcion, descuento, idEstablecimiento) VALUES (p_idproducto, p_nombre, p_foto, p_precio, p_descripcion, p_descuento, p_idEstablecimiento);
        COMMIT;
    END IF;
END //
DELIMITER ;

-- Consultar Producto
DELIMITER //
CREATE PROCEDURE sp_consultar_producto(
    IN p_idproducto VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Producto WHERE idproducto = p_idproducto;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID del producto especificado';
    ELSE
        SELECT * FROM Producto WHERE idproducto = p_idproducto;
    END IF;
END //
DELIMITER ;





-- Actualizar Producto
DELIMITER //
CREATE PROCEDURE sp_actualizar_producto(
    IN p_idproducto VARCHAR(255),
    IN p_nuevo_nombre VARCHAR(255),
    IN p_nueva_foto LONGBLOB,
    IN p_nuevo_precio DECIMAL(10, 2),
    IN p_nueva_descripcion TEXT,
    IN p_nuevo_descuento DECIMAL(5, 2),
    IN p_nuevo_idEstablecimiento VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Producto WHERE idproducto = p_idproducto;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID del producto especificado';
    ELSE
        UPDATE Producto
        SET
            nombre = IF(CHAR_LENGTH(p_nuevo_nombre) > 0, p_nuevo_nombre, nombre),
            foto = IF(CHAR_LENGTH(p_nueva_foto) > 0, p_nueva_foto, foto),
            precio = IF(p_nuevo_precio IS NOT NULL, p_nuevo_precio, precio),
            descripcion = IF(CHAR_LENGTH(p_nueva_descripcion) > 0, p_nueva_descripcion, descripcion),
            descuento = IF(p_nuevo_descuento IS NOT NULL, p_nuevo_descuento, descuento),
            idEstablecimiento = IF(CHAR_LENGTH(p_nuevo_idEstablecimiento) > 0, p_nuevo_idEstablecimiento, idEstablecimiento)
        WHERE idproducto = p_idproducto;

        COMMIT;
    END IF;
END //
DELIMITER ;




-- Eliminar Producto 
DELIMITER //
CREATE PROCEDURE sp_eliminar_producto(
    IN p_idproducto VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    -- Desactivar temporalmente las restricciones de clave foránea
    SET foreign_key_checks = 0;

    SELECT COUNT(*) INTO existe_registro FROM Producto WHERE idproducto = p_idproducto;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para el ID del producto especificado';
    ELSE
        DELETE FROM Producto WHERE idproducto = p_idproducto;
        COMMIT;
    END IF;

    -- Restaurar las restricciones de clave foránea
    SET foreign_key_checks = 1;
END //
DELIMITER ;

-- ============================================================
-- ======================TABLA REPARTIDOR======================
-- ============================================================
-- Agregar Repartidor
DELIMITER //
CREATE PROCEDURE sp_agregar_repartidor(
    IN p_cedula VARCHAR(255),
    IN p_nombre VARCHAR(255),
    IN p_telefono VARCHAR(255),
    IN p_calificacion DECIMAL(3, 2),
    IN p_fechanacimiento DATE,
    IN p_email VARCHAR(255),
    IN p_numpedido VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Repartidor WHERE cedula = p_cedula;
    IF existe_registro > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Entrada duplicada para la cédula del repartidor especificado';
    ELSE
        INSERT INTO Repartidor (cedula, nombre, telefono, calificacion, fechanacimiento, email, numpedido) VALUES (p_cedula, p_nombre, p_telefono, p_calificacion, p_fechanacimiento, p_email, p_numpedido);
        COMMIT;
    END IF;
END //
DELIMITER ;

-- Consultar Repartidor
DELIMITER //
CREATE PROCEDURE sp_consultar_repartidor(
    IN p_cedula VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Repartidor WHERE cedula = p_cedula;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para la cédula del repartidor especificado';
    ELSE
        SELECT * FROM Repartidor WHERE cedula = p_cedula;
    END IF;
END //
DELIMITER ;

-- Actualizar Repartidor
DELIMITER //
CREATE PROCEDURE sp_actualizar_repartidor(
    IN p_cedula VARCHAR(255),
    IN p_nuevo_nombre VARCHAR(255),
    IN p_nuevo_telefono VARCHAR(255),
    IN p_nueva_calificacion DECIMAL(3, 2),
    IN p_nueva_fechanacimiento DATE,
    IN p_nuevo_email VARCHAR(255),
    IN p_nuevo_numpedido VARCHAR(255)
)
BEGIN
    DECLARE existe_registro INT;

    SELECT COUNT(*) INTO existe_registro FROM Repartidor WHERE cedula = p_cedula;
    IF existe_registro = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se encontró la entrada para la cédula del repartidor especificado';
    ELSE
        UPDATE Repartidor
        SET nombre = COALESCE(p_nuevo_nombre, nombre),
            telefono = COALESCE(p_nuevo_telefono, telefono),
            calificacion = COALESCE(p_nueva_calificacion, calificacion),
            fechanacimiento = COALESCE(p_nueva_fechanacimiento, fechanacimiento),
            email = COALESCE(p_nuevo_email, email),
            numpedido = COALESCE(p_nuevo_numpedido, numpedido)
        WHERE cedula = p_cedula;

        COMMIT;
    END IF;
END //
DELIMITER ;


-- Eliminar Repartidor
DELIMITER //
CREATE PROCEDURE sp_eliminar_repartidor(
    IN p_cedula BIGINT
)
BEGIN
    -- Desactivar temporáneamente las restricciones de clave externa
    SET foreign_key_checks = 0;

    -- Eliminar todas las relaciones que dependen del repartidor
    DELETE FROM Pedido WHERE cedula = p_cedula;
    DELETE FROM CALIFICACION WHERE numpedido IN (SELECT numpedido FROM Pedido WHERE cedula = p_cedula);
    DELETE FROM MetodoDePago WHERE NumPedido IN (SELECT numpedido FROM Pedido WHERE cedula = p_cedula);

    -- Eliminar el repartidor
    DELETE FROM Repartidor WHERE cedula = p_cedula;

    -- Reactivar las restricciones de clave externa
    SET foreign_key_checks = 1;

    COMMIT;
END //
DELIMITER ;


