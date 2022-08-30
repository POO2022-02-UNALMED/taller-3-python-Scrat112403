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
                        self.tv.canalUp+=1
            def canalDown(self):
                if self.tv.estado==True:
                    if 120>=self.tv.canal>1:
                        self.tv.canalDown-=1
            
            def volumenUp(self):
                if self.tv.estado==True:
                    if 7>self.tv.volumen>=0:
                        self.tv.volumenUp+=1
    
            def volumenDown(self):
                if self.tv.estado==True:
                    if 7>=self.tv.volumen>0:
                        self.tv.volumenDown-=1

            def setCanal (self, can):
                self.tv.canal=can
        

            def enlazar (self,tv):
                self.tv=tv
                self.tv.setControl(self)
    
            def setTV (self, tv):
                self.tv=tv

            def getTV (self):
                return self.tv


                