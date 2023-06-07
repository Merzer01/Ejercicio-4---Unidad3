from empleado_CP import Empleado

#clase hija de la clase empleado
class Planta(Empleado):
    __basico: int #sueldo basico
    __antiguedad: int
    def __init__(self, doc, nomb, direc, tel, sb, ant):
        super().__init__(doc, nomb, direc, tel)
        self.__basico = sb
        self.__antiguedad = ant
    
    def mostrar(self):
        super().showEmpleado()
        print('''
Categoria: PLANTA
Sueldo Basico: {}
Antiguedad (años): {}
        '''.format(self.__basico, self.__antiguedad))
    
    def getbasico(self):
        return self.__basico
    def getantiguedad(self):
        return self.__antiguedad
    
    def calcularsueldo(self):   #POLIMORMISMO DE SUBTIPO
        return self.__basico + (0.01*self.__basico)*self.__antiguedad