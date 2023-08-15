from Orden import Orden
from Producto import Producto

producto1 = Producto('camisa', 100.00)
producto2 = Producto('pantalon', 150.00)
productos1 = [producto1, producto2]
producto4= Producto('calcetines', 50.00)
producto5=Producto('blusa', 70.00)
orden1=Orden(productos1)
print(orden1)
print(orden1.calcular_total())
producto3 = Producto('jeans', 200.00)
productos2=[producto1, producto3, producto2]
orden2=Orden(productos2)
print(orden2)
productos3=[producto1, producto3, producto4, producto5, producto2]
orden3=Orden(productos3)
print(orden3)