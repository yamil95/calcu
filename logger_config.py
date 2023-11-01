import logging
from datetime import datetime
from typing import Any
from typing import Callable


class loger :
    
    def __init__ (self,func:Callable):
        
        self.func = func
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formato_log = logging.Formatter("Nivel del log : %(levelname)s, Hora: %(asctime)s,ubicacion en codigo: funcName %(funcName)s, mensaje : %(message)s")
        salida_consola = logging.StreamHandler()
        salida_consola.setLevel(logging.WARNING)
        self.logger.addHandler(salida_consola)
        self.salida_archivo_log = logging.FileHandler("salida_ejecucion_log.txt")
        self.salida_archivo_log.setFormatter(self.formato_log)
        self.logger.addHandler(self.salida_archivo_log)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        try:
            
            self.logger.debug(f"{self.func.__name__} Operacion  exitosa")
            return self.func(*args, **kwds)

        except Exception as e:
            self.logger.warning(f"ERROR GRAVE DE INGRESO DE DATOS EN LA FUNCION> {self.func.__name__} con EXCEPTION > {e.args[0]}")
        
        