from empxcont_SC_emp import EmpxContrato

#clase hija de EmpxContrato
class Contratado(EmpxContrato):
    __horas_trab: int
    __valor_hora = 750  #variable de clase -> valor de la hora laboral de los contratados
    def __init__(self, doc, nomb, direc, tel, fi, ff, ht):
        super().__init__(doc, nomb, direc, tel, fi, ff)
        self.__horas_trab = ht
    
    def mostrar(self):
        print("Categoria: CONTRATADO")
        print("Vigencia de Contrato")
        super().showvigencia()
        super().showEmpleado()
        print('''
Valor hora: {}$
Horas trabajadas: {}hs
        '''.format(self.__valor_hora, self.__horas_trab))

    def gethoras(self):
        return self.__horas_trab
    def getvalor(self):
        return self.__valor_hora
    
    def addhoras(self, h):
        self.__horas_trab += h

    def calcularsueldo(self):   #POLIMORMISMO DE SUBTIPO
        return self.__horas_trab * self.__valor_hora