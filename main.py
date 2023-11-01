

from calculadora import Calculadora
import os
import time
import copy

def imprimir_menu():
    print("#" * 40)
    print("######## Menú de Opciones ########")
    print("#" * 40)
    print("# 1. ingrese el simbolo + para sumar")
    print("# 2. ingrese el simbolo - para sumar")
    print("# 3. ingrese el simbolo * para sumar")
    print("# 4. ingrese el simbolo / para sumar")
    print("#" * 40)

def chequear_operacion ():
    operaciones_disponibles = ["+","-","/","*"]
    operacion = input (">>>")
    operacion_copy = copy.deepcopy(operacion)
    
    if operacion not in operaciones_disponibles:
            operacion = None
            raise TypeError(f"el valor *{operacion_copy}* no es un una operacion valida ")
    else:
        return operacion

def chequear_numeros ():
        try:
            numero_1 = int (input ("ingrese un numero"))
            numero_2 = int (input ("ingrese un numero"))
            return numero_1,numero_2
        except Exception as e:
            raise ValueError("los valores ingresados deben ser del tipo numerico")
        
    
def ingresar_datos ():
    
    
    try :

        operacion = chequear_operacion()
        print ("#######puede ingresar hasta 2 numeros########")
        numero_1,numero_2 = chequear_numeros()
        return operacion,numero_1,numero_2
    
    except Exception as e:
        raise Exception (e.args[0])



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
            print ("Resultado = {}".format(resultado))
            time.sleep(2)
            os.system("clear")
            imprimir_menu()
        except Exception as e :
            print (f"ocurrio un error del tipo : {e.args[0]}")
    
