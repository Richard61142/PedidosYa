import mysql.connector

# Configurar la conexión a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="moreira520",
    database="pedidosya"
)
cursor = connection.cursor()
print("Se ha conectado a la bases de datos con éxito!!")



######################### CALIFICACION ###################################
def agregar_calificacion():
    idpedido = input("Ingrese el ID del pedido: ")
    calificacionEstablecimiento = input("Ingrese la calificación del establecimiento: ")
    calificacionRepartidor = input("Ingrese la calificación del repartidor: ")
    calificacionProducto = input("Ingrese la calificación del producto: ")
    numpedido = input("Ingrese el número del pedido: ")


    cursor.callproc("Agregar_calificacion", (idpedido, calificacionEstablecimiento, calificacionRepartidor, calificacionProducto, numpedido))
    connection.commit()
    print("Registro agregado exitosamente.")


def consultar_calificacion():
    try:
        idpedido = input("Ingrese el ID del pedido: ")

        cursor.callproc("Consultar_calificacion", (idpedido,))
        for result in cursor.stored_results():
            rows = result.fetchall()

            if rows:
                print("Calificación encontrada:")
                for row in rows:
                    print("ID Pedido:", row[0])
                    print("Calificación Establecimiento:", row[1])
                    print("Calificación Repartidor:", row[2])
                    print("Calificación Producto:", row[3])
                    print("Número Pedido:", row[4])
            else:
                print("Calificación no encontrada.")

    except mysql.connector.Error as err:
        print(f"Error de MySQL: {err}")


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


        print("\nSeleccione el campo que desea actualizar:")
        print("1 - Calificación Establecimiento")
        print("2 - Calificación Repartidor")
        print("3 - Calificación Producto")
        print("4 - No realizar cambios")

        opcion = input("Ingrese el número de la opción: ")


        if opcion == "1":
            nuevo_valor = input("Ingrese la nueva calificación del establecimiento: ")
            cursor.callproc("Actualizar_calificacion_establecimiento", (idpedido, nuevo_valor))
        elif opcion == "2":
            nuevo_valor = input("Ingrese la nueva calificación del repartidor: ")
            cursor.callproc("Actualizar_calificacion_repartidor", (idpedido, nuevo_valor))
        elif opcion == "3":
            nuevo_valor = input("Ingrese la nueva calificación del producto: ")
            cursor.callproc("Actualizar_calificacion_producto", (idpedido, nuevo_valor))

        if opcion != "4":
            connection.commit()
            print("Registro actualizado exitosamente.")
        else:
            print("No se realizaron cambios.")
    else:
        print("Calificación no encontrada.")




def eliminar_calificacion():
    idpedido = input("Ingrese el ID del pedido que desea eliminar: ")


    cursor.callproc("Eliminar_calificacion", (idpedido,))
    connection.commit()
    print("Registro eliminado exitosamente.")
    
############################ CLIENTE ######################################
 
def agregar_cliente():
    telefono = input("Ingrese el número de teléfono: ")
    email = input("Ingrese el email: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    cedula = input("Ingrese la cédula: ")
    direccion = input("Ingrese la dirección: ")
    edad = input("Ingrese la edad: ")
    numpedido = input("Ingrese el número del pedido: ")
    
    
    id_empleado = input("Ingrese el ID del empleado (presione Enter para dejarlo en blanco): ")
    id_empleado = id_empleado.strip() if id_empleado else None

    cursor.callproc("sp_agregar_cliente", (telefono, email, fecha_nacimiento, cedula, direccion, edad, numpedido, id_empleado))
    connection.commit()
    print("Cliente agregado exitosamente.")



def consultar_cliente():
    telefono = input("Ingrese el número de teléfono: ")


    cursor.callproc("sp_consultar_cliente", (telefono,))
    for result in cursor.stored_results():
        rows = result.fetchall()

        if rows:
            print("Cliente encontrado:")
            for row in rows:
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

    print("Seleccione la información que desea modificar:")
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
        nueva_valor = input("Ingrese el nuevo correo electrónico: ")
        campo = 'email'
    elif opcion == '2':
        nueva_valor = input("Ingrese la nueva fecha de nacimiento: ")
        campo = 'fecha_nacimiento'
    elif opcion == '3':
        nueva_valor = input("Ingrese la nueva cédula: ")
        campo = 'cedula'
    elif opcion == '4':
        nueva_valor = input("Ingrese la nueva dirección: ")
        campo = 'direccion'
    elif opcion == '5':
        nueva_valor = input("Ingrese la nueva edad: ")
        campo = 'edad'
    elif opcion == '6':
        nueva_valor = input("Ingrese el nuevo número del pedido: ")
        campo = 'num_pedido'
    elif opcion == '7':
        nueva_valor = input("Ingrese el nuevo ID del empleado: ")
        campo = 'id_empleado'
    elif opcion == '8':
        print("No se realizarán cambios. Volviendo al menú principal.")
        return
    else:
        print("Opción no válida. No se realizarán cambios.")
        return


    cursor.callproc('sp_actualizar_cliente', (
        telefono,
        nueva_valor if campo == 'email' else None,
        nueva_valor if campo == 'fecha_nacimiento' else None,
        nueva_valor if campo == 'cedula' else None,
        nueva_valor if campo == 'direccion' else None,
        nueva_valor if campo == 'edad' else None,
        nueva_valor if campo == 'num_pedido' else None,
        nueva_valor if campo == 'id_empleado' else None
    ))

    connection.commit()
    print("Registro actualizado exitosamente.")
    return


def eliminar_cliente():
    telefono = input("Ingrese el número de teléfono que desea eliminar: ")


    cursor.callproc("sp_eliminar_cliente", (telefono,))
    connection.commit()
    print("Cliente eliminado exitosamente.")

############################## ESTABLECIMIENTO ################################

def agregar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento: ")
    numpedido = input("Ingrese el número del pedido: ")
    ubicacion = input("Ingrese la ubicación: ")
    calificacion = input("Ingrese la calificación: ")
    distancia = input("Ingrese la distancia: ")
    telefono = input("Ingrese el teléfono: ")
    tipoEstablecimiento = input("Ingrese el tipo de establecimiento: ")


    cursor.callproc("sp_agregar_establecimiento", (idEstablecimiento, numpedido, ubicacion, calificacion, distancia, telefono, tipoEstablecimiento))
    connection.commit()
    print("Establecimiento agregado exitosamente.")
    
    
def consultar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento: ")


    cursor.callproc("sp_consultar_establecimiento", (idEstablecimiento,))
    for result in cursor.stored_results():
        rows = result.fetchall()

        if rows:
            print("Establecimiento encontrado:")
            for row in rows:
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

        print("\nSeleccione el campo que desea actualizar:")
        print("1 - Número Pedido")
        print("2 - Ubicación")
        print("3 - Calificación")
        print("4 - Distancia")
        print("5 - Teléfono")
        print("6 - Tipo de Establecimiento")
        print("7 - No realizar cambios")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            nuevo_numero_pedido = input("Ingrese el nuevo número de pedido: ")
            row = list(row)
            row[1] = nuevo_numero_pedido
        elif opcion == '2':
            nueva_ubicacion = input("Ingrese la nueva ubicación: ")
            row = list(row)
            row[2] = nueva_ubicacion
        elif opcion == '3':
            nueva_calificacion = input("Ingrese la nueva calificación: ")
            row = list(row)
            row[3] = nueva_calificacion
        elif opcion == '4':
            nueva_distancia = input("Ingrese la nueva distancia: ")
            row = list(row)
            row[4] = nueva_distancia
        elif opcion == '5':
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            row = list(row)
            row[5] = nuevo_telefono
        elif opcion == '6':
            nuevo_tipo_establecimiento = input("Ingrese el nuevo tipo de establecimiento: ")
            row = list(row)
            row[6] = nuevo_tipo_establecimiento
        elif opcion == '7':
            print("No se realizarán cambios.")
        else:
            print("Opción no válida. No se realizarán cambios.")

       
        cursor.callproc("sp_actualizar_establecimiento", (
            idEstablecimiento,
            row[1],  # Número Pedido
            row[2],  # Ubicación
            row[3],  # Calificación
            row[4],  # Distancia
            row[5],  # Teléfono
            row[6]   # Tipo de Establecimiento
        ))
        connection.commit()
        print("Establecimiento actualizado exitosamente.")
    else:
        print("Establecimiento no encontrado.")




def eliminar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento que desea eliminar: ")

    # Utilizar el procedimiento almacenado
    cursor.callproc("sp_eliminar_establecimiento", (idEstablecimiento,))
    connection.commit()
    print("Establecimiento eliminado exitosamente.")


######################### METODO DE PAGO ####################################

def agregar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago: ")
    idcliente = input("Ingrese el ID del cliente: ")
    NumPedido = input("Ingrese el número del pedido: ")
    tipo_tarjeta = input("Ingrese el tipo de tarjeta (debito/credito): ")
    numTarjeta = input("Ingrese el número de tarjeta: ")
    apodo = input("Ingrese el apodo: ")
    fechaExpi = input("Ingrese la fecha de expiración (YYYY-MM-DD): ")


    cursor.callproc("sp_agregar_metodo_pago", (IDmetodoPago, idcliente, NumPedido, tipo_tarjeta, numTarjeta, apodo, fechaExpi))
    connection.commit()
    print("Método de pago agregado exitosamente.")
    
    
    


def consultar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago: ")

    try:

        cursor.callproc("sp_consultar_metodo_pago", (IDmetodoPago,))
        for result in cursor.stored_results():
            rows = result.fetchall()

            if rows:
                print("Método de pago encontrado:")
                for row in rows:
                    print("ID Método de Pago:", row[0])
                    print("ID Cliente:", row[1])
                    print("Número Pedido:", row[2])


                cursor.execute("SELECT * FROM TarjetaDebito WHERE IDmetodoPago = %s", (IDmetodoPago,))
                row_debito = cursor.fetchone()
                if row_debito:
                    print("Tarjeta Débito vinculada:")
                    print("Número de Tarjeta:", row_debito[1])
                    print("Apodo:", row_debito[2])
                    print("Fecha de Expiración:", row_debito[3])
                else:
                    print("No se encontró tarjeta débito vinculada.")
            else:
                print("Método de pago no encontrado.")

    except mysql.connector.Error as err:
        print("Error de MySQL: {}".format(err))




def actualizar_metodo_pago():
    try:
        IDmetodoPago = input("Ingrese el ID del método de pago que desea actualizar: ")
        nuevo_idcliente = input("Ingrese el nuevo ID del cliente (presione Enter para dejar sin cambios): ")
        nuevo_NumPedido = input("Ingrese el nuevo número del pedido (presione Enter para dejar sin cambios): ")
        

        nuevo_NumPedido = int(nuevo_NumPedido) if nuevo_NumPedido else None

        tipo_tarjeta = input("Ingrese el tipo de tarjeta (debito/credito): ")
        nuevo_numTarjeta = input("Ingrese el nuevo número de tarjeta (presione Enter para dejar sin cambios): ")
        nuevo_apodo = input("Ingrese un nuevo apodo para la tarjeta (presione Enter para dejar sin cambios): ")
        nueva_fechaExpi = input("Ingrese la nueva fecha de expiración (YYYY-MM-DD) de la tarjeta (presione Enter para dejar sin cambios): ")

        cursor.callproc('sp_actualizar_metodo_pago', (IDmetodoPago, nuevo_idcliente, nuevo_NumPedido, tipo_tarjeta, nuevo_numTarjeta, nuevo_apodo, nueva_fechaExpi))
        connection.commit()
        print("Registro de método de pago actualizado exitosamente.")
    except mysql.connector.Error as err:
        if err.errno == 1644:
            print("No se encontró la entrada para el ID del método de pago especificado.")
        else:
            print(f"Error al actualizar método de pago: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def eliminar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago que desea eliminar: ")
    cursor.callproc("sp_eliminar_metodo_pago", (IDmetodoPago,))
    connection.commit()
    print("Método de pago eliminado exitosamente.")

##################### PRODUCTO #########################################

def agregar_producto():
    idproducto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    foto = input("Ingrese la ruta de la foto del producto (o deje en blanco si no hay foto): ")
    precio = input("Ingrese el precio del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    descuento = input("Ingrese el descuento del producto: ")
    idEstablecimiento = input("Ingrese el ID del establecimiento asociado al producto: ")


    if foto:
        with open(foto, 'rb') as file:
            foto_binaria = file.read()
    else:
        foto_binaria = None

    cursor.callproc("sp_agregar_producto", (idproducto, nombre, foto_binaria, precio, descripcion, descuento, idEstablecimiento))
    connection.commit()
    print("Producto agregado exitosamente.")


def consultar_producto():
    idproducto = input("Ingrese el ID del producto: ")

    cursor.callproc("sp_consultar_producto", (idproducto,))
    for result in cursor.stored_results():
        rows = result.fetchall()

        if rows:
            print("Producto encontrado:")
            for row in rows:
                print("ID Producto:", row[0])
                print("Nombre:", row[1])
                print("Precio:", row[3])
                print("Descripción:", row[4])
                print("Descuento:", row[5])
                print("ID Establecimiento:", row[6])
        else:
            print("Producto no encontrado o no disponible.")



def actualizar_producto():
    idproducto = input("Ingrese el ID del producto que desea actualizar: ")


    cursor.execute("SELECT * FROM Producto WHERE idproducto = %s", (idproducto,))
    row = cursor.fetchone()

    if row:
        print("Producto actual:")
        print("ID Producto:", row[0])
        print("Nombre:", row[1])
        print("Foto:", row[2]) 
        print("Precio:", row[3])
        print("Descripción:", row[4])
        print("Descuento:", row[5])
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


        nuevo_nombre = row[1]
        nueva_foto = row[2]
        nuevo_precio = row[3]
        nueva_descripcion = row[4]
        nuevo_descuento = row[5]
        nuevo_idEstablecimiento = row[6]

        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        elif opcion == "2":
            nueva_foto = input("Ingrese la nueva ruta de la foto del producto: ")
        elif opcion == "3":
            nuevo_precio = input("Ingrese el nuevo precio del producto: ")
        elif opcion == "4":
            nueva_descripcion = input("Ingrese la nueva descripción del producto: ")
        elif opcion == "5":
            nuevo_descuento = input("Ingrese el nuevo descuento del producto: ")
        elif opcion == "6":
            nuevo_idEstablecimiento = input("Ingrese el nuevo ID del establecimiento asociado al producto: ")


        try:
            nuevo_precio_decimal = float(nuevo_precio)
        except ValueError:
            print("Error: El precio debe ser un valor decimal válido.")
            return

        try:
            nuevo_descuento_decimal = float(nuevo_descuento)
        except ValueError:
            print("Error: El descuento debe ser un valor numérico válido.")
            return


        cursor.callproc("sp_actualizar_producto", (idproducto, nuevo_nombre, nueva_foto, nuevo_precio_decimal, nueva_descripcion, nuevo_descuento_decimal, nuevo_idEstablecimiento))
        connection.commit()
        print("Producto actualizado exitosamente.")
    else:
        print("Producto no encontrado.")


def eliminar_producto():
    idproducto = input("Ingrese el ID del producto que desea eliminar: ")


    cursor.callproc("sp_eliminar_producto", (idproducto,))
    connection.commit()
    print("Producto eliminado exitosamente.")


############################### REPARTIDOR ####################################

def agregar_repartidor():
    cedula = input("Ingrese la cédula del repartidor: ")
    nombre = input("Ingrese el nombre del repartidor: ")
    telefono = input("Ingrese el teléfono del repartidor: ")
    calificacion = input("Ingrese la calificación del repartidor: ")
    fechanacimiento = input("Ingrese la fecha de nacimiento del repartidor (YYYY-MM-DD): ")
    email = input("Ingrese el correo electrónico del repartidor: ")
    numpedido = input("Ingrese el número del pedido asociado al repartidor: ")


    cursor.callproc("sp_agregar_repartidor", (cedula, nombre, telefono, calificacion, fechanacimiento, email, numpedido))
    connection.commit()
    print("Repartidor agregado exitosamente.")

def consultar_repartidor():
    cedula = input("Ingrese la cédula del repartidor: ")


    cursor.callproc("sp_consultar_repartidor", (cedula,))
    for result in cursor.stored_results():
        rows = result.fetchall()

        if rows:
            print("Repartidor encontrado:")
            for row in rows:
                print("Cédula:", row[0])
                print("Nombre:", row[1])
                print("Teléfono:", row[2])
                print("Calificación:", row[3])
                print("Fecha de Nacimiento:", row[4])
                print("Correo Electrónico:", row[5])
                print("Número de Pedido:", row[6])
        else:
            print("Repartidor no encontrado.")


def actualizar_repartidor():
    try:
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

            print("\nSeleccione el campo que desea actualizar:")
            print("1 - Nombre")
            print("2 - Teléfono")
            print("3 - Calificación")
            print("4 - Fecha de Nacimiento")
            print("5 - Email")
            print("6 - Número de Pedido Asignado")
            print("7 - No realizar cambios")

            opcion = input("Ingrese el número de la opción: ")

 
            nuevo_nombre = row[1]
            nuevo_telefono = row[2]
            nueva_calificacion = row[3]
            nueva_fechanacimiento = row[4]
            nuevo_email = row[5]
            nuevo_numpedido = row[6]

            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre del repartidor: ")
            elif opcion == "2":
                nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            elif opcion == "3":
                nueva_calificacion = input("Ingrese la nueva calificación del repartidor: ")
            elif opcion == "4":
                nueva_fechanacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
            elif opcion == "5":
                nuevo_email = input("Ingrese el nuevo correo electrónico: ")
            elif opcion == "6":
                nuevo_numpedido = input("Ingrese el nuevo número de pedido asignado: ")

 
            nuevo_telefono = int(nuevo_telefono) if nuevo_telefono else None

     
            nueva_calificacion = float(nueva_calificacion) if nueva_calificacion else None

        
            nueva_fechanacimiento = nueva_fechanacimiento if nueva_fechanacimiento else None

         
            nuevo_numpedido = int(nuevo_numpedido) if nuevo_numpedido else None

            cursor.callproc("sp_actualizar_repartidor", (cedula, nuevo_nombre, nuevo_telefono, nueva_calificacion, nueva_fechanacimiento, nuevo_email, nuevo_numpedido))
            connection.commit()
            print("Repartidor actualizado exitosamente.")
        else:
            print("Repartidor no encontrado.")

    except mysql.connector.Error as err:
        if err.errno == 1644:
            print("No se encontró la entrada para la cédula del repartidor especificado.")
        else:
            print(f"Error al actualizar repartidor: {err}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()
        
        
        


def eliminar_repartidor():
    try:
        cedula = input("Ingrese la cédula del repartidor que desea eliminar: ")


        cursor.execute("SELECT COUNT(*) FROM repartidor WHERE cedula = %s", (cedula,))
        count = cursor.fetchone()[0]

        if count == 0:
            print("Error: La cédula especificada no existe en la tabla repartidor.")
            return

        cursor.callproc("sp_eliminar_repartidor", (cedula,))
        connection.commit()
        print("Repartidor eliminado exitosamente.")

    except mysql.connector.Error as err:
        if err.errno == 1644:
            print("Error: No se puede eliminar el repartidor, existen pedidos asociados.")
        else:
            print(f"Error al eliminar repartidor: {err}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()



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

