import abc
from abc import ABC

#clase padre
class Empleado (ABC):
    __dni: int
    __nombre: str
    __direccion: int
    __telefono: int
    def __init__(self, doc, nomb, direc, tel):
        self.__dni = doc
        self.__nombre = nomb
        self.__direccion = direc
        self.__telefono = tel

    def showEmpleado(self):
        print('''
-Empleado-
{} - Dni: {}
Dir: {}
Tel:        
        '''.format(self.__nombre, self.__dni, self.__direccion, self.__telefono))

    def getdni(self):
        return self.__dni
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    
    def calcularsueldo(self):   #POLIMORMISMO DE SUBTIPO
        pass
