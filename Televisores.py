def __init__():
    class Marca:
        def __init__(self, nombre):
            self.nombre=nombre
        
        def getNombre (self):
            return self.nombre
        
        def setNombre (self, name):
            self.nombre=name
    
    from Televisores import Marca
    if __name__=="__main__":
        class TV:
            def __init__(self, marca, canal, precio, estado, volumen, control):
                self.marca= Marca
                self.canal= canal
                self.precio= precio
                self.estado= estado
                self.volumen= volumen
                self.control=control

            def __init__(self, marca, estado):
                self.marca=Marca
                self.estado=estado

            canal=1
            volumen=1
            precio=500

            def setMarca (self, marc):
                self.marca=marc
            def setControl (self, ctrl):
                self.control= ctrl
            def setPrecio (self, price):
                self.precio=price
            def setVolumen (self, vol):
                self.volumen=vol
            def setCanal (self, can):
                self.canal=can

            def getMarca (self):
                return self.marca
            def getControl (self):
                return self.control
            def getPrecio (self):
                return self.precio
            def getVolumen (self):
                return self.volumen
            def getCanal (self):
                return self.canal


    
            numTV= 0
            def nuevoTV():
                numTV= numTV+1 

            def turnOn (self, On):
                self.estado=On
            def turnOff (self, Off):
                self.estado=Off
    
            def getEstado (self):
                return self.estado
            
                if estado=="On":
                    def canalUp(self,canal):
                        if 120>canal>=1:
                            self.canal= canal+1
                        else:
                            self.canal= canal
            
                    def canalDown(self,canal):
                        if 120>=canal>1:
                            self.canal= canal-1
                        else:
                            self.canal= canal
            
        
                if estado=="On":
                    def volumenUp(self,volumen):
                        if 7>volumen>=0:
                            self.volumen= volumen+1
                        else:
                            self.volumen=volumen
    
                    def volumenDown(self,volumen):
                        if 7>=volumen>0:
                            self.volumen= volumen-1
                        else:
                            self.volumen=volumen

    from Televisores import TV
    if __name__=="__main__":
        class Control:
        
            def __init__(self, tv):
                self.tv= TV
    
            def turnOn (self, On):
                self.estado=On
            def turnOff (self, Off):
                self.estado=Off
    
            def getEstado (self):
                return self.estado
            
                if estado=="On":
                    def canalUp(self,canal):
                        if 120>canal>=1:
                            self.canal= canal+1
                        else:
                            self.canal= canal
            
                    def canalDown(self,canal):
                        if 120>=canal>1:
                            self.canal= canal-1
                        else:
                            self.canal= canal
        
                if estado=="On":
                    def volumenUp(self,volumen):
                        if 7>volumen>=0:
                            self.volumen= volumen+1
                        else:
                            self.volumen=volumen
    
                    def volumenDown(self,volumen):
                        if 7>=volumen>0:
                            self.volumen= volumen-1
                        else:
                            self.volumen=volumen

            def setCanal (self, can):
                self.canal=can
        

            def enlazar (self, televisor):
                self.tv=TV
                self.control: Control
    
            def settv (self, tv):
                self.tv=tv

            def gettv (self):
                return self.tv
