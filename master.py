import os
from time import sleep
#By eloywin

def menu():
    limpiar_consola()
    print("Software de finanzas personal.\n")
    print("[1]Mostrar resumen.")
    print("[2]Añadir gastos.")
    print("[3]Añadir ingresos")
    
    entrada = input("\n==>")

    if entrada == "1":
        pass
    elif entrada == "2":
        pass
    elif entrada == "3":
        pass
    else:
        print("OPCION DESCONOCIDA")
        sleep(2)
        menu()

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


menu()