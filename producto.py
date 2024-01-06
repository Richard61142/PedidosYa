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

    cursor.execute("DELETE FROM Producto WHERE idproducto = %s", (idproducto,))
    connection.commit()
    print("Registro eliminado exitosamente.")

# Menú interactivo
while True:
    print("\nMenu:")
    print("1. Agregar Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        consultar_producto()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

# Cerrar la conexión
cursor.close()
connection.close()
