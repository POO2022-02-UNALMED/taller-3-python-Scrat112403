from televisores.tv import TV
class Control:
        
    def __init__(self):
        self.tv= None
    
    def turnOn (self):
        self.tv.turnOn()
    def turnOff (self):
        self.tv.turnOff()
    
    def getEstado (self):
        return self.tv.estado
            
    def canalUp(self):
        if self.tv.estado==True:
            if 120>self.tv.canal>=1:
                self.tv.canalUp()
    def canalDown(self):
        if self.tv.estado==True:
            if 120>=self.tv.canal>1:
                self.tv.canalDown()
            
    def volumenUp(self):
        if self.tv.estado==True:
            if 7>self.tv.volumen>=0:
                self.tv.volumenUp()
    
    def volumenDown(self):
        if self.tv.estado==True:
            if 7>=self.tv.volumen>0:
                self.tv.volumenDown()

    def setCanal (self,canal):
        if self.tv.estado==True:
            if 121>self.tv.canal>0:
                self.tv.setCanal=canal

    def getCanal (self):
        return self.canal
        

    def enlazar (self,tv):
        self.tv=tv
        self.tv.setControl(self)
    
    def setTv (self, tv):
        self.tv=tv

    def getTv (self):
        return self.tv

                