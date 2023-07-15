def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """ Recebe dois vetores e soma seus elementos um a um.

    Caso os vetores possuam diferentes tamanhos, o menor deles recebe
    elementos zero no final até que atinja o tamanho do outro.

    Args:
        vetor1 (list[int]): Um vetor
        vetor2 (list[int]): Outro vetor

    Returns:
        list[int]: Uma list contendo o resultado da soma de vetor1[0] +
        vetor2[0] na posição 0, vetor1[1] + vetor2[1] na posição 1 etc.
        Possui o comprimento igual ao do maior vetor passado como argumento.
    """

    vetor1, vetor2 = iguala_tamanho(vetor1, vetor2, 0)

    resultado = []
    for i in range(len(vetor1)):
        resultado.append(vetor1[i] + vetor2[i])

    return resultado


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """ Recebe dois vetores e subtrai seus elementos um a um.

    Caso os vetores possuam diferentes tamanhos, o menor deles recebe
    elementos zero no final até que atinja o tamanho do outro.

    Args:
        vetor1 (list[int]): Um vetor
        vetor2 (list[int]): Outro vetor

    Returns:
        list[int]: Uma list contendo o resultado de de vetor1[0] - vetor2[0]
        na posição 0, vetor1[1] - vetor2[1] na posição 1 etc. Possui o
        comprimento igual ao do maior vetor passado como argumento.
    """

    vetor1, vetor2 = iguala_tamanho(vetor1, vetor2, 0)

    resultado = []
    for i in range(len(vetor1)):
        resultado.append(vetor1[i] - vetor2[i])

    return resultado


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """ Recebe dois vetores e multiplica seus elementos um a um.

    Caso os vetores possuam diferentes tamanhos, o menor deles recebe
    elementos 1 no final até que atinja o tamanho do outro.

    Args:
        vetor1 (list[int]): Um vetor
        vetor2 (list[int]): Outro vetor

    Returns:
        list[int]: Uma list contendo o resultado de de vetor1[0] * vetor2[0]
        na posição 0, vetor1[1] * vetor2[1] na posição 1 etc. Possui o
        comprimento igual ao do maior vetor passado como argumento.
    """

    vetor1, vetor2 = iguala_tamanho(vetor1, vetor2, 1)

    resultado = []
    for i in range(len(vetor1)):
        resultado.append(vetor1[i] * vetor2[i])

    return resultado


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """ Recebe dois vetores e divide seus elementos um a um.

    Caso os vetores possuam diferentes tamanhos, o menor deles recebe
    elementos 1 no final até que atinja o tamanho do outro.

    Args:
        vetor1 (list[int]): Um vetor
        vetor2 (list[int]): Outro vetor

    Returns:
        list[int]: Uma list contendo o resultado de de vetor1[0] / vetor2[0]
        na posição 0, vetor1[1] / vetor2[1] na posição 1 etc. Possui o
        comprimento igual ao do maior vetor passado como argumento.

        Caso haja uma tentativa de divisão por zero, uma exceção é lançada
        e o vetor1 é retornado sem modificações.
    """

    if len(vetor1) > len(vetor2):
        vetor1, vetor2 = iguala_tamanho(vetor1, vetor2, 1)
    elif len(vetor2) > len(vetor1):
        vetor1, vetor2 = iguala_tamanho(vetor1, vetor2, 0)

    try:
        resultado = []
        for i in range(len(vetor1)):
            resultado.append(vetor1[i] // vetor2[i])

        return resultado

    except ZeroDivisionError:
        print("Erro. Tentativa de divisão por zero")

        return vetor1


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    """ Recebe um vetor e multiplica todos seus elementos por um inteiro.

    Args:
        vetor1 (list[int]): Um vetor
        escalar (int): Um número inteiro

    Returns:
        list[int]: Uma list contendo o resultado de de vetor1[0] * escalar
        na posição 0, vetor1[1] * escalar na posição 1 etc.
    """

    for i in range(len(vetor)):
        vetor[i] *= escalar

    return vetor


def n_duplicacao(vetor1: list[int], n: int) -> list[int]:
    """ Recebe um vetor e concatena-o consigo mesmo n vezes.

    Args:
        vetor1 (list[int]): Um vetor
        n (int): Um número inteiro

    Returns:
        list[int]: Uma list contendo o vetor1 repetido n vezes.
    """

    return vetor1 * n


def soma_elementos(vetor1: list[int]) -> int:
    """ Recebe um vetor e soma seus elementos.

    Args:
        vetor1 (list[int]): Um vetor

    Returns:
        int: A soma de todos os elementos do vetor.
    """

    soma = 0
    for n in vetor1:
        soma += n
    return soma


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    """ Recebe dois vetores, multiplica os elementos correspondentes
    e retorna o resultado.

    Args:
        vetor1 (list[int]): Um vetor
        vetor2 (list[int]): Outro vetor

    Returns:
        int: A soma dos elementos do vetor obtido multiplicando vetor1
        e vetor2.
    """

    vetor = multiplica_vetores(vetor1, vetor2)

    return soma_elementos(vetor)


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """ Recebe dois vetores e multiplica cada elemento do primeiro por
    todos do segundo.

    Caso os vetores possuam diferentes tamanhos, o menor deles recebe
    elementos 1 no final até que atinja o tamanho do outro.

    Args:
        vetor1 (list[int]): Um vetor
        vetor2 (list[int]): Outro vetor

    Returns:
        list[int]: Um vetor que, na posição i, possui a soma de vetor1[i]
        multiplicado por cada elemento de vetor2.
    """

    resultado = []
    for i1 in vetor1:
        soma = 0
        for i2 in vetor2:
            soma += i1 * i2
        resultado.append(soma)

    return resultado


def correlacao_cruzada(vetor1: list[int], mascara: list[int]) -> list[int]:
    """ Recebe dois vetores e multiplica-os seguindo uma regra.

    Para cada elemento de índice i do vetor1, faz (vetor[i] * mascara[0]) +
    (vetor[i + 1] * mascara[1]) + ... + (vetor[i + k] * mascara[k]),
    onde k é o comprimento da mascara, e armazena o resultado na posição
    i do vetor resultado. Note que a processo se repete até o valor
    máximo de i, que é i = (len(vetor1) - k + 1).

    Args:
        vetor1 (list[int]): Um vetor
        mascara (list[int]): Outro vetor, de tamanho menor do que a entrada

    Returns:
        list[int]: Um vetor, de comprimento menor do que a entrada,
        representando o resultado da operação.
    """

    len1 = len(vetor1)
    len2 = len(mascara)
    resultado = []
    for i in range(len1 - len2 + 1):
        soma = 0
        for j in range(len2):
            soma += vetor1[i + j] * mascara[j]
        resultado.append(soma)

    return resultado


def iguala_tamanho(vetor1: list[int], vetor2: list[int],
                   n: int) -> list[list[int]]:
    """ Recebe dois vetores e iguala seus tamanhos.

    Caso os vetores possuam tamanhos distintos, completa o menor deles com
    o inteiro passado até que atinjam o mesmo comprimento.

    Args:
        vetor1 (list[int]): Um vetor
        vetor2 (list[int]): Outro vetor
        n (int): Um inteiro

    Returns:
        list[list[int]]: Uma lista com dois elementos, sendo o primeiro o
        vetor1 e o segundo o vetor2, já com os tamanhos equalizados.
    """

    if len(vetor1) < len(vetor2):
        while len(vetor1) < len(vetor2):
            vetor1.append(n)
    elif len(vetor2) < len(vetor1):
        while len(vetor2) < len(vetor1):
            vetor2.append(n)

    return [vetor1, vetor2]


def main() -> None:
    entrada = input().split(",")
    vetor1 = list(map(lambda n: int(n), entrada))
    operacao = input()

    while operacao != "fim":

        if operacao == "soma_elementos":
            vetor1 = [soma_elementos(vetor1)]

        elif operacao == "n_duplicacao":
            n = int(input())
            vetor1 = n_duplicacao(vetor1, n)

        elif operacao == "multiplicacao_escalar":
            n = int(input())
            vetor1 = multiplicacao_escalar(vetor1, n)

        else:
            entrada = input().split(",")
            vetor2 = list(map(lambda n: int(n), entrada))
            match operacao:
                case "soma_vetores":
                    vetor1 = soma_vetores(vetor1, vetor2)

                case "subtrai_vetores":
                    vetor1 = subtrai_vetores(vetor1, vetor2)

                case "multiplica_vetores":
                    vetor1 = multiplica_vetores(vetor1, vetor2)

                case "divide_vetores":
                    vetor1 = divide_vetores(vetor1, vetor2)

                case "produto_interno":
                    vetor1 = [produto_interno(vetor1, vetor2)]

                case "multiplica_todos":
                    vetor1 = multiplica_todos(vetor1, vetor2)

                case "correlacao_cruzada":
                    vetor1 = correlacao_cruzada(vetor1, vetor2)

                case _:
                    raise ValueError

        print(vetor1)
        operacao = input()


if __name__ == "__main__":
    main()
