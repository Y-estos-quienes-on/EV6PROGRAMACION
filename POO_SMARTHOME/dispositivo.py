from typing import List, Optional

class Dispositivo:
    def __init__(self, nombre: str, tipo: str, estado: str = "apagado"):
        self.nombre = nombre
        self.tipo = tipo.lower()
        self.estado = estado.lower()

    def cambiar_estado(self, nuevo_estado: str):
        self.estado = nuevo_estado.lower()


class GestorDispositivos:
   
    
    def __init__(self):
        self.dispositivos: List[Dispositivo] = []
    
    def agregar_dispositivo(self, nombre: str, tipo: str, estado: str = "apagado") -> Dispositivo:
     
        if self.buscar_por_nombre(nombre):
            raise ValueError(f"Ya existe un dispositivo con nombre '{nombre}'")
        
        dispositivo = Dispositivo(nombre, tipo, estado)
        self.dispositivos.append(dispositivo)
        return dispositivo
    
    def eliminar_dispositivo(self, nombre: str) -> bool:
        dispositivo = self.buscar_por_nombre(nombre)
        if dispositivo:
            self.dispositivos.remove(dispositivo)
            return True
        return False
    
    def modificar_estado_dispositivo(self, nombre: str, nuevo_estado: str) -> bool:
        dispositivo = self.buscar_por_nombre(nombre)
        if dispositivo:
            dispositivo.cambiar_estado(nuevo_estado)
            return True
        return False
    
  
    def buscar_por_nombre(self, nombre: str) -> Optional[Dispositivo]:
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == nombre:
                return dispositivo
        return None
    
    
    def listar_dispositivos(self) -> List[Dispositivo]:
        return self.dispositivos.copy()
    
    def filtrar_por_tipo(self, tipo: str) -> List[Dispositivo]:
        return [d for d in self.dispositivos if d.tipo == tipo.lower()]
    
    def filtrar_por_estado(self, estado: str) -> List[Dispositivo]:
        return [d for d in self.dispositivos if d.estado == estado.lower()]
    
   
