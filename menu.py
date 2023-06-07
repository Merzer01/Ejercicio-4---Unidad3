class Menu(object):
    def showmenu(self):
        print("MENU DE OPCIONES")
        print("1 - Registrar horas")
        print("2 - Total de tarea")
        print("3 - Ayuda economica")
        print("4 - Calcular sueldo")
        print("5 - Mostrar datos")
        print("0 - Salir")
        cond = False
        while not cond:
            op = int(input("Ingrese numero de opcion: "))
            if op in [1,2,3,4,0]:
                cond = True
        return op