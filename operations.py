# funciones.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        #Genera una exception, indica que se ha producido un error
        raise ValueError("No se puede dividir por cero.")
    return a / b

