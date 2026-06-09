from p5 import *
from classes.clases import Cuadrado, Figura

class Ventana(Figura):
    
    def __init__(self):
        self.cuadrado_base = Cuadrado(borde_color="#000000", borde_grosor=2, width=50, height=60, x=0, y=0, relleno="#622E61")
        self.vidrio1 = Cuadrado(borde_color="#2E3437", borde_grosor=2, width=15, height=15, x=5, y=5, relleno="#BFE5F7")  
        self.vidrio2 = Cuadrado(borde_color="#2E3437", borde_grosor=2, width=15, height=15, x=30, y=5, relleno="#BFE5F7") 
        self.vidrio3 = Cuadrado(borde_color="#2E3437", borde_grosor=2, width=15, height=15, x=5, y=30, relleno="#BFE5F7")
        self.vidrio4 = Cuadrado(borde_color="#2E3437", borde_grosor=2, width=15, height=15, x=30, y=30, relleno="#BFE5F7")
        self.base = Cuadrado(borde_color="#000000", borde_grosor=2, width=50, height=10, x=0, y=50, relleno="#3B1D08")

    def dibujar(self):
        self.cuadrado_base.dibujar()
        self.vidrio1.dibujar()
        self.vidrio2.dibujar()
        self.vidrio3.dibujar()
        self.vidrio4.dibujar()
        self.base.dibujar()