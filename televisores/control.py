from televisores.tv import TV
class Control:
        
            def __init__(self):
                self.tv= None
    
            def turnOn (self):
                self.tv.turnOn()
            def turnOff (self):
                self.tv.turnOff()
    
            def getEstado (self):
                return TV.estado
            
            def canalUp(self):
                if self.estado==True:
                    if 120>self.canal>=1:
                        TV.canalUp+=1
            def canalDown(self):
                if self.estado==True:
                    if 120>=self.canal>1:
                        TV.canalDown-=1
            
            def volumenUp(self):
                if self.estado==True:
                    if 7>self.volumen>=0:
                        TV.volumenUp+=1
    
            def volumenDown(self):
                if self.estado==True:
                    if 7>=self.volumen>0:
                        TV.volumenDown-=1

            def setCanal (self, can):
                TV.canal=can
        

            def enlazar (self,tv):
                self.tv=tv
                self.tv.setControl(self)
    
            def setTV (self, tv):
                self.tv=tv

            def getTV (self):
                return self.tv


                