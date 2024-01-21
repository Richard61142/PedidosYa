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

def agregar_establecimiento():
    idEstablecimiento = input("Ingrese el ID del establecimiento: ")
    numpedido = input("Ingrese el número del pedido: ")
    ubicacion = input("Ingrese la ubicación: ")
    calificacion = input("Ingrese la calificación del establecimiento: ")
    distancia = input("Ingrese la distancia: ")
    telefono = input("Ingrese el número de teléfono: ")
    tipoEstablecimiento = input("Ingrese el tipo de establecimiento: ")

    # Utilizar un marcador de posición para cada valor y proporcionarlos como una tupla
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

        # Realizar la actualización utilizando una nueva consulta
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

    cursor.execute("DELETE FROM Establecimiento WHERE idEstablecimiento = %s AND numpedido = %s",
                   (idEstablecimiento, numpedido))
    connection.commit()
    print("Registro eliminado exitosamente.")

# Menú interactivo
while True:
    print("\nMenu:")
    print("1. Agregar Establecimiento")
    print("2. Consultar Establecimiento")
    print("3. Actualizar Establecimiento")
    print("4. Eliminar Establecimiento")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_establecimiento()
    elif opcion == "2":
        consultar_establecimiento()
    elif opcion == "3":
        actualizar_establecimiento()
    elif opcion == "4":
        eliminar_establecimiento()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
