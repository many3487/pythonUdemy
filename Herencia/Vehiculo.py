class Vehiculo:
    def __init__(self, color, ruedas):
        self.color= color
        self.ruedas= int(ruedas)

    def __str__(self):
        return f'Vehiculo: {self.color}, {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = int(velocidad)

    def __str__(self):
        return f'Coche: {super().__str__()}, {self.velocidad}km/h'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta: {super().__str__()}, {self.tipo}'



vehiculo1= Vehiculo('negro',4)
print(vehiculo1)
coche1= Coche('naranja',4,50)
print(coche1)
bicicleta1 = Bicicleta('cromada',2,'fixie')
print(bicicleta1)
