import pytest
from string_calculator import add

def test_string_vazia_retorna_zero():
    assert add("") == 0

def test_um_numero():
    assert add("1") == 1

def test_dois_numeros_com_virgula():
    assert add("1,2") == 3

def test_varios_numeros_com_virgula():
    assert add("1,2,3,4,5") == 15

def test_quebra_de_linha():
    assert add("1\n2,3") == 6

def test_delimitador_personalizado():
    assert add("//;\n1;2") == 3

def test_mensagem_negativos():
    with pytest.raises(ValueError, match="-2.*-5"):
        add("1, -2, -3, -5")

def test_entrada_invalida():
    with pytest.raises(ValueError):
        add("1, Daiane")

