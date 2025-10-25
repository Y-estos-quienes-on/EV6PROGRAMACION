DROP TABLE IF EXISTS UsuariosDispositivos;
DROP TABLE IF EXISTS Dispositivo;
DROP TABLE IF EXISTS Configuracion_Dispositivo;
DROP TABLE IF EXISTS Estado_Dispositivo;
DROP TABLE IF EXISTS ConsentimientoPrivacidad;
DROP TABLE IF EXISTS Usuario;

CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(80) NOT NULL UNIQUE,
    contrasena VARCHAR(30) NOT NULL,
    rol VARCHAR(50) DEFAULT 'General'
);

CREATE TABLE ConsentimientoPrivacidad (
    id_consentimiento INT AUTO_INCREMENT PRIMARY KEY,
    acepta_politicas TINYINT,
    fecha DATETIME,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Estado_Dispositivo (
    id_estado INT AUTO_INCREMENT PRIMARY KEY,
    estado_actual VARCHAR(45),
    ultima_actualizacion DATETIME
);

CREATE TABLE Configuracion_Dispositivo (
    id_configuracion INT AUTO_INCREMENT PRIMARY KEY,
    estado TINYINT,
    configuracion VARCHAR(45),
    time_stamp DATETIME
);

CREATE TABLE Dispositivo (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80),
    tipo_dispositivo VARCHAR(80),
    id_estado INT,
    id_configuracion INT,
    FOREIGN KEY (id_estado) REFERENCES Estado_Dispositivo(id_estado),
    FOREIGN KEY (id_configuracion) REFERENCES Configuracion_Dispositivo(id_configuracion)
);

CREATE TABLE UsuariosDispositivos (
    id_usuario INT NOT NULL,
    id_dispositivo INT NOT NULL,
    PRIMARY KEY (id_usuario, id_dispositivo),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo)
);

INSERT INTO Usuario (usuario, email, contrasena, rol) VALUES
('admin', 'admin@gmail.com', 'admin123', 'Admin'),
('mromano', 'mromano@gmail.com', 'mromano123', 'General'),
('fllanos', 'fllanos@gmail.com', 'fllanos123', 'Admin'),
('emoreno', 'emoreno@gmail.com', 'emoreno123', 'General'),
('rpresta', 'rpresta@gmail.com', 'rpresta123', 'General'),
('jlopez', 'jlopez@gmail.com', 'jlopez123', 'General'),
('cgarcia', 'cgarcia@gmail.com', 'cgarcia123', 'General'),
('psanchez', 'psanchez@gmail.com', 'psanchez123', 'Admin'),
('lrodriguez', 'lrodriguez@gmail.com', 'lrodriguez123', 'General'),
('mfernandez', 'mfernandez@gmail.com', 'mfernandez123', 'General');

INSERT INTO ConsentimientoPrivacidad (acepta_politicas, fecha, id_usuario) VALUES
(1, '2025-07-12 10:25:00', 1),
(0, '2025-09-05 14:12:00', 2),
(1, '2025-08-20 09:40:00', 3),
(0, '2025-09-30 16:30:00', 4),
(1, '2025-10-01 11:15:00', 5),
(1, '2025-07-25 13:45:00', 6),
(1, '2025-08-10 08:50:00', 7),
(0, '2025-10-02 17:20:00', 8),
(1, '2025-09-18 12:05:00', 9),
(0, '2025-10-08 09:30:00', 10);

INSERT INTO Estado_Dispositivo (estado_actual, ultima_actualizacion) VALUES
('Encendido', '2025-10-10 12:10:00'),
('Apagado', '2025-10-11 08:45:00'),
('En espera', '2025-10-09 18:20:00'),
('Mantenimiento', '2025-10-08 15:50:00'),
('Desconectado', '2025-10-07 11:30:00'),
('Error', '2025-10-06 16:00:00'),
('Actualizando', '2025-10-05 14:10:00'),
('Modo Vacaciones', '2025-10-04 09:20:00'),
('Modo Noche', '2025-10-03 22:00:00'),
('Modo Seguridad', '2025-10-02 07:45:00');

INSERT INTO Configuracion_Dispositivo (estado, configuracion, time_stamp) VALUES
(1, 'Modo Noche', '2025-10-01 21:00:00'),
(0, 'Modo Seguridad', '2025-09-28 08:30:00'),
(1, 'Modo Desarrollo', '2025-10-03 14:20:00'),
(1, 'Modo Eco', '2025-09-25 17:45:00'),
(0, 'Modo Proteccion', '2025-09-30 12:15:00'),
(1, 'Modo Invitados', '2025-10-02 19:10:00'),
(0, 'Modo Ausente', '2025-09-29 09:50:00'),
(1, 'Modo Fiesta', '2025-10-04 20:30:00'),
(0, 'Modo Automático', '2025-10-05 10:05:00'),
(1, 'Modo Manual', '2025-10-06 11:40:00');

INSERT INTO Dispositivo (nombre, tipo_dispositivo, id_estado, id_configuracion) VALUES
('Luz Pieza', 'Luz', 1, 1),
('Aire Dormitorio', 'Aire acondicionado', 2, 2),
('Cámara Cocina', 'Camara', 3, 3),
('Alarma Patio', 'Alarma', 4, 4),
('Termostato Sala', 'Termostato', 5, 5),
('Sensor Puerta', 'Sensor', 6, 6),
('Luz Jardín', 'Luz', 7, 7),
('Cámara Garaje', 'Camara', 8, 8),
('Aire Oficina', 'Aire acondicionado', 9, 9),
('Alarma Techo', 'Alarma', 10, 10);

INSERT INTO UsuariosDispositivos (id_usuario, id_dispositivo) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),
(6,6),(7,7),(8,8),(9,9),(10,10),
(1,2),(2,3),(3,4),(4,5),(5,6);

SELECT 'Tabla Usuario' AS Consulta;
SELECT * FROM Usuario;

SELECT 'Tabla ConsentimientoPrivacidad' AS Consulta;
SELECT * FROM ConsentimientoPrivacidad;

SELECT 'Tabla Estado_Dispositivo' AS Consulta;
SELECT * FROM Estado_Dispositivo;

SELECT 'Tabla Configuracion_Dispositivo' AS Consulta;
SELECT * FROM Configuracion_Dispositivo;

SELECT 'Tabla Dispositivo' AS Consulta;
SELECT * FROM Dispositivo;

SELECT 'Tabla UsuariosDispositivos' AS Consulta;
SELECT * FROM UsuariosDispositivos;

SELECT 'CONSULTA MULTITABLA 1: Usuarios con sus dispositivos' AS Consulta;
SELECT 
    U.usuario AS Usuario,
    D.nombre AS Dispositivo,
    D.tipo_dispositivo AS Tipo
FROM Usuario U
JOIN UsuariosDispositivos UD ON U.id_usuario = UD.id_usuario
JOIN Dispositivo D ON UD.id_dispositivo = D.id_dispositivo
ORDER BY U.usuario;

SELECT 'CONSULTA MULTITABLA 2: Estado de dispositivos' AS Consulta;
SELECT 
    D.nombre AS Dispositivo,
    D.tipo_dispositivo AS Tipo,
    E.estado_actual AS Estado,
    E.ultima_actualizacion AS Ultima_Actualizacion,
    C.configuracion AS Configuracion
FROM Dispositivo D
JOIN Estado_Dispositivo E ON D.id_estado = E.id_estado
JOIN Configuracion_Dispositivo C ON D.id_configuracion = C.id_configuracion
ORDER BY E.ultima_actualizacion DESC;

SELECT 'CONSULTA MULTITABLA 3: Auditoria de privacidad' AS Consulta;
SELECT 
    U.usuario AS Usuario,
    U.email AS Email,
    CP.acepta_politicas AS Consentimiento,
    CP.fecha AS Fecha_Consentimiento,
    D.nombre AS Dispositivo,
    D.tipo_dispositivo AS Tipo
FROM Usuario U
JOIN ConsentimientoPrivacidad CP ON U.id_usuario = CP.id_usuario
JOIN UsuariosDispositivos UD ON U.id_usuario = UD.id_usuario
JOIN Dispositivo D ON UD.id_dispositivo = D.id_dispositivo
WHERE CP.acepta_politicas = 1
ORDER BY CP.fecha DESC;


SELECT 'CONSULTA MULTITABLA 4: Luces encendidas' AS Consulta;
SELECT 
    D.nombre AS Dispositivo,
    D.tipo_dispositivo AS Tipo,
    E.estado_actual AS Estado,
    E.ultima_actualizacion AS Encendido_desde
FROM Dispositivo D
JOIN Estado_Dispositivo E ON D.id_estado = E.id_estado
WHERE D.tipo_dispositivo = 'Luz' 
  AND E.estado_actual = 'Encendido';

SELECT 'SUBCONSULTA 1: Usuarios power users' AS Consulta;
SELECT 
    U.usuario AS Usuario,
    U.email AS Email,
    (SELECT COUNT(*) 
     FROM UsuariosDispositivos UD 
     WHERE UD.id_usuario = U.id_usuario) AS Cantidad_Dispositivos
FROM Usuario U
WHERE U.id_usuario IN (
    SELECT id_usuario
    FROM UsuariosDispositivos
    GROUP BY id_usuario
    HAVING COUNT(id_dispositivo) > 1
)
ORDER BY U.usuario;

SELECT 'SUBCONSULTA 2: Admins con dispositivos criticos' AS Consulta;
SELECT 
    U.usuario AS Administrador,
    U.email AS Email,
    COUNT(UD.id_dispositivo) AS Dispositivos_Asignados
FROM Usuario U
LEFT JOIN UsuariosDispositivos UD ON U.id_usuario = UD.id_usuario
WHERE U.rol = 'Admin'
  AND U.id_usuario IN (
    SELECT DISTINCT UD2.id_usuario
    FROM UsuariosDispositivos UD2
    JOIN Dispositivo D ON UD2.id_dispositivo = D.id_dispositivo
    WHERE D.tipo_dispositivo IN ('Camara', 'Alarma')
  )
GROUP BY U.usuario, U.email
ORDER BY U.usuario;