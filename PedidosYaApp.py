import pyodbc
import datetime

# Configurar la conexión a la base de datos
connection_string = 'DRIVER={SQL Server};SERVER=tu_servidor;DATABASE=pedidosya;UID=tu_usuario;PWD=tu_contraseña'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

def agregar_calificacion():
    idpedido = input("Ingrese el ID del pedido: ")
    calificacionEstablecimiento = input("Ingrese la calificación del establecimiento: ")
    calificacionRepartidor = input("Ingrese la calificación del repartidor: ")
    calificacionProducto = input("Ingrese la calificación del producto: ")
    numpedido = input("Ingrese el número del pedido: ")

    cursor.execute("INSERT INTO CALIFICACION VALUES (?, ?, ?, ?, ?)", idpedido, calificacionEstablecimiento, calificacionRepartidor, calificacionProducto, numpedido)
    connection.commit()
    print("Registro agregado exitosamente.")

def consultar_calificacion():
    idpedido = input("Ingrese el ID del pedido: ")
    numpedido = input("Ingrese el número del pedido: ")

    cursor.execute("SELECT * FROM CALIFICACION WHERE idpedido = ? AND numpedido = ?", idpedido, numpedido)
    row = cursor.fetchone()

    if row:
        print("Calificación encontrada:")
        print("ID Pedido:", row.idpedido)
        print("Calificación Establecimiento:", row.calificacionEstablecimiento)
        print("Calificación Repartidor:", row.calificacionRepartidor)
        print("Calificación Producto:", row.calificacionProducto)
        print("Número Pedido:", row.numpedido)
    else:
        print("Calificación no encontrada.")

def actualizar_calificacion():
    idpedido = input("Ingrese el ID del pedido que desea actualizar: ")
    numpedido = input("Ingrese el número del pedido que desea actualizar: ")

    cursor.execute("SELECT * FROM CALIFICACION WHERE idpedido = ? AND numpedido = ?", idpedido, numpedido)
    row = cursor.fetchone()

    if row:
        print("Calificación actual:")
        print("ID Pedido:", row.idpedido)
        print("Calificación Establecimiento:", row.calificacionEstablecimiento)
        print("Calificación Repartidor:", row.calificacionRepartidor)
        print("Calificación Producto:", row.calificacionProducto)
        print("Número Pedido:", row.numpedido)

        nueva_calificacionEstablecimiento = input("Ingrese la nueva calificación del establecimiento (presione Enter para dejar sin cambios): ")
        nueva_calificacionRepartidor = input("Ingrese la nueva calificación del repartidor (presione Enter para dejar sin cambios): ")
        nueva_calificacionProducto = input("Ingrese la nueva calificación del producto (presione Enter para dejar sin cambios): ")

        if nueva_calificacionEstablecimiento:
            row.calificacionEstablecimiento = nueva_calificacionEstablecimiento
        if nueva_calificacionRepartidor:
            row.calificacionRepartidor = nueva_calificacionRepartidor
        if nueva_calificacionProducto:
            row.calificacionProducto = nueva_calificacionProducto

        cursor.execute("UPDATE CALIFICACION SET calificacionEstablecimiento = ?, calificacionRepartidor = ?, calificacionProducto = ? WHERE idpedido = ? AND numpedido = ?",
                       row.calificacionEstablecimiento, row.calificacionRepartidor, row.calificacionProducto, idpedido, numpedido)
        connection.commit()
        print("Registro actualizado exitosamente.")
    else:
        print("Calificación no encontrada.")

def eliminar_calificacion():
    idpedido = input("Ingrese el ID del pedido que desea eliminar: ")
    numpedido = input("Ingrese el número del pedido que desea eliminar: ")

    cursor.execute("DELETE FROM CALIFICACION WHERE idpedido = ? AND numpedido = ?", idpedido, numpedido)
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
