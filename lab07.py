def descriptografa_caractere(caractere: str, chave: int) -> str:
    """ Descriptografa um caractere, dada a chave de criptografia.

    Args:
        caractere (str): O caractere a ser descriptografado.
        chave (int): A chave de criptografia.

    Returns:
        str: O caractere descriptografado.
    """

    codigo_novo_char: int = ord(caractere) + chave

    # Se o código for superior a 126, subtraímos 95 (quantidade de caracteres
    # imprimíveis). Ex: o código 127 corresponde ao caractere 127 - 95 = 32.
    if codigo_novo_char > 126:
        while codigo_novo_char > 126:
            codigo_novo_char = (codigo_novo_char - 95)

    # Se o código for inferior a 32, devemos subtrair (32 - código) de 127.
    # Ex: O código 31 corresponde ao caractere 127 - (32 - 31) = 126
    elif codigo_novo_char < 32:
        while codigo_novo_char < 32:
            codigo_novo_char = 127 - (32 - codigo_novo_char)

    novo_caractere: str = chr(codigo_novo_char)

    return novo_caractere


def descobrir_chave(operacao: str, primeiro_char: str,
                    segundo_char: str, mensagem: str) -> int:
    """ Descobre a chave de criptografia.

    Args:
        operacao (str): "+", "-" ou "*"
        primeiro_char (str): Primeiro caractere a ser buscado. Possíveis
        valores são "vogal", "consoante", "numero" ou um único caractere.
        segundo_char (str): Segundo caractere a ser buscado. Pode receber
        os mesmos valores que primeiro_char.
        mensagem (str): A mensagem a ser descriptografada.

    Returns:
        int: A chave de criptografia.
    """

    caracteres: dict = {
        "vogal": ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"],
        "consoante": ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M",
                      "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z",
                      "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                      "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"],
        "numero": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    }

    if len(primeiro_char) == 1:
        pos_char1: int = mensagem.index(primeiro_char)
    else:
        for i in range(len(mensagem)):
            if mensagem[i] in caracteres[primeiro_char]:
                pos_char1 = i
                break

    if len(segundo_char) == 1:
        pos_char2: int = mensagem.index(segundo_char, pos_char1)
    else:
        for i in range(pos_char1, len(mensagem)):
            if mensagem[i] in caracteres[segundo_char]:
                pos_char2 = i
                break

    match operacao:
        case "+":
            chave = pos_char1 + pos_char2
        case "-":
            chave = pos_char1 - pos_char2
        case "*":
            chave = pos_char1 * pos_char2
        case _:
            raise ValueError

    return chave


def main() -> None:
    operacao = input()
    primeira_busca = input()
    segunda_busca = input()
    numero_linhas = int(input())
    mensagem: str = ""
    linhas_list: list[str] = []

    i = 1
    while i <= numero_linhas:
        linha = input()
        mensagem += linha
        linhas_list.append(linha)
        i += 1

    chave = descobrir_chave(operacao, primeira_busca, segunda_busca, mensagem)
    print(chave)

    for lista in linhas_list:
        linha_descript: str = ""
        for char in lista:
            novo_char = descriptografa_caractere(char, chave)
            linha_descript += novo_char
        print(linha_descript)


if __name__ == "__main__":
    main()
