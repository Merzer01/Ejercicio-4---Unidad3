from empleado_CP import Empleado
from datetime import datetime
import abc
from abc import ABC
#clase hija de la clase empleado
#clase padre de CONTRATADOS Y EXTERNOS
class EmpxContrato(Empleado, ABC):
    __fecha_inicio: None
    __fecha_fin: None

    def __init__(self, doc, nomb, direc, tel, fi, ff):
        super().__init__(doc, nomb, direc, tel)
        self.__fecha_inicio = datetime.strptime(fi, '%Y-%m-%d').date()
        self.__fecha_fin = datetime.strptime(ff, '%Y-%m-%d').date()

    def showvigencia(self):
        print('''
Desde {} - Hasta {}
        '''.format(self.__fecha_inicio, self.__fecha_fin))
    
    def getff(self):
        return self.__fecha_fin