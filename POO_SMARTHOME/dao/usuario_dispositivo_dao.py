from dominio.usuarios.base import Usuario
from dominio.dispositivos.dispositivo import Dispositivo
from conn.conn_db import DBConnection

class UsuarioDispositivoDAO:
    def __init__(self):
        try:
            with DBConnection() as cursor:
                cursor.execute("SELECT COUNT(*) FROM UsuariosDispositivos")
                print("Tabla UsuariosDispositivos verificada")
        except Exception as e:
            print(f"Error al verificar tabla: {e}")
            raise

    def asignar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "INSERT IGNORE INTO UsuariosDispositivos (id_usuario, id_dispositivo) VALUES (%s, %s)",
                    (id_usuario, id_dispositivo)
                )
        except Exception as e:
            print(f"Error al asignar dispositivo: {e}")
            raise

    def quitar_dispositivo(self, id_usuario: int, id_dispositivo: int):
        try:
            with DBConnection() as cursor:
                cursor.execute(
                    "DELETE FROM UsuariosDispositivos WHERE id_usuario=%s AND id_dispositivo=%s",
                    (id_usuario, id_dispositivo)
                )
        except Exception as e:
            print(f"Error al quitar dispositivo: {e}")
            raise

    def obtener_dispositivos_de_usuario(self, id_usuario: int):
        try:
            with DBConnection() as cursor:
                cursor.execute("""
                    SELECT d.id_dispositivo, d.nombre, d.tipo_dispositivo, d.id_estado, d.id_configuracion
                    FROM Dispositivo d
                    JOIN UsuariosDispositivos ud ON d.id_dispositivo = ud.id_dispositivo
                    WHERE ud.id_usuario = %s
                """, (id_usuario,))
                filas = cursor.fetchall()
                
                # Importamos los DAOs necesarios
                from dao.estado_dispositivo_dao import EstadoDispositivoDAO
                from dao.configuracion_dispositivo_dao import ConfiguracionDispositivoDAO
                from dominio.dispositivos.estado_dispositivo import EstadoDispositivo
                from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo
                
                estado_dao = EstadoDispositivoDAO()
                config_dao = ConfiguracionDispositivoDAO()
                
                dispositivos = []
                for f in filas:
                    id_disp, nombre, tipo, id_estado, id_config = f
                    
                    # Obtener estado y configuración
                    estado_data = estado_dao.obtener_estado(id_estado)
                    config_data = config_dao.obtener_configuracion(id_config)
                    
                    # Crear objetos de estado y configuración
                    estado = EstadoDispositivo(
                        id_estado=id_estado,
                        estado_actual=estado_data['estado_actual'] if estado_data else 'apagado'
                    )
                    
                    configuracion = ConfiguracionDispositivo(
                        id_configuracion=id_config,
                        estado=config_data['estado'] if config_data else 1,
                        configuracion=config_data['configuracion'] if config_data else 'default'
                    )
                    
                    # Crear dispositivo completo
                    dispositivo = Dispositivo(
                        id_dispositivo=id_disp,
                        nombre=nombre,
                        tipo_dispositivo=tipo,
                        estado=estado,
                        configuracion=configuracion
                    )
                    dispositivos.append(dispositivo)
                
                return dispositivos
        except Exception as e:
            print(f"Error al obtener dispositivos de usuario: {e}")
            raise

    def obtener_usuarios_de_dispositivo(self, id_dispositivo: int):
        try:
            with DBConnection() as cursor:
                cursor.execute("""
                    SELECT u.id_usuario, u.usuario, u.email, u.contrasena, u.rol
                    FROM Usuario u
                    JOIN UsuariosDispositivos ud ON u.id_usuario = ud.id_usuario
                    WHERE ud.id_dispositivo = %s
                """, (id_dispositivo,))
                filas = cursor.fetchall()
                
                usuarios = []
                for f in filas:
                    usuario = Usuario(
                        id_usuario=f[0],
                        usuario=f[1],
                        email=f[2],
                        contraseña=f[3],
                        rol=f[4]
                    )
                    usuarios.append(usuario)
                
                return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios de dispositivo: {e}")
            raise