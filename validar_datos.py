def chequear_operacion ():
    """_summary_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    operaciones_disponibles = ["+","-","/","*"]
    operacion = input (">>>")
    
    if operacion not in operaciones_disponibles:
            raise TypeError(f"el valor *{operacion}* no es un una operacion valida ")
    else:
        return operacion

def chequear_numeros ():
    """_summary_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
        
    try:
        numero_1 = int (input ("ingrese un numero>"))
        numero_2 = int (input ("ingrese un numero>"))
        return numero_1,numero_2
    except:
        raise ValueError ("los valores deben ser del tipo numerico")
             
        
    
def ingresar_datos ():
    """_summary_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    
    
    try :

        operacion = chequear_operacion()
        print ("#######puede ingresar hasta 2 numeros########")
        numero_1,numero_2 = chequear_numeros()
        return operacion,numero_1,numero_2
    
    except Exception as e:
        raise e