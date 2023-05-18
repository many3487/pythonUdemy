class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):#sobre escribe  la clase padre con esto retorno los valores que se ingresan pero los retorno como un string
        return f'Persona: Nombre: {self.nombre} Edad: {self.edad}'
class Empleado(Persona):#con esto heredo de la clase Persona

    def __init__(self,nombre, edad, sueldo):# se le pasan los parametros que se vana usar el padre en este caso la edad y nombre
        super().__init__(nombre, edad) # cpon esto invoco la clase anterior que sería la clase persona
        self.sueldo= sueldo

    def __str__(self):
        return f'Empleado: {super().__str__()}, {self.sueldo} '#aquí con el metodo super lo que se hace es que se llama a la cadena str ahora lo unico que se debe hacer es ingresar los campos agregados dentro del objeto empleado

"""empleado1 =Empleado('Juan','28',5000)

print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
esta es una prueba del objeto creado
"""


