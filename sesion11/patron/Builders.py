from classes.clases import *


class Builder:
    def configBorde(self, borde_grosor:int, borde_color:int):
        self._borde_color = borde_color
        self._borde_grosor = borde_grosor
        return self
    
    def configColor(self, color:str):
        self._color_relleno = color
        return self
    
    def configPosicion(self, x:float, y:float):
        self._coord_x = x
        self._coord_y = y
        return self

    def configDefinicion(self, width:int = 50, height:int = 50):
        self._widht = width
        self._height = height
        return self

    def esElipse(self):
        self.esElipse = True
        return self

    def build(self):
        if self.esElipse == False:
            variable = {
                'width':self._width, 'height':self._height, 'borde_grosor':self._borde_grosor, 'borde_color':self._borde_color, 'x':self._coord_x, 'y':self._coord_y, 'relleno':self._relleno
            }
#           return Cuadrado(width=50, height=50, borde_color=self._borde_color, borde_grosoe=self._borde_grosor, x=50, y=50, relleno=self._color_relleno)
#           return Cuadrado(width=variable['width'], height=variable['height'], borde_color=variable['borde_color'], borde_grosor=variable['borde_grosor'], x=variable['x'], y=variable['y'], relleno=variable['relleno'])
            return Cuadrado(**variable)
        else:
#           return Elipse(width=variable['width'], height=variable['height'], borde_color=variable['borde_color'], borde_grosor=variable['borde_grosor'], x=variable['x'], y=variable['y'], relleno=variable['relleno'])
            return Elipse(**variable)

    #width,height,x,y,relleno,velocidad_x,velocidad_y
    ...

#class ElipseBuilder:
#    def build():
#        return Cuadrado(width=50, height=50, borde_color=self.borde_color, borde_grosoe=self.borde_grosor, x=50, y=50, relleno=self.color_relleno):