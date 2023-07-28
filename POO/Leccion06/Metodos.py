class MiClase:
    variables_clase = 'valor variable clase'#esta es una variable de clase

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
#metodos estaticos así como se tienen variables de clase, se tienen metodos de clase existen dos tipos de metodos que se pueden asociar a una clase  metodos staticos o metodos de clase de forma especifica
    @staticmethod
    #staticmethodes el decorador para decirle a python que se hará un metodo statico
    #a @staticmethod  a esto se le conoce como decorador
    #un metodo estaticio no recibe informacion de la clase es decir un metodo estatico no tiene información directamente relacionada con la clase así que este metodo no tiene relacion con la clase

    def metodo_estatico():
        #un metodo estatico recibe los parametros de entrada un metodo estatico no puede acceder a las variables de instancia
        MiClase.variables_clase
        print(MiClase.variables_clase)

        #metodo de clase
        #para definir un metodo de clase se usa el siguiente decorador:
    @classmethod
    def metodo_clase(cls):

        #estos metodos si reciben los metodos de la clase
        #con cls accedo a las variables de clase es decir ya no es necesario utilizar el nombre de la clase
        print(cls.variables_clase)



print(MiClase.variables_clase)

miclase = MiClase('Valor variable instancia')
print(miclase.variable_instancia)

print(f'accedo desde el objeto a  {miclase.variables_clase}')

miclase2 = MiClase('otro valor de la instancia')
print(miclase2.variable_instancia)

MiClase.variable_vuelo="valor variable al vuelo"
print(miclase2.variable_vuelo)


#contexto dinamico cuando ya se han creado los objetos tampoco los metodos pueden acceder a las instancias  para acceder a la variable clase, se debe llamar priumero a la clase

MiClase.metodo_estatico()


#atributo o variable es lo mismo

print("aqui")
MiClase.metodo_clase()