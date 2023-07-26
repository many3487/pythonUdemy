#ABC = Abstract Base Class

from abc import ABC, abstractmethod
#no se puede instanciar una clase abstracta
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    #para encapsular una variable solamente es necesario agregar el guion bajo antes de el nombre como se ve anteriormente, es decir self._ancho
    #acontinuacion se ponen los metodos set y get
    @property
    def ancho(self):
        return self._ancho
    #este es el metodo set

    #ahora vamos con el metodo get
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto
#ahora se manda a llamar el metodo str para sobre escribir y que nos mande a imprimir directamente la dirección de memoria de la clase object sino que imprima los valores de ancho y largo
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho} Alto:{self._alto}]'
    #rellenar relleno de - se hace así
    print('hola'.center(50, '-'))