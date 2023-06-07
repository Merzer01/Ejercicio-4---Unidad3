from empleado_CP import Empleado
from planta__SC_empleado import Planta
from contratado_SC_empxcont import Contratado
from externo_SC_empxcont import Externo
from datetime import datetime
import csv
import numpy as np

class coleccion:
    __dimension: int
    __cantidad = 0
    __incremento = 5

    def __init__(self, dimension=0, incremento=5):
        self.__emp = np.empty(dimension, dtype=Empleado)
        self.__dimension = dimension
        self.__cantidad = 0
    
    def addempleado(self, x):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__emp.resize(self.__dimension, refcheck=False)
        self.__emp[self.__cantidad] = x
        self.__cantidad += 1
    
    def reads(self):
        self.readplanta()
        self.readcontratado()
        self.readexterno()
        print("DATOS CARGADOS!!!")

    def readplanta(self):   #CARGA DE EMPLEADOS -> PLANTA
        with open ('planta.csv', 'r', encoding='UTF-8') as archivo:
            lector = csv.reader(archivo, delimiter=';')

            for row in lector:
                dni = row[0]
                nomb = row[1]
                direc = row[2]
                tel = row[3]
                sb = row[4]     #sueldo basico
                ant = row[5]    #antiguedad
                p = Planta(dni, nomb, direc, tel, sb, ant)
                self.testdatos(p)
                self.addempleado(p)

    def readcontratado(self):   #CARGA DE EMPLEADOS -> CONTRATADOS
        with open ('contratado.csv', 'r', encoding='UTF-8') as archivo:
            lector = csv.reader(archivo, delimiter=';')

            for row in lector:
                dni = row[0]
                nomb = row[1]
                direc = row[2]
                tel = row[3]
                fi = row[4] #fecha de inicio de contrato
                ff = row[5] #fecha de fin de contrato
                ht = row[6] #horas trabajadas
                c = Contratado(dni, nomb, direc, tel, fi, ff, ht)
                self.addempleado(c)

    def readexterno(self):  #CARGA DE EMPLEADOS -> EXTERNOS
        with open ('externo.csv', 'r', encoding='UTF-8') as archivo:
            lector = csv.reader(archivo, delimiter=';')

            for row in lector:
                dni = row[0]
                nomb = row[1]
                direc = row[2]
                tel = row[3]
                tarea = row[4]  #tarea
                fi = row[5] #fecha de inicio
                ff = row[6] #fecha de fin
                viat = row[7]   #monto de viaticos
                co = row[8] #costo de obra
                sv = row[9] #seguro de vida
                e = Externo(dni, nomb, direc, tel, tarea, fi, ff, viat, co, sv)
                self.addempleado(e)

    def reghoras(self): #opcion 1
        doc = int(input("Ingrese documento del empleado: "))
        ht = int(input("Ingrese la cantidad de horas trabajadas: "))
        i = 0
        band = False

        while i < len(self.__emp) and band == False:
            if self.__emp[i].getdni() == doc and isinstance(self.__emp[i], Contratado):
                self.__emp[i].addhoras(ht)
                band = True
            else: i += 1
        
        if i > len(self.__emp):
            print("Empleado no encontrado!!!")
        else:
            print("Horas actualizadas de {}: {}hs".format(self.__emp[i].getnombre, self.__emp[i].gethoras()))

    def totaltarea(self):   #opcion 2
        total = 0
        fecha_actual = datetime.now().date()
        fecha_actual = fecha_actual.strftime('%Y-%m-%d')
        tarea = str(input("Ingrese nombre de tarea: "))

        for i in range(len(self.__emp)):
            if isinstance(self.__emp[i], Externo) and tarea == self.__emp[i].gettarea() and self.__emp[i].getff() > fecha_actual:
                total += self.__emp[i].getmonto()
        
        print('''
Tarea: {}
Total a pagar: {}$
        '''.format(tarea, total))

    def ayudaeconomica(self):   #opcion 3
        print("Listado de empleados que accederan a la ayuda economica de la empresa")
        print('-'*40)
        for i in range(len(self.__emp)):
            if self.__emp[i].calcularsueldo() < 150000:
                print('''
{}
DNI: {}
Domicilio: {}
                '''.format(self.__emp[i].getnombre(), self.__emp[i].getdni(), self.__emp[i].getdireccion()))

    def sueldos(self):  #OPCION 4
        for i in range(len(self.__emp)):
            print('''
--------------------
{} ({})
Sueldo a pagar: {}$
--------------------
            '''.format(self.__emp[i].getnombre(), self.__emp[i].gettel(), self.__emp[i].calcularsueldo()))  #POLIMORMISMO DE SUBTIPO

    def mostrardatos(self):
        for i in range(len(self.__emp)):
            if isinstance (self.__emp[i], Planta):
                self.__emp[i].mostrar()


    def testdatos(self, d):
        print('''
--------------------
Nombre: {} (Tel: {})
DNI: {}
Domicilio: {}
PLANTA
Sueldo Basico: {}$
Antiguedad: {}
--------------------
        '''.format(d.getnombre(), d.gettelefono(), d.getdni(), d.getdireccion(), d.getbasico(), d.getantiguedad()))