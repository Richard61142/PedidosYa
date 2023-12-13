create database if not exists pedidosya;
use pedidosya;

create table establecimiento(
	idestablecimiento varchar(50) primary key not null,
	ubicacion varchar(50),
	calificacion float(10),
	distancia float(10)
	);
    
create table producto(
	idproducto varchar(50) primary key not null,
    precio float(10) not null,
    descripcion varchar(30) not null,
    descuento float(10) null
    
);

create table repartidor(
	cedula int primary key not null,
    nombre varchar(50) not null,
    calificacion varchar(50) null,
    fechanacimiento date,
    email varchar(50)
    
);

CREATE TABLE Cliente(
Telefono INT PRIMARY KEY,
email VARCHAR(50),
fecha_nacimiento date,
cedula INT,
direccion VARCHAR(50),
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
nombre VARCHAR(250),
correo VARCHAR(250),
telefono INT
);

CREATE TABLE Establecimiento(
idEstablecimiento VARCHAR(50),
numpedido VARCHAR(50),
ubicacion VARCHAR(250),
calificacion FLOAT(10),
distancia FLOAT(10),
telefono INT,
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

CREATE TABLE Metodo de Pago(
IDmetodoPago VARCHAR(50) PRIMARY KEY,
idcliente VARCHAR(50) not null,
NumPedido VARCHAR(50) not null,
Foreign key (idcliente) references PerfilCiente(idcliente),
Foreign key (NumPedido) references Pedido(NumPedido)
);
