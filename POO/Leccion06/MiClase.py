class MiClase:
    variables_clase = 'valor variable clase'#esta es una variable de clase

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
#metodos estaticos así como se tienen variables de clase, se tienen metodos de clase existen dos tipos de metodos que se pueden asociar a una clase  metodos staticos o metodos de clase de forma especifica
    @staticmethod
    #staticmethodes el decorador para decirle a python que se hará un metodo statico
    #a @staticmethod  a esto se le conoce como decorador
    def metodo_estatico():
        #un metodo estatico recibe los parametros de entrada un metodo estatico no puede acceder a las variables de instancia
        MiClase.variables_clase
        print(MiClase.variables_clase)


#para acceder una variable de clase solo es necesario:

print(MiClase.variables_clase)#llamar a la clase y a su variable
#ahora para acceder al la variable de la instancia, es decir del metodo init se debe crear un objeto, esto se hace de la sigioente manera:

miclase = MiClase('Valor variable instancia')
print(miclase.variable_instancia)

#ACCESO DESDE EL OBJETO
print(f'accedo desde el objeto a  {miclase.variables_clase}')

#otro objero

miclase2 = MiClase('otro valor de la instancia')
print(miclase2.variable_instancia)

#variable clase al vuelo es decir que se puede instanciar en cualquier momento y se realiza de la siguiente manera

MiClase.variable_vuelo="valor variable al vuelo"
print(miclase2.variable_vuelo)

#contexexto estatico, que no se han creado los objetos de la calse

#contexto dinamico cuando ya se han creado los objetos tampoco los metodos pueden acceder a las instancias  para acceder a la variable clase, se debe llamar priumero a la clase

MiClase.metodo_estatico()


#atributo o variable es lo mismo 