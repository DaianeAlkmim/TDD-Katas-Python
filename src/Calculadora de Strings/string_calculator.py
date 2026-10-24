import re 

def add(num : str) -> int:
    if num == "":
        return 0

    delimitador = r",|\n"

    if num.startswith("//"):
        cabecalho, num = num.split("\n", 1)
        delimitador = re.escape(cabecalho[2:])

    valores = [int(n) for n in re.split(delimitador, num)]

    negativos = [n for n in valores if n < 0]

    if negativos:
        raise ValueError(f"Negativos não permitidos: {negativos}")
    return sum(valores)