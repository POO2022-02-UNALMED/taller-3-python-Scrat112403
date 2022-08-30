from televisores.marca import Marca
class TV:
    numTV=0
    def __init__(self, marca, estado):
        self.marca=marca
        self.estado=estado     
        self.canal=1
        self.volumen=1
        self.precio=500
        TV.numTV+=1

    
    def setMarca (self, marc):
        self.marca=marc
    def setControl (self, ctrl):
        self.control= ctrl
    def setPrecio (self, price):
        self.precio=price
    def setVolumen (self, vol):
        self.volumen=vol
    def setCanal (self, canal):
        if self.estado==True:
            if 121>self.canal>0:
                self.canal=canal

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

    def setNumTV(num):
        TV.numTV=num

     
    def getNumTV():
        return TV.numTV

    def turnOn (self):
        self.estado=True
    def turnOff (self):
        self.estado= False
    
    def getEstado (self):
        return self.estado
        
    def canalUp(self):
        if self.estado==True:
            if 120>self.canal>=1:
                self.canal+=1
    def canalDown(self):
        if self.estado==True:
            if 120>=self.canal>1:
                self.canal-=1
            
    def volumenUp(self):
        if self.estado==True:
            if 7>self.volumen>=0:
                self.volumen+=1
    
    def volumenDown(self):
        if self.estado==True:
            if 7>=self.volumen>0:
                self.volumen-=1
 
