from dao.estado_dispositivo_dao import EstadoDispositivoDAO
from dao.configuracion_dispositivo_dao import ConfiguracionDispositivoDAO
from dao.dispositivo_dao import DispositivoDAO
from dominio.dispositivos.dispositivo import Dispositivo
from dominio.dispositivos.estado_dispositivo import EstadoDispositivo
from dominio.dispositivos.configuracion_dispositivo import ConfiguracionDispositivo

class DispositivoService:
    def __init__(self):
        self.estado_dao = EstadoDispositivoDAO()
        self.config_dao = ConfiguracionDispositivoDAO()
        self.dispositivo_dao = DispositivoDAO()

    #Crear dispositivo
    def registrar_dispositivo(self, nombre, tipo):
        estado = EstadoDispositivo()
        id_estado = self.estado_dao.agregar_estado(estado)

        configuracion = ConfiguracionDispositivo()
        id_config = self.config_dao.agregar_configuracion(configuracion)

        dispositivo = Dispositivo(nombre, tipo, estado, configuracion)
        id_dispositivo = self.dispositivo_dao.agregar_dispositivo(dispositivo, id_estado, id_config)

        return f"Dispositivo '{nombre}' agregado con ID {id_dispositivo}."

    #Obtener dispositivo
    def obtener_dispositivo(self, id_dispositivo):
        fila = self.dispositivo_dao.obtener_dispositivo(id_dispositivo)
        if not fila:
            return None

        nombre, tipo, id_estado, id_config = fila

        estado = self.estado_dao.obtener_estado(id_estado)
        configuracion = self.config_dao.obtener_configuracion(id_config)

        return Dispositivo(nombre, tipo, estado, configuracion)

    #Actualizar dispositivo
    def actualizar_dispositivo(self, id_dispositivo, nombre=None, tipo=None, estado=None, configuracion=None):
        fila = self.dispositivo_dao.obtener_dispositivo(id_dispositivo)
        if not fila:
            return "No se encontró el dispositivo con ese ID"

        id_estado, id_config = fila[2], fila[3]

        if nombre or tipo:
            self.dispositivo_dao.actualizar_dispositivo(id_dispositivo, nombre, tipo)
        if estado:
            self.estado_dao.actualizar_estado(id_estado, estado)
        if configuracion:
            self.config_dao.actualizar_configuracion(id_config, configuracion)

        return "Dispositivo actualizado correctamente."

    #Eliminar dispositivo
    def eliminar_dispositivo(self, id_dispositivo):
        fila = self.dispositivo_dao.obtener_dispositivo(id_dispositivo)
        if not fila:
            return "No se encontró el dispositivo con ese ID"

        id_estado, id_config = fila[2], fila[3]

        self.estado_dao.eliminar_estado(id_estado)
        self.config_dao.eliminar_configuracion(id_config)
        self.dispositivo_dao.eliminar_dispositivo(id_dispositivo)

        return "Dispositivo eliminado correctamente."

    #Listar dispositivos
    def listar_dispositivos(self):
        dispositivos = []
        filas = self.dispositivo_dao.obtener_todos_dispositivos()

        for fila in filas:
            id_dispositivo, nombre, tipo, id_estado, id_config = fila
            estado = self.estado_dao.obtener_estado(id_estado)
            configuracion = self.config_dao.obtener_configuracion(id_config)

            dispositivos.append({
                "id": id_dispositivo,
                "nombre": nombre,
                "tipo": tipo,
                "estado": estado.estado_actual if estado else None,
                "configuracion": configuracion.configuracion if configuracion else None
            })
        return dispositivos
