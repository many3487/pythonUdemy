nombres =["Juan","Karla","Ricardo","Maria"]
#imprimir la lista de nombre
print (nombres)
#acceder
print(nombres[0])
#acceder de manera inversa
print(nombres[-1])

#acceder a elementos de la lista con exepción con el ultimo número -1 (lo imprime como un arreglo)
print(nombres[0:2])#sin incluir el indice 2
#ir del inicio de la lista al indice(sin incluirlo)
print(nombres[ : 3])
#desde el indice indicado haste  el final
print(nombres[1:])
#cambiar valor de la lista
nombres[3] = 'ivonne'
print(nombres)
#iterar una listra
for nombre in nombres:
    print (nombre)
else:
    print("no existen mas nombres en la lista")

#preguntar cuantos elementos tiene o el largo de una lista
print(len(nombres))
#agregae elemento
nombres.append('lorenzo')
print(nombres)
#insertar elemento en indica proporcionado o en especifico o en campo especifico
nombres.insert(1,'octavio')
print(nombres)
#revomer o eliminar elemento
nombres.remove('octavio')
print(nombres)
#remover el ultimo valor agregado
nombres.pop()
print(nombres)
#eliminar un elemento en un indice indicafo
del nombres[1]
print (nombres)
#limpiar elementos de la lista es decir borrar todos los elementosde la lista
nombres.clear()
print(nombres)
#borrar la lista por completo
'''
del nombres #en este caso envia un error ya que los elementos de la lista han sido removidos
print(nombres)
'''
#sintaxis de range(inicio <opcional>, fin<requerido>,incremento<opcional>)
for num in range(11):
    if num % 3 ==0:
        print(num)
print("\n")
for nume in range (2,7):
    print(nume)
print("\n")
for nuevo_numero in range(3,11,2):
    print(nuevo_numero)


print("\n")

#tuplas
#las tuplas siguen guardando los datos y esta no se pueden ni modificar ni borrar ni agregar cuando se trabajan con tuplas es importante poner una , al final
frutas =("naranja","platano","guayaba",)
print (frutas)
#largo de una tupla
print(len(frutas))
#acceder a un elemento en particulas
print(frutas[2])
#navegacion inversa
print(frutas[-2])
#rango de valores
print(frutas[0:1])#sun incluir indice2

print(f"aquì empieza el for \n")
for fruta in frutas:
    print (fruta, end=' ')#aquì se usa end= para que no me haga un salto de linea es decir para que no haga \n sino que agrege un espacio y que imprima en linea recta
#cambiar el valor de una tupla
#frutas[0]='pera'# n las tuplas no se pueden modificar por tanto esta funcion no funciona
#print (frutas)
#de tupla a lista
frutasLista= list(frutas) #aqui estamos pasando una tupla a una lista
frutasLista[0]="pera"
print("\n")
frutas = tuple(frutasLista)#aquí se vuelve a convertir la lista a una tupla

print(frutas)
print(frutasLista)
#eliminar la tupla cpor completo
del frutas #aquí se elimino la tupla
#print(frutas)


#dada la siguiente tupla
#crear una lista que solo incluya los números menores a 5
tupla = (13,1,8,3,2,5,8)
tuplaLista=list(tupla)
print(tuplaLista)
numeros =[]
for numero in tuplaLista:
    if numero <5:
        numeros.append(numero)

print(numeros)

#tipo set
print ("tipo set")
#a diferencia el no mantiene un orden, ni tampoco permite agregar elementos duplicados no es posible modificar los elementos en un set, pero si es posible agregar mas elementos o eliminarlos
#los set se decharan con llaves {} las tuplas con corchetes() y las listas con llaves cuadradas[]
planetas = {"Marte", "Venus", "Júpiter"}
print (planetas)
print("\n")
print(len(planetas))
#revisar si esta presente un elemento
print('Marte' in planetas)
print('Martes' in planetas)
#agregar mas elementos
planetas.add("Tierra")#se agrega un nuevo elemento
print(planetas)
#no elementos duplicados
planetas.add("Tierra")
#eliminar elemento
planetas.remove('Tierra')
print(planetas)
#eliminar elemento aqui se elimina si el elemento no existe en la lista
#planetas.remove('Tierras')
#print(planetas)
#otra forma de eliminar sin arrojar errores en caso de que no se encuentre el elemento
planetas.discard('Júpiter')
print(planetas)
#eliminar todos los elementos
planetas.clear()
print(planetas)
#eliminar por completo el set
#del planetas
#print(planetas)
#diccionarios
print ("\n")
print("diccionarios")
#los diccionarios estan compuestos de una llave y un valor
#dict(key,value)
diccionario= {
    'IDE': 'Integrated Development Eniroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': "Database Management System"
}
print(diccionario)
#largo
print(len(diccionario))
#para acceder a un elementos se debe proporcionar la llave del elemento
print(diccionario['IDE'])

#otra forma de recuperar elementos
print(diccionario.get('OOP'))
#modificar elementos
diccionario['IDE']='integrated development enviroment'
print(diccionario)

#recorrer elementos en un diccionario
for termino in diccionario:
    print(termino)
#solo puedo acceder al termino más no al valor es decir no los dos al tiempo si no con una funcion items
for termino, valor in diccionario.items():
    print(termino, valor)
#si quiero solo las llaves
for termino in diccionario.keys():
    print(termino)

#si quiero solo los valores
for valor in diccionario.values():
    print(valor)

#comprobar si existe un elementos en un diccionario
print('IDE' in diccionario)
#agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
#eliminar o remover un elemento del diccionario
diccionario.pop('DBMS')
print(diccionario)

#limpiar diccionario
diccionario.clear()
print(diccionario)

#eliminar variable por completo
del diccionario
print(diccionario)






