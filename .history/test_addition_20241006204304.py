
from operations import sumar, restar, multiplicar, dividir

# test_funciones.py
import pytest
from operations import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(-1, -1) == 0
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 5) == 0

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(-6, 3) == -2
    assert dividir(0, 1) == 0
    with pytest.raises(ValueError, match="No se puede dividir por cero."):
        dividir(1, 0)
