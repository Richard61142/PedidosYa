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

def agregar_metodo_pago():
    IDmetodoPago = input("Ingrese el ID del método de pago: ")
    idcliente = input("Ingrese el ID del cliente: ")
    NumPedido = input("Ingrese el número del pedido: ")

    # Utilizar un marcador de posición para cada valor y proporcionarlos como una tupla
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

        # Consultar tarjeta vinculada (si existe)
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
        # Eliminar tarjeta vinculada (si existe)
        cursor.execute("DELETE FROM TarjetaDebito WHERE IDmetodoPago = %s", (IDmetodoPago,))
        cursor.execute("DELETE FROM TarjetaCredito WHERE IDmetodoPago = %s", (IDmetodoPago,))

        cursor.execute("DELETE FROM MetodoDePago WHERE IDmetodoPago = %s", (IDmetodoPago,))
        connection.commit()
        print("Registro de método de pago y tarjetas vinculadas eliminados exitosamente.")
    else:
        print("Método de pago no encontrado.")

# Menú interactivo
while True:
    print("\nMenu:")
    print("1. Agregar Método de Pago")
    print("2. Consultar Método de Pago")
    print("3. Actualizar Método de Pago")
    print("4. Eliminar Método de Pago")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_metodo_pago()
    elif opcion == "2":
        consultar_metodo_pago()
    elif opcion == "3":
        actualizar_metodo_pago()
    elif opcion == "4":
        eliminar_metodo_pago()
    elif opcion == "5":
        print("Desconectado de la interfaz")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
