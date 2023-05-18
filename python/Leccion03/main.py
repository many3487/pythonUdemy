condicion = True
if(condicion):
    print("condicion verdadera")
else:
    print("condicion falsa")

numero = int(input("ingrese un valor entre 1 y 3 : "))

if numero ==1:
    numeroTexto= "Numero Uno"
elif numero ==2:
    numeroTexto ="Numero Dos"
elif numero ==3:
    numeroTexto="Numero Tres"
else:
    numeroTexto="Valor fuera de rango"


print (f'Número proporcionado {numero} : {numeroTexto}')


mes= int(input("proporciona mes del año (1-12): "))
estacion = None
'''
if estacion == None:
    print("no se ha ingresado ningun valor")
    '''
if mes == 1 or mes==2 or mes ==12:
    estacion='Invierno'
elif mes == 3 or mes ==4 or mes ==5:
    estacion="Primavera"
elif mes == 6 or mes ==7 or mes ==8:
    estacion="Verano"
elif mes == 9 or mes ==10 or mes ==11:
    estacion="Otoño"
else:
    print("Mes Incorrecto")
print (f"la estación es {estacion}")

edad =int(input("ingresa tu edad: "))
if  0 <= edad <=10:
    mensaje=("La infancia es Increible...")
elif edad >10 and edad <=20:
    mensaje =("Muchos cambios y mucho estudio...")
elif edad > 20 and edad<=30:
    mensaje = ("Amor y comienza el trabajo...")
else:
    print("Etapa de la vida no reconocida viejo verde")
print(f"tu edad es  {edad}, {mensaje}")


nota = int(input("ingrese la calificacion: "))

if 0 <= nota < 6:
    mensaje ="F"
elif nota >=6 and nota <7:
    mensaje="D"
elif nota >=7 and nota< 8:
    mensaje="C"
elif nota >= 8 and nota < 9:
    mensaje = "B"
elif nota >= 9 and nota <= 10:
    mensaje ="A"
else:
    mensaje=("valor incorrecto")
print(f"tu nota es de {mensaje}")