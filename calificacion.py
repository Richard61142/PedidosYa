import datetime
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

def agregar_calificacion():
    idpedido = input("Ingrese el ID del pedido: ")
    calificacionEstablecimiento = input("Ingrese la calificación del establecimiento: ")
    calificacionRepartidor = input("Ingrese la calificación del repartidor: ")
    calificacionProducto = input("Ingrese la calificación del producto: ")
    numpedido = input("Ingrese el número del pedido: ")

    # Utilizar %s como marcador de posición
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

# Menú interactivo
while True:
    print("\nMenu:")
    print("1. Agregar Calificación")
    print("2. Consultar Calificación")
    print("3. Actualizar Calificación")
    print("4. Eliminar Calificación")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_calificacion()
    elif opcion == "2":
        consultar_calificacion()
    elif opcion == "3":
        actualizar_calificacion()
    elif opcion == "4":
        eliminar_calificacion()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
