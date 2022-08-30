from televisores.tv import TV
if __name__=="__main__":
        class Control:
        
            def __init__(self, tv):
                self.tv= TV
    
            def turnOn (self):
                TV.turnOn()
            def turnOff (self):
                TV.turnOff()
    
            def getEstado (self):
                return TV.estado
            
                if estado=="On":
                    def canalUp(self,canal):
                        if 120>canal>=1:
                            TV.canalUp()
                        else:
                            self.canal= canal
            
                    def canalDown(self,canal):
                        if 120>=canal>1:
                            TV.canalDown()
                        else:
                            self.canal= canal
        
                if estado=="On":
                    def volumenUp(self,volumen):
                        if 7>volumen>=0:
                            TV.volumenUp()
                        else:
                            self.volumen=volumen
    
                    def volumenDown(self,volumen):
                        if 7>=volumen>0:
                            TV.volumenDown()
                        else:
                            self.volumen=volumen

            def setCanal (self, can):
                TV.canal=can
        

            def enlazar (self, televisor):
                self.tv=televisor
                TV.setControl(self)
    
            def settv (self, tv):
                self.tv=tv

            def gettv (self):
                return self.tv