from coleccion import coleccion
from menu import Menu
import os

if __name__ == '__main__':
    os.system('cls')
    c = coleccion()
    c.reads()

    band = True
    while band:
        m = Menu()
        opcion = m.showmenu()
        if opcion == 1:
            c.reghoras()
        elif opcion == 2:
            c.totaltarea()
        elif opcion == 3:
            c.ayudaeconomica()
        elif opcion == 4:
            c.sueldos()
        elif opcion == 5:
            c.mostrardatos()
        elif opcion == 0:
            print("Saliendo...")
            band = False
        else: print("Opcion incorrecta!!!")
        os.system('pause')
        os.system('cls')