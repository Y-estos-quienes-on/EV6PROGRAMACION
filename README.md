# EV5PROGRAMACION
Evidencia 5 Módulo programador. 
Integrantes: 
Llanos Aberastain Fernanda
Moreno Elbio Alejo 
Presta Rocío 
Romano Matías

Profes: Rocío subió los archivos a una rama equivocada, está en la rama de fer y por eso no figura. A Ro se le complicó con el horario de trabajo poder modificar eso, así que Matías sube lo que Ro le pasó directo al repositorio. 
Gracias!! 

Profes:Moreno Alejo hizo los commits en su rama y cuando los mergeo a la main salian los commits ahi pero ahora no sale :,(


SmartHome Solution

Sistema de gestión de dispositivos inteligentes con control de usuarios y privacidad, desarrollado con principios de Programación Orientada a Objetos (POO).

POO SmartHome es una aplicación que permite gestionar dispositivos inteligentes en un hogar. El sistema diferencia entre dos tipos de usuarios: administradores y usuarios generales, cada uno con permisos específicos. Incluye validación de consentimiento de privacidad y registro de auditoría mediante timestamps.

Características Principales

✅ Gestión de Usuarios

Registro y autenticación de usuarios
Roles diferenciados: administrador y usuario general
Validación de datos (email, contraseña, nombre de usuario)
Cambio dinámico de roles

✅ Control de Dispositivos

Crear, actualizar, eliminar y listar dispositivos
Seguimiento de estado de dispositivos (encendido/apagado)
Configuración de dispositivos personalizada
Registro de timestamps para auditoría

✅ Privacidad y Consentimiento

Sistema de consentimiento de privacidad obligatorio
Registro y verificación de aceptación de políticas
Validación antes de usar funcionalidades

✅ Arquitectura Limpia

Separación de capas: presentación, servicios, DAO e dominio
Interfaces para cada DAO

Requisitos

Python 3.7+
SQLite3 (incluido en Python)

Instalación

Clonar o descargar el repositorio
git clone https://github.com/Y-estos-quienes-on/EV5PROGRAMACION.git

No hay dependencias externas, solo Python estándar

Ejecutar la aplicación
    poniendo python main.py en la terminal bash

Al ejecutar por primera vez, se crea automáticamente un usuario administrador:

Usuario: admin
Contraseña: admin123
Email: admin@mail.com

Inicio de sesión / Registro

    Opción de registrar nuevo usuario
    Aceptación obligatoria de política de privacidad
    Iniciar sesión con credenciales


Menú de Usuario General

    Consultar mis datos
    Ver dispositivos asignados
    Ver estado de consentimiento de privacidad


Menú de Administrador

    Consultar datos de usuarios
    Cambiar roles de usuarios
    Gestionar dispositivos (crear, eliminar, cambiar estado)

Ejemplos de Uso

Registrar un nuevo usuario
    === Sistema de Usuarios ===
        Registrar usuario
        Usuario: juan_perez
        Email: juan@example.com
        Contraseña: pass123
        Rol (general/admin): general
        ¿Acepta la política de privacidad? (S/N): S
        Consentimiento registrado.

Iniciar sesión
    Usuario: juan_perez
    Contraseña: pass123
    ¡Bienvenido juan_perez!

Crear dispositivo (Admin)
    === Gestión de Dispositivos ===
    Agregar dispositivo
    Nombre del dispositivo: Luz Salón
    Tipo (luz, cámara, etc.): luz
    Dispositivo 'Luz Salón' agregado con ID 1.

Ver dispositivos
    ID:1 - Luz Salón (luz) - Estado: apagado - Config: default



