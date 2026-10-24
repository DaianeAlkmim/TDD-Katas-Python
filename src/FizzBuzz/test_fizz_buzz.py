import pytest
from fizz_buzz import fizz_buzz, fizz_buzz_range

@pytest.mark.parametrize("num, esperado", [
    (1, 1),
    (2, 2),
    (4, 4),
    (7, 7),
])

def test_numero_comum_retorna_mesmo_numero(num, esperado):
    resultado = fizz_buzz(num)
    assert fizz_buzz(num) == esperado
    assert isinstance(resultado, int)

@pytest.mark.parametrize("num", [3, 6, 9, 12])
def test_multiplo_de_tres_retorna_fizz(num):
    assert fizz_buzz(num) == "Fizz"

@pytest.mark.parametrize("num", [5, 10, 20, 25])
def test_multiplo_de_cinco_retorna_buzz(num):
    assert fizz_buzz(num) == "Buzz"

def test_zero_retorna_fizzbuzz():
    assert fizz_buzz(0) == "FizzBuzz"

def test_negativos():
    assert fizz_buzz(-3) == "Fizz"
    assert fizz_buzz(-5) == "Buzz"
    assert fizz_buzz(-15) == "FizzBuzz"
    assert fizz_buzz(-1) == -1

@pytest.mark.parametrize("entrada", [3.0, "doze", None, True, [7]])
def test_entrada_invalida(entrada):
    with pytest.raises(ValueError):
        fizz_buzz(entrada)

def test_range_padrao_vai_de_1_a_100():
    resultado = fizz_buzz_range()
    assert len(resultado) == 100
    assert resultado[0] == 1
    assert resultado[2] == "Fizz"
    assert resultado[14] == "FizzBuzz"
    assert resultado[-1] == "Buzz"

def test_range_com_um_unico_numero():
    assert fizz_buzz_range(5, 5) == ["Buzz"]


def test_range_comecando_no_zero():
    assert fizz_buzz_range(0, 3) == ["FizzBuzz", 1, 2, "Fizz"]

@pytest.mark.parametrize("numero", [15, 30, 45, 90])
def test_multiplo_de_quinze_retorna_fizzbuzz(numero):
    assert fizz_buzz(numero) == "FizzBuzz"


def test_range_com_inicio_maior_que_fim_lanca_erro():
    with pytest.raises(ValueError, match="start must not be greater than end"):
        fizz_buzz_range(10, 1)


def test_range_com_inicio_invalido_lanca_erro():
    with pytest.raises(ValueError, match="start must be an integer"):
        fizz_buzz_range("a", 10)


def test_range_com_fim_invalido_lanca_erro():
    with pytest.raises(ValueError, match="end must be an integer"):
        fizz_buzz_range(1, 10.5)