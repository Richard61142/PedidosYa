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

        if nueva_email:
            row[1] = nueva_email
        if nueva_fecha_nacimiento:
            row[2] = nueva_fecha_nacimiento
        if nueva_cedula:
            row[3] = nueva_cedula
        if nueva_direccion:
            row[4] = nueva_direccion
        if nueva_edad:
            row[5] = nueva_edad
        if nuevo_numpedido:
            row[6] = nuevo_numpedido
        if nuevo_id_empleado:
            row[7] = nuevo_id_empleado

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

# Menú interactivo
while True:
    print("\nMenu:")
    print("1. Agregar Cliente")
    print("2. Consultar Cliente")
    print("3. Actualizar Cliente")
    print("4. Eliminar Cliente")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_cliente()
    elif opcion == "2":
        consultar_cliente()
    elif opcion == "3":
        actualizar_cliente()
    elif opcion == "4":
        eliminar_cliente()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
