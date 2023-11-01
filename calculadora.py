class Calculadora:
    """_summary_
    """
    def __init__(self) -> None:
        
        self.__operaciones = {"+": lambda  a,b: a+b,
                       "-": lambda  a,b: a-b if a>b else b-a,    
                       "*": lambda  a,b: a*b,    
                       "/": lambda  a,b: a/b if b!=0 else None
                    }   
    
    def operar (self,operacion : str , numero_1:int ,numero_2:int )->int:
        resultado = self.__operaciones[operacion](numero_1,numero_2)
        return resultado
            