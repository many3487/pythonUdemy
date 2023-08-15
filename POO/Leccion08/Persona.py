class Persona:
    def __init__(self,nombre, edad):
        self.nombre= nombre
        self.edad = edad

    def __add__(self, otro):
        return f' {self.nombre} {otro.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

persona1 =Persona("Juan",28)
persona2 =Persona("Carlos",50)
print( persona1 + persona2)
print(persona1 - persona2)


#obj1.__add__(obj2)
#obj1 +obj2

