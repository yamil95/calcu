import logging
from typing import Any
from typing import Callable
import functools


class loger :
    
    
    """ 
    proposito : La clase loger se encargara de decorar aquellas funciones que necesiten ser controladas tanto en si su ejecucion fue exitosa como fallida
    en este caso la configuracion del loger se hara de forma tal que se va a generar un archivo "salida_ejecucion_log.txt" donde se almacenaran los logs de warning
    como de Debug añadiendo tambien mas una salida por consola a los mensajes de Warnings 
    
    precondicion : El loger debe estar decorado en las definiciones de funciones que consideres criticas, para modificar o añadir mensajes al loger deberas modificar
    el metodo __call__ 
    
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formato_log = logging.Formatter("Nivel del log : %(levelname)s, Hora: %(asctime)s,ubicacion en codigo: funcName %(funcName)s, mensaje : %(message)s")
    salida_consola = logging.StreamHandler()
    salida_consola.setLevel(logging.WARNING)
    logger.addHandler(salida_consola)
    salida_archivo_log = logging.FileHandler("salida_ejecucion_log.txt")
    salida_archivo_log.setFormatter(formato_log)
    logger.addHandler(salida_archivo_log)
    
    def __init__ (self,func:Callable):
        
        self.func = func

        functools.update_wrapper(self, func)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        
        validar_parametros = lambda x: f"{x[1]} {x[0]} {x[2]} = {x[3]}" if len (x)>3 else x
        validar = validar_parametros(args)
        
        try:
            self.logger.info (f"Realizando ejecucion de funcion {self.func.__name__}>  ")
            valor = self.func (*args,**kwds)
            self.logger.info (f"ejecucion exitosa de la funcion {self.func.__name__} {validar}")
            
            return valor

        except Exception as e:
            validar_fin = lambda x: "EJECUCION FINALIZADA" if "." in list (x[0]) else "ERROR GRAVE DE INGRESO DE DATOS EN LA FUNCION"
            self.logger.warning(f"{validar_fin(e.args)}> {self.func.__name__}> Tipo de evento > {e.args[0]}")
            raise
        
        