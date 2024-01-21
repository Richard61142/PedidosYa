import mysql.connector

# Configurar la conexión a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="------PASSWORD-----", #COLOCAR EL PASSWORD
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
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
