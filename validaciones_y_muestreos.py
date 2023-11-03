from logger_config import loger
import os
import time

def imprimir_menu():
    print("#" * 40)
    print("######## Menú de Opciones ########")
    print("#" * 40)
    print("# 1. ingrese el simbolo + para sumar")
    print("# 2. ingrese el simbolo - para restar")
    print("# 3. ingrese el simbolo * para multiplica")
    print("# 4. ingrese el simbolo / para dividir")
    print("# 5. para salir ingrese cero a continuacion de >>>")
    print("#" * 40)



@loger
def imprimir_resultado (operacion:str,numero_1:int,numero_2:int,resultado:int):
        
        print (f"resultado de la operacion {numero_1} {operacion} {numero_2} = {resultado}")
        time.sleep(2)
        os.system("clear")

@loger
def chequear_operacion ():

    operaciones_disponibles = ["+","-","/","*"]
    operacion = input (">>>")
    
    if operacion not in operaciones_disponibles and operacion != "0":
            raise TypeError(f"el valor *{operacion}* no es un una operacion valida ")
    if operacion == "0": raise Exception ("ejecucion finalizada del programa.")
    else:
        return operacion
@loger
def chequear_numeros ():

    try:
        numero_1 = int (input ("ingrese un numero>"))
        numero_2 = int (input ("ingrese un numero>"))
        return numero_1,numero_2
    except:
        raise ValueError ("los valores deben ser del tipo numerico")
             

def ingresar_datos ():
    
    try :

        operacion = chequear_operacion()
        print ("#######puede ingresar hasta 2 numeros########")
        numero_1,numero_2 = chequear_numeros()
        return operacion,numero_1,numero_2
    
    except Exception as e:
        raise e
    

            