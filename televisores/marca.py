class Marca:
    nombre=None
    def __init__(self, nombre):
        self.nombre=nombre
        
    def setNombre (self):
        self.nombre=None
        
    def getNombre(self):
        return Marca.nombre