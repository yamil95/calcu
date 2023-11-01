class Calculadora:
    
    def __init__(self) -> None:
        
        self.__operaciones = {"+": lambda  a,b: a+b,
                       "-": lambda  a,b: a-b if a>b else b-a,    
                       "*": lambda  a,b: a*b,    
                       "/": lambda  a,b: a/b if b!=0 else None
                    }   
    
    def operar (self,operacion : str , numero_1:int ,numero_2:int )->int:
        try :
            resultado = self.__operaciones[operacion](numero_1,numero_2)
            return resultado
        except Exception as e:
            raise Exception(f"la clave {operacion} no existe")