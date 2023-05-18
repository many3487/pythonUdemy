def mi_funcion():
    print("soludos desde mi funcion")
mi_funcion()

#funciones con parametros

def miFuncion(nombre, apellido):
    print(f"saludos desde mi funcion  {nombre} {apellido}")

miFuncion("many","jimenez")

#palabra return
def sumar(a,b):
    return a + b

print("\n usando palabra return  \n" )
resultado= sumar(3,5)
print(resultado)
print(f"el resultado de la suma es : {resultado}")
print(f"una suma más de la funcion sumar {sumar(8, 4)}")
#asignacion de valores por default

def otraSuma(a=0,b=0) ->int:#en el caso de -> es una pista de que es lo que va a devolver estoes opcional
    return a+b

resul= otraSuma()

print(f"el resultado de la suma es : {resul}")
print(f"una suma más de la funcion sumar {otraSuma(8,4)}")

#pasar argumentos variables a una funcion en python
print("\n pasar varias variables \n")
def listarNombres(*nombres):#al poner * se le indica a la funcion que va a tener n cantidad de nombres es decir va a tener la cantidad infinita o la que se le vayan agragando internamente python la convertiria en una tupla
    for nombre in nombres:
        print(nombre)
listarNombres('juan','carla','maria','hernesto','pedro')

#ejercicio de funciones para sumar
'''
crear una funcion para sumar valores recibidos de tipo numerico,
utilizando argumentos variables (*args) como parámetro de la funcion
y regresar como resultado la suma de todos los valores
'''
def sumatoria(*num):
    suma = 0
    for numero in num:
        suma += numero
        
    return suma


resultado = sumatoria(1,5,4,7,8,6,4,7,8,6,6,5)
print(resultado)

'''
crear una funcion para multiplicar los valores recibidos de tipo num
utilizando argumentos variables *args como parametro de la funcion 
y regresar como resultado la multiplicacion de todos los valores pasados como argumentos.
'''


def mul(*numeros):
    resultado = 1
    for valor in numeros:
        resultado *= valor
    return resultado


print(mul(5, 8, 8, 5, 4))


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'elmo', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')


# para manejar un diccionario
def listarTerminos(
        **terminos):  # se usa dos ** para que se tome como un diccionario o kwars es decir los parametros de un diccionario
    for llave, valor in terminos.items():
        print(f'{llave} : {valor} ')


listarTerminos(IDE='integrated develomet enviroment',
               PK='Primary Key')  # la llave no necesita comillas cuando s epasa de forma directa
listarTerminos(DBMS='Database management System')


# funcion que reciba una liosta de elementos
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Maria', 'Carla', 'guillermo']
desplegarNombres(nombres)
desplegarNombres(
    'elmo')  # aqui es porque se esta manejando un string y envia letra por letra si se envía un int este no sería iterable se podrían enviar si se convierte en tupla también se puede pasar una lista


# funciones recursivas esta es una funcion que se manda a llamar así misma para completar una tarea
# ejemplo el factorial
# 5! = 5 * 4 * 3 * 2 *1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


resultado = factorial(5)
print(f'el factorial de 5 es  {resultado}')

'''
imprimir los numeros de 5 a 1 de manera descendente usando funciones recursivas.
puede ser cualquier valor positivo, ejemplo si pasamor el valor de 5 debe imprimir
5
4
3
2
1 
en sado de el valor 3
3
2
1 


'''


def valoresDes(numero):
    if numero < 1:
        return 1
    else:
        print(numero)
        respuesta = numero - valoresDes(numero - 1)
        return respuesta


num = 5
resultado = valoresDes(num)


# otra manera de ejercicio
def Imp_valores_recursivos(numero):
    if numero >= 1:
        print(numero)
        Imp_valores_recursivos(numero - 1)
    elif numero == 0:
        return 0
    elif numero <= 0:
        print('valor incorrecto ...')


Imp_valores_recursivos(9)

'''
ejercicio:  Calculadora de Impuestos
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
#formula = pago_total = pago_sin_impuestos+ pago_sin_impuestos *(impuestos/100)

'''

pago_sin_impuestos = float(input("proporcione el pago sin impuestos: "))
impuestos= float(input("proporcione el pago de impuestos: "))

def pago(pago_sin_impuestos,impuestos):
    pago_total= pago_sin_impuestos + pago_sin_impuestos *(impuestos/100)
    print(f'pago con impuesto: {pago_total}')
    return pago_total

pago(pago_sin_impuestos , impuestos)

'''
Ejercicio: convertidor de Temperatura
Realizar dos funciones para convertir de grados celcius a fahrenheit y viceversa.
'''

def celcius(fahrenheit):
    Celcius = (fahrenheit - 32)/1.8
    return Celcius
fahrenheit = float(input(" ingrese los grados fahrenheit : "))

print(f"los grados fahrenheit {fahrenheit} a celcius  son : { celcius(fahrenheit)}´")

def fahrenheit(celcius):
    fahrenheit = celcius *1.8 + 32
    return fahrenheit
celcius = float(input(f"ingrese los grados Celcius: "))
print(f"los grados {celcius}  a fahrenheit son: {fahrenheit(celcius)}")






