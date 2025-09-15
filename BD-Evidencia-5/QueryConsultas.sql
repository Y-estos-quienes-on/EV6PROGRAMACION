use SmartHome
--Insert Usuario
insert into Usuario (usuario, email, contraseña, rol) values ('admin', 'admin@gmail.com', 'admin123', 'Admin')
--Insert Usuario
insert into Usuario (usuario, email, contraseña) values ('mromano', 'mromano@gmail.com', 'mromano123')
--Insert Usuario
insert into Usuario (usuario, email, contraseña, rol) values ('fllanos', 'fllanos@gmail.com', 'fllanos123', 'Admin')
--Insert Usuario
insert into Usuario (usuario, email, contraseña) values ('emoreno', 'emoreno@gmail.com', 'General')
--Insert Usuario
insert into Usuario (usuario, email, contraseña) values ('rpresta', 'rpresta@gmail.com', 'General')
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
insert into Dispositivo (id_dispositivo, nombre, tipo_dispositivo, id_estado, id_configuracion) values (3, 'Cámara Cocina', 'Camara', 3, 3)
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

--consulta: "Quiero visualizar los usuarios que aceptaron las políticas de privacidad"
select U.Usuario, CP.acepta_politicas, CP.fecha
from Usuario U
INNER JOIN  ConsentimientoPrivacidad CP on U.id_usuario = CP.id_usuario
where CP.acepta_politicas = 1

--consulta: "Quiero ver los dispositivos configurados y su estado actual"
select D.nombre, D.tipo_dispositivo, E.estado_actual, E.ultima_actualizacion
from Dispositivo D 
INNER JOIN Estado_Dispositivo E on D.id_estado = E.id_estado

--consulta: "Quiero saber los dispositivos del usuario de mromano"
select U.usuario, D.nombre as dispositivo
from Usuario U
inner join UsuariosDispositivos UD on U.id_usuario = UD.id_usuario
inner join Dispositivo D on UD.id_dispositivo = D.id_dispositivo
where U.usuario = 'mromano'