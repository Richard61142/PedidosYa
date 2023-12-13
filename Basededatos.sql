create database if not exists pedidosya;
use pedidosya;

    
create table producto(
	idproducto varchar(50) primary key not null,
	nombre varchar(30) not null, 
	foto Blob,
	precio float(10) not null,
	descripcion varchar(30) not null,
	descuento float(10) null,
	idEstablecimiento varchar(30),
	Foreign Key (idEstablecimiento) references Establecimiento(idEstablecimiento)
);

create table repartidor(
	cedula int primary key not null,
	nombre varchar(50) not null,
	telefono int,
	calificacion varchar(50) null,
	fechanacimiento date not null,
	email varchar(50),
	numpedido varchar(50),
	foreign key (numpedido) references Calificacion(numpedido)    
	);

CREATE TABLE Cliente(
	Telefono INT PRIMARY KEY,
	email VARCHAR(50)not null,
	fecha_nacimiento date not null,
	cedula INT not null,
	direccion VARCHAR(50)not null,
	edad INT,
	numpedido VARCHAR(50) UNIQUE
	);

CREATE TABLE PerfilCliente(
	idCliente VARCHAR(50) PRIMARY KEY,
	HistorialPedido VARCHAR(20),
	favoritos VARCHAR(250),
	direcciones VARCHAR(50),
	cupones VARCHAR(250),
	MetodoDePago VARCHAR(250),
	Telefono INT,
	FOREIGN KEY (Telefono) REFERENCES Cliente(Telefono)
	);

CREATE TABLE ServicioTecnico(
	id_empleado VARCHAR(50) PRIMARY KEY,
	nombre VARCHAR(250)not null,
	correo VARCHAR(250)not null,
	telefono INT not null
	);

CREATE TABLE Establecimiento(
	idEstablecimiento VARCHAR(50),
	numpedido VARCHAR(50),
	ubicacion VARCHAR(250)not null,
	calificacion FLOAT(10)null,
	distancia FLOAT(10)not null,
	telefono INT not null,
	tipoEstablecimiento varchar(50) not null,
	PRIMARY KEY (idEstablecimiento,numpedido)
	);

CREATE TABLE cancelacion(
	numpedido VARCHAR(50) PRIMARY KEY,
	motivo VARCHAR(30),
	estadoDelPedido VARCHAR(30),
	costoCancelacion FLOAT(10)
	);

CREATE TABLE Calificacion(
	idpedido VARCHAR(50),
	calificacionEstablecimiento VARCHAR(250),
	calificacionRepartidor VARCHAR(250),
	calificacionProducto VARCHAR(250),
	numpedido VARCHAR(50),
	PRIMARY KEY(idpedido,numpedido)
	);

CREATE TABLE Pedido(
	numpedido VARCHAR(50) PRIMARY KEY,
	estado VARCHAR(30),
	ubicacion VARCHAR(50),
	precio FLOAT(10),
	telefono INT,
	cedula INT,
	idproducto VARCHAR(30),
	establecimiento VARCHAR(50)
	);

CREATE TABLE MetodoDePago(
	IDmetodoPago VARCHAR(50) PRIMARY KEY,
	idcliente VARCHAR(50) not null,
	NumPedido VARCHAR(50) not null,
	Foreign key (idcliente) references PerfilCiente(idcliente),
	Foreign key (NumPedido) references Pedido(NumPedido)
	);

CREATE TABLE TarjetaDebito(
	IDmetodoPago VARCHAR(50),
	numTarjeta int not null,
	apodo VARCHAR(250) not null,
	FechaExpi DATE not null,
	Foreign key (IDmetodoPago) references MetodoDePago(IDmetodoPago)
	);

CREATE TABLE TarjetaCredito(
	IDmetodoPago VARCHAR(50),
	numTarjeta int not null,
	apodo VARCHAR(250) not null,
	FechaExpi DATE not null,
	Foreign key (IDmetodoPago) references MetodoDePago(IDmetodoPago)
	);

CREATE TABLE Vehiculo(
	idvehiculo VARCHAR(50) PRIMARY KEY,
	color VARCHAR(50) not null,
	cedula VARCHAR(50) not null,
	Foreign key (cedula) references repartidor(cedula)
	);

CREATE TABLE carro(
	idvehiculo VARCHAR(50),
	numMatricula VARCHAR(50) not null,
	modelo VARCHAR(50) not null,
	Foreign key (idvehiculo) references Vehiculo(idvehiculo)
	);

CREATE TABLE motocicleta(
	idvehiculo VARCHAR(50),
	numMatricula VARCHAR(50) not null,
	modelo VARCHAR(50) not null,
	Foreign key (idvehiculo) references Vehiculo(idvehiculo)
	);
CREATE TABLE bicicleta(
	idvehiculo VARCHAR(50),
	modelo VARCHAR(50) not null,
	Foreign key (idvehiculo) references Vehiculo(idvehiculo)
	);

CREATE TABLE Repartidor(
	Cedula INT PRIMARY KEY,
	Nombre varchar(50) not null,
	Telefono INT not null,
	Calificacion varchar(250) not null,
	FechaNacimiento date,
	Email varchar(250) not null,
	numpedido varchar(50)
	);
