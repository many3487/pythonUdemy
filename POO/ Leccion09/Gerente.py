from Empleado import Empleado

class Gerente(Empleado):#se extiende es decir que trae el metodo empleado
    def __int__(self, departamento, nombre, sueldo):
        super().__int__(nombre, sueldo)#se inicializa es decir se llaman las variables del metodo anterior
        self.departamento = departamento

    def __str__(self):
        return f'[Departamento: {self.departamento}] {super().__str__()}'