operadoA=6
operandoB=8
suma = operandoB + operadoA
#impresion normal
print("resultado: ",suma)
#cadenas F o print format
print(f"resultado: {suma}")

#ejercicio
alto = int(input("ingrese el alto: "))
ancho = int(input("ingrese el ancho: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f"el área es de : {area}")
print(f"el  perimetro es de {perimetro}")

#ejercicio

a =int(input("ingrese un número: "))
if(a%2 ==0):
    print("es par")
else:
    print("es impar")

#para nop cerrar la cadena se pone un \
print("proporcione los tados del libro: ")
name = input("Proporcione el nombre del libro: ")
id= int(input("ingrese el ID del libro: "))
precio= float(input("ingrese el precio del libro: "))
envio = bool(input("indica si el envio es gratuito (True / False"))

print(f"nombre: {name} \n Id: {id} \n Precio: {precio} \n Envio gratuito ? : {envio}")