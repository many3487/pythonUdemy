'''condicion = False

while condicion:
    print("ejecutar ciclo while")
else:
    print("fin del ciclo while")
'''
contador =0
while contador <4:
    print(contador)
    contador+=1
else:
    print("fin del ciclo")

i=0
while i < 6:
    print (i)
    i +=1
    #i = i +1

print ("print otro ejercicio \n")

x=5
while x > 0:
    print(x)
    x = x-1

print ("print otro ejercicio \n")

#ciclo for

cadena= "hola"
for letra in cadena:
    print (letra)
else:
    print("fin ciclo for")

#break en ciclos
for letra in 'Holanda':
    if letra == 'a':
        print(f'letra encontrada: {letra}')
        break
else:
       print("fin del ciclo for")

for h in range(6):
    if h % 2 ==0:
        print(f'valor {h}')

#uso de continue

print("otra manera \n")

for l in range(6):
    if l % 2 !=0:
        continue
    print(f'valor: {l}')
