from empxcont_SC_emp import EmpxContrato

#clase hija de EmpxContratos
class Externo(EmpxContrato):
    __tarea: str
    __viatico: int
    __costo_obra: int
    __seguro_vida: int
    def __init__(self, doc, nomb, direc, tel, tarea, fi, ff, viat, co, sv):
        super().__init__(doc, nomb, direc, tel, fi, ff)
        self.__tarea = tarea
        self.__viatico = viat
        self.__costo_obra = co
        self.__seguro_vida = sv
    
    def mostrar(self):
        print("Categoria: EXTERNO")
        print("Vigencia de Trabajo")
        super().showvigencia()
        super().showEmpleado()
        print('''
Tarea: {}
Viaticos: {}
Costo de obra: {}
Seguro de vida: {}
        ''',format(self.__tarea, self.__inicio, self.__fin, self.__viatico, self.__costo_obra, self.__seguro_vida))

    def gettarea(self):
        return self.__tarea
    def getmonto(self):
        return self.__costo_obra
    def getviatico(self):
        return self.__viatico
    def getseguro(self):
        return self.__seguro_vida

    def calcularsueldo(self):   #POLIMORMISMO DE SUBTIPO
        return self.__costo_obra - self.__viatico - self.__seguro_vida