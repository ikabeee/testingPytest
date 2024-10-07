# funciones.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números, lanzando un error si el divisor es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
