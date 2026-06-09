from p5 import *

class Borde:

    def __init__(self, grosor, color):
        self.grosor = grosor
        self.color = color

    def __str__(self):
        return f"Borde[grosor={self.grosor}, color={self.color}]"


class Dimension:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Dimension[width={self.width}, height={self.height}]"


class Posicion:

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        return f"Posicion[x={self.coord_x}, y={self.coord_y}]"

#La clase Cuadrado cambio a Figura
class Figura:
    def __init__(self,borde_grosor,borde_color,width,height,x,y,relleno,borde:Borde=None):

        if borde is None:
            self.borde = Borde(borde_grosor,borde_color)
        else:
            self.borde = borde
            
        self.dimension = Dimension(width,height)
        self.posicion = Posicion(x,y)

        self.relleno = relleno

    def __str__(self):

        return (
            f"Cuadrado[{self.borde}, "
            f"{self.dimension}, "
            f"{self.posicion}, "
            f"relleno={self.relleno}]"
        )

    def dibujar(self):

        stroke_weight(self.borde.grosor)
        stroke(self.borde.color)
        fill(self.relleno)
        rect(self.posicion.coord_x,self.posicion.coord_y,self.dimension.width,self.dimension.height)

class Cuadrado(Figura):
    ...
class Elipse(Figura):
     def dibujar(self):

        stroke_weight(self.borde.grosor)
        stroke(self.borde.color)
        fill(self.relleno)
        ellipse(self.posicion.coord_x,self.posicion.coord_y,self.dimension.width,self.dimension.height)

if __name__ == "__main__":

    borde = Borde(3, "#15326")
    print(borde)

    cuadrado = Cuadrado(2,"#000000",50,50,10,10,"#FFFFFF")
    elipse = Elipse(2,"#FF004C",50,50,300,200,"#2F5EC5")

    print(cuadrado)
    print(elipse)