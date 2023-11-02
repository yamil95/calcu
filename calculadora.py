from logger_config import loger
class Calculadora:
    """ 
    proposito: Esta clase se encarga de realizar operacion aritmeticas basicas tales como 
    sumar restar dividir y multiplicar, dichas operaciones estan bindeadas por medio de un diccionario que contiene
    el simbolo (clave) asociadas a su funcion lambda que se encargara de realizar las operaciones aritmeticas 
    realizando tambien las validaciones pertinentes para poder operar
    
    precondicion: Para poder realizar las operaciones aritmeticas primero se debe instanciar un objeto de clase y 
    utilizar el metodo operar() que recibe 3 parametros en este formato (+,2,4) donde en el primer valor es el signo
    de la operacion y el resto los numeros con los que se va operar, el metodo nos devuelve un valor del tipo entero
    
    """
    def __init__(self) -> None:
        
        self.__operaciones = {"+": lambda  a,b: a+b,
                       "-": lambda  a,b: a-b if a>b else b-a,    
                       "*": lambda  a,b: a*b,    
                       "/": lambda  a,b: a/b if b!=0 else None
                    }   
    
    def operar (self,operacion:str,numero_1:int,numero_2:int)->int:
        resultado = self.__operaciones[operacion](numero_1,numero_2)
        return resultado
            