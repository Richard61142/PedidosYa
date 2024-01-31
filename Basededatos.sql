CREATE DATABASE IF NOT EXISTS pedidosya;
USE pedidosya;

CREATE TABLE CALIFICACION(
	idpedido VARCHAR(50) NOT NULL,
	calificacionEstablecimiento VARCHAR(250),
	calificacionRepartidor VARCHAR(250),
	calificacionProducto VARCHAR(250),
	numpedido VARCHAR(50) NOT NULL,
	PRIMARY KEY(idpedido,numpedido),
	INDEX idx_numpedido (numpedido)
);


CREATE TABLE Establecimiento(
    idEstablecimiento VARCHAR(50) NOT NULL,
    numpedido VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(250) NOT NULL,
    calificacion FLOAT NULL,
    distancia FLOAT NOT NULL,
    telefono INT NOT NULL,
    tipoEstablecimiento VARCHAR(50) NOT NULL,
    PRIMARY KEY (idEstablecimiento, numpedido),
    foreign key (numpedido) references CALIFICACION(numpedido)
);

CREATE TABLE ServicioTecnico(
    id_empleado VARCHAR(50) PRIMARY KEY NOT NULL,
    nombre VARCHAR(250) NOT NULL,
    correo VARCHAR(250) NOT NULL,
    telefono INT NOT NULL
);

CREATE TABLE Cliente(
    Telefono INT NOT NULL,
    email VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    cedula BIGINT NOT NULL,
    direccion VARCHAR(250) NOT NULL,
    edad INT,
    numpedido VARCHAR(50) NOT NULL,
    id_empleado VARCHAR(50),
    PRIMARY KEY (Telefono),
    foreign key (id_empleado) references ServicioTecnico(id_empleado),
	foreign key (numpedido) references CALIFICACION(numpedido)
);


CREATE TABLE Producto(
    idproducto VARCHAR(50) PRIMARY KEY NOT NULL,
    nombre VARCHAR(30) NOT NULL, 
    foto BLOB,
    precio FLOAT NOT NULL,
    descripcion VARCHAR(250) NOT NULL,
    descuento FLOAT NULL,
    idEstablecimiento VARCHAR(50),
    FOREIGN KEY (idEstablecimiento) REFERENCES Establecimiento(idEstablecimiento)
);

CREATE TABLE PerfilCliente(
    idCliente VARCHAR(50) PRIMARY KEY NOT NULL,
    HistorialPedido VARCHAR(20),
    favoritos VARCHAR(250),
    direcciones VARCHAR(250),
    cupones VARCHAR(250),
    MetodoDePago VARCHAR(250),
    Telefono INT NOT NULL,
    FOREIGN KEY (Telefono) REFERENCES Cliente(Telefono)
);


CREATE TABLE Cancelacion(
    numpedido VARCHAR(50) PRIMARY KEY NOT NULL,
    motivo VARCHAR(250),
    estadoDelPedido VARCHAR(250),
    costoCancelacion FLOAT NOT NULL
);



CREATE TABLE Repartidor(
    cedula BIGINT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    telefono INT,
    calificacion VARCHAR(250) NULL,
    fechanacimiento DATE NOT NULL,
    email VARCHAR(50),
    numpedido VARCHAR(50) NOT NULL,
    primary key(cedula,numpedido),
    foreign key (numpedido) references CALIFICACION(numpedido)
);


CREATE TABLE Vehiculo(
    idvehiculo VARCHAR(50) PRIMARY KEY NOT NULL,
    color VARCHAR(50) NOT NULL,
    cedula BIGINT NOT NULL,
	FOREIGN KEY(cedula) REFERENCES Repartidor(cedula)
);

CREATE TABLE Carro(
    idvehiculo VARCHAR(50) NOT NULL,
    numMatricula VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    FOREIGN KEY (idvehiculo) REFERENCES Vehiculo(idvehiculo)
);

CREATE TABLE Motocicleta(
    idvehiculo VARCHAR(50) NOT NULL,
    numMatricula VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    FOREIGN KEY (idvehiculo) REFERENCES Vehiculo(idvehiculo)
);

CREATE TABLE Bicicleta(
    idvehiculo VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    FOREIGN KEY (idvehiculo) REFERENCES Vehiculo(idvehiculo)
);
CREATE TABLE Pedido(
	numpedido VARCHAR(50) NOT NULL,
	estado VARCHAR(30) NOT NULL,
	ubicacion VARCHAR(250) NOT NULL,
	precio FLOAT(10) NOT NULL,
	telefono INT ,
	cedula BIGINT NOT NULL,
	idproducto VARCHAR(30) NOT NULL,
	establecimiento VARCHAR(50) NOT NULL,
    PRIMARY KEY(numpedido),
    foreign key(establecimiento) references Establecimiento(idEstablecimiento),
    foreign key(telefono) references Cliente(telefono),
    foreign key(idproducto) references Producto(idproducto),
    foreign key(numpedido) references Cancelacion(numpedido),
    foreign key(cedula) references Repartidor(cedula)
	);

CREATE TABLE MetodoDePago(
    IDmetodoPago VARCHAR(50) PRIMARY KEY NOT NULL,
    idcliente VARCHAR(50) NOT NULL,
    NumPedido VARCHAR(50) ,
    FOREIGN KEY (idcliente) REFERENCES PerfilCliente(idCliente),
    FOREIGN KEY(NumPedido) REFERENCES Pedido(numpedido)
);

CREATE TABLE TarjetaDebito(
    IDmetodoPago VARCHAR(50) NOT NULL,
    numTarjeta VARCHAR(16) NOT NULL,
    apodo VARCHAR(250) NOT NULL,
    FechaExpi DATE NOT NULL,
    FOREIGN KEY (IDmetodoPago) REFERENCES MetodoDePago(IDmetodoPago)
);

CREATE TABLE TarjetaCredito(
    IDmetodoPago VARCHAR(50) NOT NULL,
    numTarjeta VARCHAR(16) NOT NULL,
    apodo VARCHAR(250) NOT NULL,
    FechaExpi DATE NOT NULL,
    FOREIGN KEY (IDmetodoPago) REFERENCES MetodoDePago(IDmetodoPago)
);

