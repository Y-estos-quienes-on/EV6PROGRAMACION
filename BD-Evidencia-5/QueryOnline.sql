create table Usuario(
id_usuario int identity(1,1) primary key,
usuario  varchar(50) not null unique,
email varchar(80) not null unique,
contrase�a varchar(30) not null,
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
--Insert Usuario
insert into Usuario (usuario, email, contrase�a, rol) values ('admin', 'admin@gmail.com', 'admin123', 'Admin')
--Insert Usuario
insert into Usuario (usuario, email, contrase�a) values ('mromano', 'mromano@gmail.com', 'mromano123')
--Insert Usuario
insert into Usuario (usuario, email, contrase�a, rol) values ('fllanos', 'fllanos@gmail.com', 'fllanos123', 'Admin')
--Insert Usuario
insert into Usuario (usuario, email, contrase�a) values ('emoreno', 'emoreno@gmail.com', 'General')
--Insert Usuario
insert into Usuario (usuario, email, contrase�a) values ('rpresta', 'rpresta@gmail.com', 'General')
--Insert Consentimiento de Privacidad
insert into ConsentimientoPrivacidad (id_consentimiento, acepta_politicas, fecha, id_usuario) values (1, 1, GETDATE(), 1)
--insert Consentimiento de Privacidad
insert into ConsentimientoPrivacidad (id_consentimiento, acepta_politicas, fecha, id_usuario) values (2, 0, GETDATE(), 2)
--insert Consentimiento de Privacidad
insert into ConsentimientoPrivacidad (id_consentimiento, acepta_politicas, fecha, id_usuario) values (3, 1, GETDATE(), 3)
--insert Consentimiento de Privacidad
insert into ConsentimientoPrivacidad (id_consentimiento, acepta_politicas, fecha, id_usuario) values (4, 0, GETDATE(), 4)
--insert Consentimiento de Privacidad
insert into ConsentimientoPrivacidad (id_consentimiento, acepta_politicas, fecha, id_usuario) values (5, 1, GETDATE(), 5)
--insert Estado del Dispositivo
insert into Estado_Dispositivo (id_estado, estado_actual, ultima_actualizacion) values (1, 'Encendido', GETDATE())
--insert Estado del Dispositivo
insert into Estado_Dispositivo (id_estado, estado_actual, ultima_actualizacion) values (2, 'Apagado', GETDATE())
--insert Estado del Dispositivo
insert into Estado_Dispositivo (id_estado, estado_actual, ultima_actualizacion) values (3, 'En espera', GETDATE())
--insert Configuracion del Dispositivo
insert into Configuracion_Dispositivo (id_configuracion, estado, configuracion, time_stamp) values (1, 1, 'Modo Noche', GETDATE())
--insert Configuracion del Dispositivo
insert into Configuracion_Dispositivo (id_configuracion, estado, configuracion, time_stamp) values (2, 0, 'Modo Seguridad', GETDATE())
--insert Configuracion del Dispositivo
insert into Configuracion_Dispositivo (id_configuracion, estado, configuracion, time_stamp) values (3, 1, 'Modo en desarrollo', GETDATE())
--insert Dispositivo
insert into Dispositivo (id_dispositivo, nombre, tipo_dispositivo, id_estado, id_configuracion) values (1, 'Luz Pieza', 'Luz', 1, 1)
--insert Dispositivo
insert into Dispositivo (id_dispositivo, nombre, tipo_dispositivo, id_estado, id_configuracion) values (2, 'Aire Dormitorio', 'Aire acondicionado', 2, 2)
--insert Dispositivo
insert into Dispositivo (id_dispositivo, nombre, tipo_dispositivo, id_estado, id_configuracion) values (3, 'C�mara Cocina', 'Camara', 3, 3)
--insert Dispositivo
insert into Dispositivo (id_dispositivo, nombre, tipo_dispositivo, id_estado, id_configuracion) values (4, 'Alarma Patio', 'Alarma', 1, 2)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (1, 1)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (2, 2)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (3, 3)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (4, 1)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (5, 4)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (1, 2)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (2, 3)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (3, 4)
--insert Usuarios y sus dispositivos
insert into UsuariosDispositivos (id_usuario, id_dispositivo) values (4, 2)

--consulta: "Quiero visualizar las automatizaciones que estan encendidas"
select * from Configuracion_Dispositivo CD
where CD.estado = 1

--consulta: "Quiero ver los usuarios que no aceptaron el consentimiento"
select * from ConsentimientoPrivacidad CP
where CP.acepta_politicas != 1

--consulta: "Quiero saber los dispositivos de luz y de camara que tengo"
select * from Dispositivo D
where D.tipo_dispositivo = 'Luz' OR D.tipo_dispositivo = 'Camara'

--consulta: "Quiero saber los estados disponibles que tengo"
select ED.estado_actual
from Estado_Dispositivo ED

--consulta: "Quiero visualizar los usuarios que tengan rol de administrador"
select U.Usuario, U.rol, U.email
from Usuario U
where U.rol = 'admin'

--consulta: "Quiero saber los dispositivos del usuario de mromano"
SELECT U.usuario,U.rol, D.nombre AS NombreDispositivo, D.tipo_dispositivo AS Tipo
FROM Usuario U
JOIN UsuariosDispositivos UD ON U.id_usuario = UD.id_usuario
JOIN Dispositivo D ON UD.id_dispositivo = D.id_dispositivo
where U.usuario = 'mromano'