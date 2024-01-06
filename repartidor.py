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
    print("1. Agregar Repartidor")
    print("2. Consultar Repartidor")
    print("3. Actualizar Repartidor")
    print("4. Eliminar Repartidor")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_repartidor()
    elif opcion == "2":
        consultar_repartidor()
    elif opcion == "3":
        actualizar_repartidor()
    elif opcion == "4":
        eliminar_repartidor()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
