import mysql.connector

# Configurar la conexión a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="---------", #COLOCAR CONTRASEÑA DE LA BASE DA DATOS....
    database="pedidosya"
)
cursor = connection.cursor()
print("Se ha conectado a la bases de datos con éxito!!")

############################ CALIFICACION ##################################
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
    idpedido = input("Ingrese el ID del pedido que desea consultar: ")

    cursor.execute("SELECT * FROM CALIFICACION WHERE idpedido = %s", (idpedido,))
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

    cursor.execute("SELECT * FROM CALIFICACION WHERE idpedido = %s", (idpedido,))
    row = cursor.fetchone()

    if row:
        print("Calificación actual:")
        print("ID Pedido:", row[0])
        print("Calificación Establecimiento:", row[1])
        print("Calificación Repartidor:", row[2])
        print("Calificación Producto:", row[3])
        print("Número Pedido:", row[4])

        print("Seleccione el campo que desea actualizar:")
        print("1 - Calificación Establecimiento")
        print("2 - Calificación Repartidor")
        print("3 - Calificación Producto")
        print("4 - No realizar cambios")

        opcion = input("Ingrese el número de la opción: ")

     
        if opcion == '1':
            nueva_calificacionEstablecimiento = input("Ingrese la nueva calificación del establecimiento: ").upper()
            updated_row = (
                row[0],  # ID Pedido
                nueva_calificacionEstablecimiento,  # Nueva Calificación Establecimiento
                row[2],  # Calificación Repartidor existente
                row[3],  # Calificación Producto existente
                row[4]  # Número Pedido existente
            )
        elif opcion == '2':
            nueva_calificacionRepartidor = input("Ingrese la nueva calificación del repartidor: ").upper()
            updated_row = (
                row[0],  # ID Pedido
                row[1],  # Calificación Establecimiento existente
                nueva_calificacionRepartidor,  # Nueva Calificación Repartidor
                row[3],  # Calificación Producto existente
                row[4]  # Número Pedido existente
            )
        elif opcion == '3':
            nueva_calificacionProducto = input("Ingrese la nueva calificación del producto: ").upper()
            updated_row = (
                row[0],  # ID Pedido
                row[1],  # Calificación Establecimiento existente
                row[2],  # Calificación Repartidor existente
                nueva_calificacionProducto,  # Nueva Calificación Producto
                row[4]  # Número Pedido existente
            )
        elif opcion == '4':
            print("No se realizarán cambios. Volviendo al menú principal.")
            return
        else:
            print("Opción no válida. No se realizarán cambios.")
            return

      
        cursor.execute("UPDATE CALIFICACION SET calificacionEstablecimiento = %s, calificacionRepartidor = %s, calificacionProducto = %s WHERE idpedido = %s",
                       (updated_row[1], updated_row[2], updated_row[3], idpedido))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Calificación no encontrada.")




def eliminar_calificacion():
    idpedido = input("Ingrese el ID del pedido que desea eliminar la calificación: ")

    cursor.execute("DELETE FROM CALIFICACION WHERE idpedido = %s", (idpedido,))
    connection.commit()
    print("Registro de calificación eliminado exitosamente.")


#################################### CLIENTE #################################
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

    cursor.execute("SELECT * FROM Cliente WHERE Telefono = %s", (telefono,))
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

    cursor.execute("SELECT * FROM Cliente WHERE Telefono = %s", (telefono,))
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

        print("Seleccione el campo que desea actualizar:")
        print("1 - Email")
        print("2 - Fecha de Nacimiento")
        print("3 - Cédula")
        print("4 - Dirección")
        print("5 - Edad")
        print("6 - Número del Pedido")
        print("7 - ID del Empleado")
        print("8 - No realizar cambios")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            nueva_email = input("Ingrese el nuevo correo electrónico: ")
        elif opcion == '2':
            nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento: ")
        elif opcion == '3':
            nueva_cedula = input("Ingrese la nueva cédula: ")
        elif opcion == '4':
            nueva_direccion = input("Ingrese la nueva dirección: ")
        elif opcion == '5':
            nueva_edad = input("Ingrese la nueva edad: ")
        elif opcion == '6':
            nuevo_numpedido = input("Ingrese el nuevo número del pedido: ")
        elif opcion == '7':
            nuevo_id_empleado = input("Ingrese el nuevo ID del empleado: ")
        elif opcion == '8':
            print("No se realizarán cambios. Volviendo al menú principal.")
            return
        else:
            print("Opción no válida. No se realizarán cambios.")
            return

        row = (
            row[0],  # Teléfono
            nueva_email if opcion == '1' else row[1],  # Email
            nueva_fecha_nacimiento if opcion == '2' else row[2],  # Fecha de Nacimiento
            nueva_cedula if opcion == '3' else row[3],  # Cédula
            nueva_direccion if opcion == '4' else row[4],  # Dirección
            nueva_edad if opcion == '5' else row[5],  # Edad
            nuevo_numpedido if opcion == '6' else row[6],  # Número Pedido
            nuevo_id_empleado if opcion == '7' else row[7]  # ID Empleado
        )

        cursor.execute("UPDATE Cliente SET email = %s, fecha_nacimiento = %s, cedula = %s, direccion = %s, edad = %s, numpedido = %s, id_empleado = %s WHERE Telefono = %s",
                       (row[1], row[2], row[3], row[4], row[5], row[6], row[7], telefono))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Cliente no encontrado.")


def eliminar_cliente():
    telefono = input("Ingrese el número de teléfono que desea eliminar: ")

    cursor.execute("DELETE FROM Cliente WHERE Telefono = %s", (telefono,))
    connection.commit()
    print("Registro eliminado exitosamente.")


############################### ESTABLECIMIENTO ###############################
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

    cursor.execute("SELECT * FROM Establecimiento WHERE idEstablecimiento = %s", (idEstablecimiento,))
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

        print("Seleccione el campo que desea actualizar:")
        print("1 - Ubicación")
        print("2 - Calificación")
        print("3 - Distancia")
        print("4 - Teléfono")
        print("5 - Tipo de Establecimiento")
        print("6 - No realizar cambios")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            nueva_ubicacion = input("Ingrese la nueva ubicación: ")
        elif opcion == '2':
            nueva_calificacion = input("Ingrese la nueva calificación: ")
        elif opcion == '3':
            nueva_distancia = input("Ingrese la nueva distancia: ")
        elif opcion == '4':
            while True:
                try:
                    nuevo_telefono_input = input("Ingrese el nuevo número de teléfono: ")
                    nuevo_telefono = int(nuevo_telefono_input)
                    break
                except ValueError:
                    print("Por favor, ingrese un valor entero para el número de teléfono.")
        elif opcion == '5':
            nuevo_tipoEstablecimiento = input("Ingrese el nuevo tipo de establecimiento: ")
        elif opcion == '6':
            print("No se realizarán cambios. Volviendo al menú principal.")
            return
        else:
            print("Opción no válida. No se realizarán cambios.")
            return

   
        updated_row = (
            row[0],  # ID Establecimiento
            row[1],  # Número Pedido
            nueva_ubicacion if opcion == '1' else row[2],  # Nueva Ubicación o valor existente
            nueva_calificacion if opcion == '2' else row[3],  # Nueva Calificación o valor existente
            nueva_distancia if opcion == '3' else row[4],  # Nueva Distancia o valor existente
            nuevo_telefono if opcion == '4' else row[5],  # Nuevo Teléfono o valor existente
            nuevo_tipoEstablecimiento if opcion == '5' else row[6],  # Nuevo Tipo de Establecimiento o valor existente
        )

 
        update_query = "UPDATE Establecimiento SET ubicacion = %s, calificacion = %s, distancia = %s, telefono = %s, tipoEstablecimiento = %s WHERE idEstablecimiento = %s"
        cursor.execute(update_query, (updated_row[2], updated_row[3], updated_row[4], updated_row[5], updated_row[6], idEstablecimiento))
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Establecimiento no encontrado.")



def consultar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento que desea consultar: ")

    cursor.execute("SELECT * FROM Establecimiento WHERE idEstablecimiento = %s", (idEstablecimiento,))
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






def eliminar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento que desea eliminar: ")

    try:
       
        cursor.execute("DELETE FROM pedido WHERE idEstablecimiento = %s", (idEstablecimiento,))

        
        cursor.execute("DELETE FROM Establecimiento WHERE idEstablecimiento = %s", (idEstablecimiento,))

        connection.commit()
        print("Registro eliminado exitosamente.")
    except mysql.connector.Error as err:
        
        print(f"Error: {err}")
        connection.rollback()

################################## METODO DE PAGO ###############################
def agregar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago: ")
    idcliente = input("Ingrese el ID del cliente: ")
    NumPedido = input("Ingrese el número del pedido: ")

 
    cursor.execute("INSERT INTO MetodoDePago (IDmetodoPago, idcliente, NumPedido) VALUES (%s, %s, %s)",
                   (IDmetodoPago, idcliente, NumPedido))

    tipo_tarjeta = input("¿Desea vincular una tarjeta de débito o crédito? (debito/credito): ").lower()
    
    if tipo_tarjeta == "debito":
        numTarjeta = input("Ingrese el número de tarjeta de débito: ")
        apodo = input("Ingrese un apodo para la tarjeta de débito: ")
        fechaExpi = input("Ingrese la fecha de expiración (YYYY-MM-DD) de la tarjeta de débito: ")

        cursor.execute("INSERT INTO TarjetaDebito (IDmetodoPago, numTarjeta, apodo, FechaExpi) VALUES (%s, %s, %s, %s)",
                       (IDmetodoPago, numTarjeta, apodo, fechaExpi))

    elif tipo_tarjeta == "credito":
        numTarjeta = input("Ingrese el número de tarjeta de crédito: ")
        apodo = input("Ingrese un apodo para la tarjeta de crédito: ")
        fechaExpi = input("Ingrese la fecha de expiración (YYYY-MM-DD) de la tarjeta de crédito: ")

        cursor.execute("INSERT INTO TarjetaCredito (IDmetodoPago, numTarjeta, apodo, FechaExpi) VALUES (%s, %s, %s, %s)",
                       (IDmetodoPago, numTarjeta, apodo, fechaExpi))

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

        cursor.execute("SELECT * FROM TarjetaDebito WHERE IDmetodoPago = %s", (IDmetodoPago,))
        tarjeta_debito = cursor.fetchone()

        cursor.execute("SELECT * FROM TarjetaCredito WHERE IDmetodoPago = %s", (IDmetodoPago,))
        tarjeta_credito = cursor.fetchone()

        if tarjeta_debito:
            print("Tarjeta de Débito vinculada:")
            print("Número de Tarjeta:", tarjeta_debito[1])
            print("Apodo:", tarjeta_debito[2])
            print("Fecha de Expiración:", tarjeta_debito[3])
        elif tarjeta_credito:
            print("Tarjeta de Crédito vinculada:")
            print("Número de Tarjeta:", tarjeta_credito[1])
            print("Apodo:", tarjeta_credito[2])
            print("Fecha de Expiración:", tarjeta_credito[3])
        else:
            print("No hay tarjeta vinculada.")

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

        # Actualizar tarjeta vinculada (si existe)
        cursor.execute("SELECT * FROM TarjetaDebito WHERE IDmetodoPago = %s", (IDmetodoPago,))
        tarjeta_debito = cursor.fetchone()

        cursor.execute("SELECT * FROM TarjetaCredito WHERE IDmetodoPago = %s", (IDmetodoPago,))
        tarjeta_credito = cursor.fetchone()

        if tarjeta_debito:
            numTarjeta = input("Ingrese el nuevo número de tarjeta de débito (presione Enter para dejar sin cambios): ")
            apodo = input("Ingrese un nuevo apodo para la tarjeta de débito (presione Enter para dejar sin cambios): ")
            fechaExpi = input("Ingrese la nueva fecha de expiración (YYYY-MM-DD) de la tarjeta de débito (presione Enter para dejar sin cambios): ")

            if numTarjeta:
                cursor.execute("UPDATE TarjetaDebito SET numTarjeta = %s WHERE IDmetodoPago = %s",
                               (numTarjeta, IDmetodoPago))
            if apodo:
                cursor.execute("UPDATE TarjetaDebito SET apodo = %s WHERE IDmetodoPago = %s",
                               (apodo, IDmetodoPago))
            if fechaExpi:
                cursor.execute("UPDATE TarjetaDebito SET FechaExpi = %s WHERE IDmetodoPago = %s",
                               (fechaExpi, IDmetodoPago))

        elif tarjeta_credito:
            numTarjeta = input("Ingrese el nuevo número de tarjeta de crédito (presione Enter para dejar sin cambios): ")
            apodo = input("Ingrese un nuevo apodo para la tarjeta de crédito (presione Enter para dejar sin cambios): ")
            fechaExpi = input("Ingrese la nueva fecha de expiración (YYYY-MM-DD) de la tarjeta de crédito (presione Enter para dejar sin cambios): ")

            if numTarjeta:
                cursor.execute("UPDATE TarjetaCredito SET numTarjeta = %s WHERE IDmetodoPago = %s",
                               (numTarjeta, IDmetodoPago))
            if apodo:
                cursor.execute("UPDATE TarjetaCredito SET apodo = %s WHERE IDmetodoPago = %s",
                               (apodo, IDmetodoPago))
            if fechaExpi:
                cursor.execute("UPDATE TarjetaCredito SET FechaExpi = %s WHERE IDmetodoPago = %s",
                               (fechaExpi, IDmetodoPago))

        connection.commit()
        print("Registro de método de pago actualizado exitosamente.")
    else:
        print("Método de pago no encontrado.")





def eliminar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago que desea eliminar: ")

    cursor.execute("SELECT * FROM MetodoDePago WHERE IDmetodoPago = %s", (IDmetodoPago,))
    row = cursor.fetchone()

    if row:
        cursor.execute("DELETE FROM TarjetaDebito WHERE IDmetodoPago = %s", (IDmetodoPago,))
        cursor.execute("DELETE FROM TarjetaCredito WHERE IDmetodoPago = %s", (IDmetodoPago,))

        cursor.execute("DELETE FROM MetodoDePago WHERE IDmetodoPago = %s", (IDmetodoPago,))
        connection.commit()
        print("Registro de método de pago y tarjetas vinculadas eliminados exitosamente.")
    else:
        print("Método de pago no encontrado.")

############################### PRODUCTO #################################
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
        row = list(row)

        print("Producto actual:")
        print("ID Producto:", row[0])
        print("Nombre:", row[1])
        print("Foto:", "Foto disponible" if row[2] else "No hay foto")
        print("Precio:", row[3])
        print("Descripción:", row[4])
        print("Descuento:", row[5] if row[5] else "No hay descuento")
        print("ID Establecimiento:", row[6])

        print("\nSeleccione el campo que desea actualizar:")
        print("1 - Nombre")
        print("2 - Foto")
        print("3 - Precio")
        print("4 - Descripción")
        print("5 - Descuento")
        print("6 - ID Establecimiento")
        print("7 - No realizar cambios")

        opcion = input("Ingrese el número de la opción: ")


        if opcion == "1":
            nuevo_valor = input("Ingrese el nuevo nombre del producto: ")
            row[1] = nuevo_valor if nuevo_valor else row[1]
        elif opcion == "2":
            nueva_foto = input("Ingrese la nueva ruta de la foto del producto: ")
            nuevo_foto_blob = None
            if nueva_foto:
                with open(nueva_foto, "rb") as file:
                    nuevo_foto_blob = file.read()
            row[2] = nuevo_foto_blob if nuevo_foto_blob else row[2]
        elif opcion == "3":
            nuevo_valor = input("Ingrese el nuevo precio del producto: ")
            row[3] = nuevo_valor if nuevo_valor else row[3]
        elif opcion == "4":
            nuevo_valor = input("Ingrese la nueva descripción del producto: ")
            row[4] = nuevo_valor if nuevo_valor else row[4]
        elif opcion == "5":
            nuevo_valor = input("Ingrese el nuevo descuento del producto: ")
            row[5] = nuevo_valor if nuevo_valor else row[5]
        elif opcion == "6":
            nuevo_valor = input("Ingrese el nuevo ID del establecimiento: ")
            row[6] = nuevo_valor if nuevo_valor else row[6]

        if opcion != "7":

            row = tuple(row)

            cursor.execute("UPDATE Producto SET nombre = %s, foto = %s, precio = %s, descripcion = %s, descuento = %s, idEstablecimiento = %s WHERE idproducto = %s",
                           (row[1], row[2], row[3], row[4], row[5], row[6], idproducto))
            connection.commit()
            print("Registro actualizado exitosamente.")
        else:
            print("No se realizaron cambios.")
    else:
        print("Producto no encontrado.")



def eliminar_producto():
    idproducto = input("Ingrese el ID del producto que desea eliminar: ")

    cursor.execute("UPDATE Producto SET disponible = FALSE WHERE idproducto = %s", (idproducto,))
    connection.commit()
    print("Producto marcado como no disponible exitosamente.")
    
############################ REPARTIDOR ##################################
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

        row = list(row)

        print("Repartidor actual:")
        print("Cédula:", row[0])
        print("Nombre:", row[1])
        print("Teléfono:", row[2] if row[2] else "No hay número de teléfono")
        print("Calificación:", row[3] if row[3] else "No hay calificación")
        print("Fecha de Nacimiento:", row[4])
        print("Email:", row[5] if row[5] else "No hay correo electrónico")
        print("Número de Pedido Asignado:", row[6] if row[6] else "No hay pedido asignado")


        print("\nSeleccione el campo que desea actualizar:")
        print("1 - Nombre")
        print("2 - Teléfono")
        print("3 - Calificación")
        print("4 - Fecha de Nacimiento")
        print("5 - Email")
        print("6 - Número de Pedido Asignado")
        print("7 - No realizar cambios")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            nuevo_valor = input("Ingrese el nuevo nombre del repartidor: ")
            row[1] = nuevo_valor if nuevo_valor else row[1]
        elif opcion == "2":
            nuevo_valor = input("Ingrese el nuevo número de teléfono: ")
            row[2] = nuevo_valor if nuevo_valor else row[2]
        elif opcion == "3":
            nuevo_valor = input("Ingrese la nueva calificación: ")
            row[3] = nuevo_valor if nuevo_valor else row[3]
        elif opcion == "4":
            nuevo_valor = input("Ingrese la nueva fecha de nacimiento: ")
            row[4] = nuevo_valor if nuevo_valor else row[4]
        elif opcion == "5":
            nuevo_valor = input("Ingrese el nuevo correo electrónico: ")
            row[5] = nuevo_valor if nuevo_valor else row[5]
        elif opcion == "6":
            nuevo_valor = input("Ingrese el nuevo número de pedido asignado: ")
            row[6] = nuevo_valor if nuevo_valor else row[6]

        if opcion != "7":
        
            row = tuple(row)

         
            cursor.execute("UPDATE Repartidor SET nombre = %s, telefono = %s, calificacion = %s, fechanacimiento = %s, email = %s, numpedido = %s WHERE cedula = %s",
                           (row[1], row[2], row[3], row[4], row[5], row[6], cedula))
            connection.commit()
            print("Registro de repartidor actualizado exitosamente.")
        else:
            print("No se realizaron cambios.")
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
