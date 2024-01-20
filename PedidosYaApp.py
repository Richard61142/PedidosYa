import mysql.connector

# Configurar la conexión a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********", #COLOCAR EL PASSWORD
    database="pedidosya"
)
cursor = connection.cursor()
print("Se ha conectado a la bases de datos con éxito!!")

def agregar_calificacion():
    idpedido = input("Ingrese el ID del pedido: ")
    calificacionEstablecimiento = input("Ingrese la calificación del establecimiento: ")
    calificacionRepartidor = input("Ingrese la calificación del repartidor: ")
    calificacionProducto = input("Ingrese la calificación del producto: ")
    numpedido = input("Ingrese el número del pedido: ")

    
    cursor.execute("INSERT INTO CALIFICACION VALUES (%s, %s, %s, %s, %s)", (idpedido, calificacionEstablecimiento, calificacionRepartidor, calificacionProducto, numpedido))
    connection.commit()
    print("Registro agregado exitosamente.")

def consultar_calificacion():
    idpedido = input("Ingrese el ID del pedido: ")
    numpedido = input("Ingrese el número del pedido: ")

    cursor.execute("SELECT * FROM CALIFICACION WHERE idpedido = %s AND numpedido = %s", (idpedido, numpedido))
    row = cursor.fetchone()

    if row:
        print("Calificación encontrada:")
        print("ID Pedido:", row[0])
        print("Calificación Establecimiento:", row[1])
        print("Calificación Repartidor:", row[2])
        print("Calificación Producto:", row[3])
        print("Número Pedido:", row[4])
    else:
        print("Calificación no encontrada.")

def actualizar_calificacion():
    idpedido = input("Ingrese el ID del pedido que desea actualizar: ")
    numpedido = input("Ingrese el número del pedido que desea actualizar: ")

    cursor.execute("SELECT * FROM CALIFICACION WHERE idpedido = %s AND numpedido = %s", (idpedido, numpedido))
    row = cursor.fetchone()

    if row:
        print("Calificación actual:")
        print("ID Pedido:", row[0])
        print("Calificación Establecimiento:", row[1])
        print("Calificación Repartidor:", row[2])
        print("Calificación Producto:", row[3])
        print("Número Pedido:", row[4])

        nueva_calificacionEstablecimiento = input("Ingrese la nueva calificación del establecimiento (presione Enter para dejar sin cambios): ")
        nueva_calificacionRepartidor = input("Ingrese la nueva calificación del repartidor (presione Enter para dejar sin cambios): ")
        nueva_calificacionProducto = input("Ingrese la nueva calificación del producto (presione Enter para dejar sin cambios): ")

        if nueva_calificacionEstablecimiento:
            row[1] = nueva_calificacionEstablecimiento
        if nueva_calificacionRepartidor:
            row[2] = nueva_calificacionRepartidor
        if nueva_calificacionProducto:
            row[3] = nueva_calificacionProducto

        # Utilizar %s como marcador de posición
        cursor.execute("UPDATE CALIFICACION SET calificacionEstablecimiento = %s, calificacionRepartidor = %s, calificacionProducto = %s WHERE idpedido = %s AND numpedido = %s",
                       (row[1], row[2], row[3], idpedido, numpedido))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Calificación no encontrada.")

def eliminar_calificacion():
    idpedido = input("Ingrese el ID del pedido que desea eliminar: ")
    numpedido = input("Ingrese el número del pedido que desea eliminar: ")

    cursor.execute("DELETE FROM CALIFICACION WHERE idpedido = %s AND numpedido = %s", (idpedido, numpedido))
    connection.commit()
    print("Registro eliminado exitosamente.")

def agregar_cliente():
    telefono = input("Ingrese el número de teléfono: ")
    email = input("Ingrese la dirección de correo electrónico: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    cedula = input("Ingrese el número de cédula: ")
    direccion = input("Ingrese la dirección: ")
    edad = input("Ingrese la edad: ")
    numpedido = input("Ingrese el número del pedido: ")
    id_empleado = input("Ingrese el ID del empleado (deje en blanco y presione Enter si no tiene ID empleado): ")
    
    
    cursor.execute("INSERT INTO Cliente (Telefono, email, fecha_nacimiento, cedula, direccion, edad, numpedido, id_empleado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (telefono, email, fecha_nacimiento, cedula, direccion, edad, numpedido, id_empleado if id_empleado.strip() != "" else None))
    connection.commit()
    print("Registro agregado exitosamente.")


def consultar_cliente():
    telefono = input("Ingrese el número de teléfono: ")
    numpedido = input("Ingrese el número del pedido: ")

    cursor.execute("SELECT * FROM Cliente WHERE Telefono = %s AND numpedido = %s",
                   (telefono, numpedido))
    row = cursor.fetchone()

    if row:
        print("Cliente encontrado:")
        print("Teléfono:", row[0])
        print("Email:", row[1])
        print("Fecha de Nacimiento:", row[2])
        print("Cédula:", row[3])
        print("Dirección:", row[4])
        print("Edad:", row[5])
        print("Número Pedido:", row[6])
        print("ID Empleado:", row[7])
    else:
        print("Cliente no encontrado.")

def actualizar_cliente():
    telefono = input("Ingrese el número de teléfono que desea actualizar: ")
    numpedido = input("Ingrese el número del pedido que desea actualizar: ")

    cursor.execute("SELECT * FROM Cliente WHERE Telefono = %s AND numpedido = %s",
                   (telefono, numpedido))
    row = cursor.fetchone()

    if row:
        print("Cliente actual:")
        print("Teléfono:", row[0])
        print("Email:", row[1])
        print("Fecha de Nacimiento:", row[2])
        print("Cédula:", row[3])
        print("Dirección:", row[4])
        print("Edad:", row[5])
        print("Número Pedido:", row[6])
        print("ID Empleado:", row[7])

        
        nueva_email = input("Ingrese el nuevo correo electrónico (presione Enter para dejar sin cambios): ")
        nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (presione Enter para dejar sin cambios): ")
        nueva_cedula = input("Ingrese la nueva cédula (presione Enter para dejar sin cambios): ")
        nueva_direccion = input("Ingrese la nueva dirección (presione Enter para dejar sin cambios): ")
        nueva_edad = input("Ingrese la nueva edad (presione Enter para dejar sin cambios): ")
        nuevo_numpedido = input("Ingrese el nuevo número del pedido (presione Enter para dejar sin cambios): ")
        nuevo_id_empleado = input("Ingrese el nuevo ID del empleado (presione Enter para dejar sin cambios): ")

        
        row = (
            row[0],  # Teléfono
            nueva_email if nueva_email else row[1],  # Email
            nueva_fecha_nacimiento if nueva_fecha_nacimiento else row[2],  # Fecha de Nacimiento
            nueva_cedula if nueva_cedula else row[3],  # Cédula
            nueva_direccion if nueva_direccion else row[4],  # Dirección
            nueva_edad if nueva_edad else row[5],  # Edad
            nuevo_numpedido if nuevo_numpedido else row[6],  # Número Pedido
            nuevo_id_empleado if nuevo_id_empleado else row[7]  # ID Empleado
        )

        cursor.execute("UPDATE Cliente SET email = %s, fecha_nacimiento = %s, cedula = %s, direccion = %s, edad = %s, numpedido = %s, id_empleado = %s WHERE Telefono = %s AND numpedido = %s",
                       (row[1], row[2], row[3], row[4], row[5], row[6], row[7], telefono, numpedido))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Cliente no encontrado.")

def eliminar_cliente():
    telefono = input("Ingrese el número de teléfono que desea eliminar: ")
    numpedido = input("Ingrese el número del pedido que desea eliminar: ")

    cursor.execute("DELETE FROM Cliente WHERE Telefono = %s AND numpedido = %s",
                   (telefono, numpedido))
    connection.commit()
    print("Registro eliminado exitosamente.")

def agregar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento: ")
    numpedido = input("Ingrese el número del pedido: ")
    ubicacion = input("Ingrese la ubicación: ")
    calificacion = input("Ingrese la calificación del establecimiento: ")
    distancia = input("Ingrese la distancia: ")
    telefono = input("Ingrese el número de teléfono: ")
    tipoEstablecimiento = input("Ingrese el tipo de establecimiento: ")

  
    cursor.execute("INSERT INTO Establecimiento (idEstablecimiento, numpedido, ubicacion, calificacion, distancia, telefono, tipoEstablecimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (idEstablecimiento, numpedido, ubicacion, calificacion, distancia, telefono, tipoEstablecimiento))
    connection.commit()
    print("Registro agregado exitosamente.")

def actualizar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento que desea actualizar: ")
    numpedido = input("Ingrese el número del pedido que desea actualizar: ")

    cursor.execute("SELECT * FROM Establecimiento WHERE idEstablecimiento = %s AND numpedido = %s",
                   (idEstablecimiento, numpedido))
    row = cursor.fetchone()

    if row:
        print("Establecimiento actual:")
        print("ID Establecimiento:", row[0])
        print("Número Pedido:", row[1])
        print("Ubicación:", row[2])
        print("Calificación:", row[3])
        print("Distancia:", row[4])
        print("Teléfono:", row[5])
        print("Tipo de Establecimiento:", row[6])

        nueva_ubicacion = input("Ingrese la nueva ubicación (presione Enter para dejar sin cambios): ")
        nueva_calificacion = input("Ingrese la nueva calificación (presione Enter para dejar sin cambios): ")
        nueva_distancia = input("Ingrese la nueva distancia (presione Enter para dejar sin cambios): ")

        while True:
            try:
                nuevo_telefono_input = input("Ingrese el nuevo número de teléfono (presione Enter para dejar sin cambios): ")
                nuevo_telefono = int(nuevo_telefono_input) if nuevo_telefono_input.strip() else None
                break
            except ValueError:
                print("Por favor, ingrese un valor entero para el número de teléfono.")

        nuevo_tipoEstablecimiento = input("Ingrese el nuevo tipo de establecimiento (presione Enter para dejar sin cambios): ")

        
        updated_row = (
            row[0],  # ID Establecimiento
            row[1],  # Número Pedido
            nueva_ubicacion if nueva_ubicacion else row[2],  # Nueva Ubicación o valor existente
            nueva_calificacion if nueva_calificacion else row[3],  # Nueva Calificación o valor existente
            nueva_distancia if nueva_distancia else row[4],  # Nueva Distancia o valor existente
            nuevo_telefono if nuevo_telefono is not None else row[5],  # Nuevo Teléfono o valor existente
            nuevo_tipoEstablecimiento if nuevo_tipoEstablecimiento else row[6],  # Nuevo Tipo de Establecimiento o valor existente
        )

       
        update_query = "UPDATE Establecimiento SET ubicacion = %s, calificacion = %s, distancia = %s, telefono = %s, tipoEstablecimiento = %s WHERE idEstablecimiento = %s AND numpedido = %s"
        cursor.execute(update_query, (updated_row[2], updated_row[3], updated_row[4], updated_row[5], updated_row[6], idEstablecimiento, numpedido))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Establecimiento no encontrado.")

def consultar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento: ")
    numpedido = input("Ingrese el número del pedido: ")

    cursor.execute("SELECT * FROM Establecimiento WHERE idEstablecimiento = %s AND numpedido = %s",
                   (idEstablecimiento, numpedido))
    row = cursor.fetchone()

    if row:
        print("Establecimiento encontrado:")
        print("ID Establecimiento:", row[0])
        print("Número Pedido:", row[1])
        print("Ubicación:", row[2])
        print("Calificación:", row[3])
        print("Distancia:", row[4])
        print("Teléfono:", row[5])
        print("Tipo de Establecimiento:", row[6])
    else:
        print("Establecimiento no encontrado.")



def actualizar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento que desea actualizar: ")
    numpedido = input("Ingrese el número del pedido que desea actualizar: ")

    cursor.execute("SELECT * FROM Establecimiento WHERE idEstablecimiento = %s AND numpedido = %s",
                   (idEstablecimiento, numpedido))
    row = cursor.fetchone()

    if row:
        print("Establecimiento actual:")
        print("ID Establecimiento:", row[0])
        print("Número Pedido:", row[1])
        print("Ubicación:", row[2])
        print("Calificación:", row[3])
        print("Distancia:", row[4])
        print("Teléfono:", row[5])
        print("Tipo de Establecimiento:", row[6])

        nueva_ubicacion = input("Ingrese la nueva ubicación (presione Enter para dejar sin cambios): ")
        nueva_calificacion = input("Ingrese la nueva calificación (presione Enter para dejar sin cambios): ")
        nueva_distancia = input("Ingrese la nueva distancia (presione Enter para dejar sin cambios): ")
        nuevo_telefono = input("Ingrese el nuevo número de teléfono (presione Enter para dejar sin cambios): ")
        nuevo_tipoEstablecimiento = input("Ingrese el nuevo tipo de establecimiento (presione Enter para dejar sin cambios): ")

        if nueva_ubicacion:
            row[2] = nueva_ubicacion
        if nueva_calificacion:
            row[3] = nueva_calificacion
        if nueva_distancia:
            row[4] = nueva_distancia
        if nuevo_telefono:
            row[5] = nuevo_telefono
        if nuevo_tipoEstablecimiento:
            row[6] = nuevo_tipoEstablecimiento

        cursor.execute("UPDATE Establecimiento SET ubicacion = %s, calificacion = %s, distancia = %s, telefono = %s, tipoEstablecimiento = %s WHERE idEstablecimiento = %s AND numpedido = %s",
                       (row[2], row[3], row[4], row[5], row[6], idEstablecimiento, numpedido))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Establecimiento no encontrado.")

def eliminar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento que desea eliminar: ")
    numpedido = input("Ingrese el número del pedido que desea eliminar: ")

    try:
        
        cursor.execute("DELETE FROM pedido WHERE idEstablecimiento = %s AND numpedido = %s",
                       (idEstablecimiento, numpedido))

        
        cursor.execute("DELETE FROM Establecimiento WHERE idEstablecimiento = %s AND numpedido = %s",
                       (idEstablecimiento, numpedido))

        connection.commit()
        print("Registro eliminado exitosamente.")
    except mysql.connector.Error as err:
        # Manejo de errores
        print(f"Error: {err}")
        connection.rollback()

def agregar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago: ")
    idcliente = input("Ingrese el ID del cliente: ")
    NumPedido = input("Ingrese el número del pedido: ")

    
    cursor.execute("INSERT INTO MetodoDePago (IDmetodoPago, idcliente, NumPedido) VALUES (%s, %s, %s)",
                   (IDmetodoPago, idcliente, NumPedido))
    connection.commit()
    print("Registro de método de pago agregado exitosamente.")

def consultar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago: ")

    cursor.execute("SELECT * FROM MetodoDePago WHERE IDmetodoPago = %s", (IDmetodoPago,))
    row = cursor.fetchone()

    if row:
        print("Método de pago encontrado:")
        print("ID Método de Pago:", row[0])
        print("ID Cliente:", row[1])
        print("Número del Pedido:", row[2])
    else:
        print("Método de pago no encontrado.")

def actualizar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago que desea actualizar: ")

    cursor.execute("SELECT * FROM MetodoDePago WHERE IDmetodoPago = %s", (IDmetodoPago,))
    row = cursor.fetchone()

    if row:
        print("Método de pago actual:")
        print("ID Método de Pago:", row[0])
        print("ID Cliente:", row[1])
        print("Número del Pedido:", row[2])

        nuevo_idcliente = input("Ingrese el nuevo ID del cliente (presione Enter para dejar sin cambios): ")
        nuevo_NumPedido = input("Ingrese el nuevo número del pedido (presione Enter para dejar sin cambios): ")

        if nuevo_idcliente:
            row[1] = nuevo_idcliente
        if nuevo_NumPedido:
            row[2] = nuevo_NumPedido

        cursor.execute("UPDATE MetodoDePago SET idcliente = %s, NumPedido = %s WHERE IDmetodoPago = %s",
                       (row[1], row[2], IDmetodoPago))
        connection.commit()
        print("Registro de método de pago actualizado exitosamente.")
    else:
        print("Método de pago no encontrado.")

def eliminar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago que desea eliminar: ")

    cursor.execute("DELETE FROM MetodoDePago WHERE IDmetodoPago = %s", (IDmetodoPago,))
    connection.commit()
    print("Registro de método de pago eliminado exitosamente.")

def agregar_producto():
    idproducto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    foto = input("Ingrese la ruta de la foto del producto (presione Enter si no hay foto): ")
    precio = input("Ingrese el precio del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    descuento = input("Ingrese el descuento del producto (presione Enter si no hay descuento): ")
    idEstablecimiento = input("Ingrese el ID del establecimiento: ")

    
    foto_blob = None
    if foto:
        with open(foto, "rb") as file:
            foto_blob = file.read()

    
    cursor.execute("INSERT INTO Producto (idproducto, nombre, foto, precio, descripcion, descuento, idEstablecimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (idproducto, nombre, foto_blob, precio, descripcion, descuento, idEstablecimiento))
    connection.commit()
    print("Registro agregado exitosamente.")

def consultar_producto():
    idproducto = input("Ingrese el ID del producto: ")

    cursor.execute("SELECT * FROM Producto WHERE idproducto = %s", (idproducto,))
    row = cursor.fetchone()

    if row:
        print("Producto encontrado:")
        print("ID Producto:", row[0])
        print("Nombre:", row[1])
        print("Foto:", "Foto disponible" if row[2] else "No hay foto")
        print("Precio:", row[3])
        print("Descripción:", row[4])
        print("Descuento:", row[5] if row[5] else "No hay descuento")
        print("ID Establecimiento:", row[6])
    else:
        print("Producto no encontrado.")

def actualizar_producto():
    idproducto = input("Ingrese el ID del producto que desea actualizar: ")

    cursor.execute("SELECT * FROM Producto WHERE idproducto = %s", (idproducto,))
    row = cursor.fetchone()

    if row:
        print("Producto actual:")
        print("ID Producto:", row[0])
        print("Nombre:", row[1])
        print("Foto:", "Foto disponible" if row[2] else "No hay foto")
        print("Precio:", row[3])
        print("Descripción:", row[4])
        print("Descuento:", row[5] if row[5] else "No hay descuento")
        print("ID Establecimiento:", row[6])

        nuevo_nombre = input("Ingrese el nuevo nombre del producto (presione Enter para dejar sin cambios): ")
        nueva_foto = input("Ingrese la nueva ruta de la foto del producto (presione Enter para dejar sin cambios): ")
        nuevo_precio = input("Ingrese el nuevo precio del producto (presione Enter para dejar sin cambios): ")
        nueva_descripcion = input("Ingrese la nueva descripción del producto (presione Enter para dejar sin cambios): ")
        nuevo_descuento = input("Ingrese el nuevo descuento del producto (presione Enter para dejar sin cambios): ")
        nuevo_idEstablecimiento = input("Ingrese el nuevo ID del establecimiento (presione Enter para dejar sin cambios): ")

       
        nuevo_foto_blob = None
        if nueva_foto:
            with open(nueva_foto, "rb") as file:
                nuevo_foto_blob = file.read()

        if nuevo_nombre:
            row[1] = nuevo_nombre
        if nuevo_foto_blob:
            row[2] = nuevo_foto_blob
        if nuevo_precio:
            row[3] = nuevo_precio
        if nueva_descripcion:
            row[4] = nueva_descripcion
        if nuevo_descuento:
            row[5] = nuevo_descuento
        if nuevo_idEstablecimiento:
            row[6] = nuevo_idEstablecimiento

        cursor.execute("UPDATE Producto SET nombre = %s, foto = %s, precio = %s, descripcion = %s, descuento = %s, idEstablecimiento = %s WHERE idproducto = %s",
                       (row[1], row[2], row[3], row[4], row[5], row[6], idproducto))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    idproducto = input("Ingrese el ID del producto que desea eliminar: ")

    
    cursor.execute("UPDATE Producto SET disponible = FALSE WHERE idproducto = %s", (idproducto,))
    connection.commit()
    print("Producto marcado como no disponible exitosamente.")

def agregar_repartidor():
    cedula = input("Ingrese la cédula del repartidor: ")
    nombre = input("Ingrese el nombre del repartidor: ")
    telefono = input("Ingrese el número de teléfono del repartidor (presione Enter si no hay número de teléfono): ")
    calificacion = input("Ingrese la calificación del repartidor (presione Enter si no hay calificación): ")
    fechanacimiento = input("Ingrese la fecha de nacimiento del repartidor (YYYY-MM-DD): ")
    email = input("Ingrese el correo electrónico del repartidor (presione Enter si no hay correo electrónico): ")
    numpedido = input("Ingrese el número del pedido asignado al repartidor (presione Enter si no hay pedido asignado): ")

    cursor.execute("INSERT INTO Repartidor (cedula, nombre, telefono, calificacion, fechanacimiento, email, numpedido) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (cedula, nombre, telefono, calificacion, fechanacimiento, email, numpedido))
    connection.commit()
    print("Registro de repartidor agregado exitosamente.")

def agregar_repartidor():
    cedula = input("Ingrese la cédula del repartidor: ")
    nombre = input("Ingrese el nombre del repartidor: ")
    telefono = input("Ingrese el número de teléfono del repartidor (presione Enter si no hay número de teléfono): ")
    calificacion = input("Ingrese la calificación del repartidor (presione Enter si no hay calificación): ")
    fechanacimiento = input("Ingrese la fecha de nacimiento del repartidor (YYYY-MM-DD): ")
    email = input("Ingrese el correo electrónico del repartidor (presione Enter si no hay correo electrónico): ")
    numpedido = input("Ingrese el número del pedido asignado al repartidor (presione Enter si no hay pedido asignado): ")

    
    cursor.execute("INSERT INTO Repartidor (cedula, nombre, telefono, calificacion, fechanacimiento, email, numpedido) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (cedula, nombre, telefono, calificacion, fechanacimiento, email, numpedido))
    connection.commit()
    print("Registro de repartidor agregado exitosamente.")

def consultar_repartidor():
    cedula = input("Ingrese la cédula del repartidor: ")

    cursor.execute("SELECT * FROM Repartidor WHERE cedula = %s", (cedula,))
    row = cursor.fetchone()

    if row:
        print("Repartidor encontrado:")
        print("Cédula:", row[0])
        print("Nombre:", row[1])
        print("Teléfono:", row[2] if row[2] else "No hay número de teléfono")
        print("Calificación:", row[3] if row[3] else "No hay calificación")
        print("Fecha de Nacimiento:", row[4])
        print("Email:", row[5] if row[5] else "No hay correo electrónico")
        print("Número de Pedido Asignado:", row[6] if row[6] else "No hay pedido asignado")
    else:
        print("Repartidor no encontrado.")

def actualizar_repartidor():
    cedula = input("Ingrese la cédula del repartidor que desea actualizar: ")

    cursor.execute("SELECT * FROM Repartidor WHERE cedula = %s", (cedula,))
    row = cursor.fetchone()

    if row:
        print("Repartidor actual:")
        print("Cédula:", row[0])
        print("Nombre:", row[1])
        print("Teléfono:", row[2] if row[2] else "No hay número de teléfono")
        print("Calificación:", row[3] if row[3] else "No hay calificación")
        print("Fecha de Nacimiento:", row[4])
        print("Email:", row[5] if row[5] else "No hay correo electrónico")
        print("Número de Pedido Asignado:", row[6] if row[6] else "No hay pedido asignado")

        nuevo_nombre = input("Ingrese el nuevo nombre del repartidor (presione Enter para dejar sin cambios): ")
        nuevo_telefono = input("Ingrese el nuevo número de teléfono (presione Enter para dejar sin cambios): ")
        nueva_calificacion = input("Ingrese la nueva calificación (presione Enter para dejar sin cambios): ")
        nueva_fechanacimiento = input("Ingrese la nueva fecha de nacimiento (presione Enter para dejar sin cambios): ")
        nuevo_email = input("Ingrese el nuevo correo electrónico (presione Enter para dejar sin cambios): ")
        nuevo_numpedido = input("Ingrese el nuevo número de pedido asignado (presione Enter para dejar sin cambios): ")

        if nuevo_nombre:
            row[1] = nuevo_nombre
        if nuevo_telefono:
            row[2] = nuevo_telefono
        if nueva_calificacion:
            row[3] = nueva_calificacion
        if nueva_fechanacimiento:
            row[4] = nueva_fechanacimiento
        if nuevo_email:
            row[5] = nuevo_email
        if nuevo_numpedido:
            row[6] = nuevo_numpedido

        cursor.execute("UPDATE Repartidor SET nombre = %s, telefono = %s, calificacion = %s, fechanacimiento = %s, email = %s, numpedido = %s WHERE cedula = %s",
                       (row[1], row[2], row[3], row[4], row[5], row[6], cedula))
        connection.commit()
        print("Registro de repartidor actualizado exitosamente.")
    else:
        print("Repartidor no encontrado.")

def eliminar_repartidor():
    cedula = input("Ingrese la cédula del repartidor que desea eliminar: ")

    cursor.execute("DELETE FROM Repartidor WHERE cedula = %s", (cedula,))
    connection.commit()
    print("Registro de repartidor eliminado exitosamente.")

# Menú interactivo
while True:
    print("\nMenu:")
    print("1. Operaciones con Calificaciones")
    print("2. Operaciones con Clientes")
    print("3. Operaciones con Establecimientos")
    print("4. Operaciones con Métodos de Pago")
    print("5. Operaciones con Productos")
    print("6. Operaciones con Repartidores")
    print("7. Salir")

    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        while True:
            print("\nMenú Calificaciones:")
            print("1. Agregar Calificación")
            print("2. Consultar Calificación")
            print("3. Actualizar Calificación")
            print("4. Eliminar Calificación")
            print("5. Volver al Menú Principal")

            opcion_calificacion = input("Seleccione una opción (1-5): ")

            if opcion_calificacion == "1":
                agregar_calificacion()
            elif opcion_calificacion == "2":
                consultar_calificacion()
            elif opcion_calificacion == "3":
                actualizar_calificacion()
            elif opcion_calificacion == "4":
                eliminar_calificacion()
            elif opcion_calificacion == "5":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    elif opcion == "2":
        while True:
            print("\nMenú Clientes:")
            print("1. Agregar Cliente")
            print("2. Consultar Cliente")
            print("3. Actualizar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")

            opcion_cliente = input("Seleccione una opción (1-5): ")

            if opcion_cliente == "1":
                agregar_cliente()
            elif opcion_cliente == "2":
                consultar_cliente()
            elif opcion_cliente == "3":
                actualizar_cliente()
            elif opcion_cliente == "4":
                eliminar_cliente()
            elif opcion_cliente == "5":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
    elif opcion == "3":
        while True:
            print("\nMenú Establecimientos:")
            print("1. Agregar Establecimiento")
            print("2. Consultar Establecimiento")
            print("3. Actualizar Establecimiento")
            print("4. Eliminar Establecimiento")
            print("5. Volver al Menú Principal")

            opcion_establecimiento = input("Seleccione una opción (1-5): ")

            if opcion_establecimiento == "1":
                agregar_establecimiento()
            elif opcion_establecimiento == "2":
                consultar_establecimiento()
            elif opcion_establecimiento == "3":
                actualizar_establecimiento()
            elif opcion_establecimiento == "4":
                eliminar_establecimiento()
            elif opcion_establecimiento == "5":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
    elif opcion == "4":
        while True:
            print("\nMenú Métodos de Pago:")
            print("1. Agregar Método de Pago")
            print("2. Consultar Método de Pago")
            print("3. Actualizar Método de Pago")
            print("4. Eliminar Método de Pago")
            print("5. Volver al Menú Principal")

            opcion_metodo_pago = input("Seleccione una opción (1-5): ")

            if opcion_metodo_pago == "1":
                agregar_metodo_pago()
            elif opcion_metodo_pago == "2":
                consultar_metodo_pago()
            elif opcion_metodo_pago == "3":
                actualizar_metodo_pago()
            elif opcion_metodo_pago == "4":
                eliminar_metodo_pago()
            elif opcion_metodo_pago == "5":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
    elif opcion == "5":
        while True:
            print("\nMenú Productos:")
            print("1. Agregar Producto")
            print("2. Consultar Producto")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("5. Volver al Menú Principal")

            opcion_producto = input("Seleccione una opción (1-5): ")

            if opcion_producto == "1":
                agregar_producto()
            elif opcion_producto == "2":
                consultar_producto()
            elif opcion_producto == "3":
                actualizar_producto()
            elif opcion_producto == "4":
                eliminar_producto()
            elif opcion_producto == "5":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
    elif opcion == "6":
        while True:
            print("\nMenú Repartidores:")
            print("1. Agregar Repartidor")
            print("2. Consultar Repartidor")
            print("3. Actualizar Repartidor")
            print("4. Eliminar Repartidor")
            print("5. Volver al Menú Principal")

            opcion_repartidor = input("Seleccione una opción (1-5): ")

            if opcion_repartidor == "1":
                agregar_repartidor()
            elif opcion_repartidor == "2":
                consultar_repartidor()
            elif opcion_repartidor == "3":
                actualizar_repartidor()
            elif opcion_repartidor == "4":
                eliminar_repartidor()
            elif opcion_repartidor == "5":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")
    elif opcion == "7":
        print("Desconectado de la interfaz")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
