create database SmartHome
use SmartHome

create table Usuario(
id_usuario int identity(1,1) primary key,
usuario  varchar(50) not null unique,
email varchar(80) not null unique,
contraseña varchar(30) not null,
rol varchar(50) default 'General',
)
create table ConsentimientoPrivacidad(
id_consentimiento int primary key,
acepta_politicas tinyint,
fecha datetime,
id_usuario int,
foreign key (id_usuario) references Usuario(id_usuario)
)
create table Estado_Dispositivo(
id_estado int primary key,
estado_actual varchar(45),
ultima_actualizacion datetime
)
create table Configuracion_Dispositivo(
id_configuracion int primary key,
estado tinyint,
configuracion varchar(45),
time_stamp datetime
)
create table Dispositivo(
id_dispositivo int primary key,
nombre varchar(80),
tipo_dispositivo varchar(80),
id_estado int,
id_configuracion int,
foreign key (id_estado) references Estado_Dispositivo(id_estado),
foreign key (id_configuracion) references Configuracion_Dispositivo(id_configuracion)
)
create table UsuariosDispositivos(
id_usuario int not null,
id_dispositivo int not null,
primary key (id_usuario, id_dispositivo),
foreign key (id_usuario) references Usuario(id_usuario),
foreign key (id_dispositivo) references Dispositivo(id_dispositivo)
)
