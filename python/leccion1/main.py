print("este es mi saludo desde python ...")
x="este es mi saludo desde python ..."
#con id conozco en donde esta el valor de la variable en memoria

print(id(x))

#declarar tres variables a las cuales se le asignen con cualquier valor

nombre= "many"
telefono= 312434234
email = "elmo@elmo.co"
print(nombre + " " + str(telefono) + " " + email)
#tipos de concatenacion
#en el lado de arriba se encuentra una de las formas ahora vamos con la ,
print( nombre,telefono,email)
#con la coma agrega de forma automatica un espacio
#califica tu dia
dia =int(input("califica tu día del 1 al 10 "))
print("tu día fue de ",dia)

titulo = input("ingrese el valor de un libro ")
autor = input("quien es el autor de ese libro ? ")
print("el titlulo ", titulo,"fue escrito por",autor)