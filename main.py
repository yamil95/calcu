

from calculadora import Calculadora
import os
import time
from validar_datos import *

def imprimir_menu():
    print("#" * 40)
    print("######## Menú de Opciones ########")
    print("#" * 40)
    print("# 1. ingrese el simbolo + para sumar")
    print("# 2. ingrese el simbolo - para sumar")
    print("# 3. ingrese el simbolo * para sumar")
    print("# 4. ingrese el simbolo / para sumar")
    print("# 5. para salir ingrese cero a continuacion de >>>")
    print("#" * 40)




if __name__ == '__main__':
    
    imprimir_menu()
    calculadora_x = Calculadora()
    
    operacion= None
    numero_1 = None
    numero_2 = None
    
    while operacion != 0:
        try:
            operacion,numero_1,numero_2 = ingresar_datos()
            resultado = calculadora_x.operar(operacion,numero_1,numero_2)
            print (f"Resultado = {resultado}")
            time.sleep(2)
            os.system("clear")
            imprimir_menu()
        except Exception as e :
            if "0" in list (e.args[0]):break
            print (f"ocurrio un error del tipo : {e.args[0]}")


    

