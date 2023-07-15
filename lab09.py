def olhar_ao_redor(pos_robo: list[int]) -> str:
    """  Verifica se há sujeira nas posições adjacentes ao robô.

    Parâmetros:
        pos_robo (list[int]): indica a linha e a coluna do robô.

    Retorna:
        Uma das seguintes cinco strings, que indicam se há sujeira nos
        arredores e sua posição: 'direita', 'esquerda', 'cima',
        'baixo' ou 'nenhuma'.
    """

    linha_robo: int = pos_robo[0]
    coluna_robo: int = pos_robo[1]

    if linha_robo % 2 == 0:
        # Se a linha for par, a ordem de escaneamento é primeiro à direita
        # e depois à esquerda.
        if coluna_robo < comprimento_quarto:
            if quarto[linha_robo][coluna_robo + 1] == "o":
                return "direita"
        if coluna_robo > 0:
            if quarto[linha_robo][coluna_robo - 1] == "o":
                return "esquerda"
    else:
        # Se a linha for ímpar, a ordem é inversa.
        if coluna_robo > 0:
            if quarto[linha_robo][coluna_robo - 1] == "o":
                return "esquerda"
        if coluna_robo < comprimento_quarto:
            if quarto[linha_robo][coluna_robo + 1] == "o":
                return "direita"
            
    if linha_robo > 0:
        if quarto[linha_robo - 1][coluna_robo] == "o":
            return "cima"
    if linha_robo < largura_quarto:
        if quarto[linha_robo + 1][coluna_robo] == "o":
            return "baixo"

    return "nenhuma"
    

def mover_direita(pos_robo: list[int]) -> list[int]:
    """ Movimenta o robô para a direita."""

    if pos_robo[1] < comprimento_quarto:
        quarto[pos_robo[0]][pos_robo[1]] = "."
        pos_robo[1] += 1
        quarto[pos_robo[0]][pos_robo[1]] = "r"
    printar_saida()

    return pos_robo


def mover_esquerda(pos_robo: list[int]) -> list[int]:
    """ Movimenta o robô para a esquerda."""

    if pos_robo[1] > 0:
        quarto[pos_robo[0]][pos_robo[1]] = "."
        pos_robo[1] -= 1
        quarto[pos_robo[0]][pos_robo[1]] = "r"
    printar_saida()

    return pos_robo


def mover_baixo(pos_robo: list[int]) -> list[int]:
    """ Movimenta o robô para baixo."""

    if pos_robo[0] < largura_quarto:
        quarto[pos_robo[0]][pos_robo[1]] = "."
        pos_robo[0] += 1
        quarto[pos_robo[0]][pos_robo[1]] = "r"
    printar_saida()

    return pos_robo


def mover_cima(pos_robo: list[int]) -> list[int]:
    """ Movimenta o robô para cima."""

    if pos_robo[0] > 0:
        quarto[pos_robo[0]][pos_robo[1]] = "."
        pos_robo[0] -= 1
        quarto[pos_robo[0]][pos_robo[1]] = "r"
    printar_saida()

    return pos_robo


def prox_scan(pos_robo: list[int]):
    """ Determina a próxima casa que o robô iria, se não houvesse sujeira,
    ou a que de fato ele irá, caso não haja.

    Parâmetros:
        pos_robo (list[int]): indica a posição do robô.

    Retorna:
        Retorna uma das seguintes cinco strings, que indica o que o robô
        fará (ou o que faria, se não houvesse sujeira nos arredores):
        'mover baixo', 'mover cima', 'mover direita', 'mover esquerda,
        'desligar'.
    """

    if pos_robo[0] % 2 == 0:  # Se a linha for par
        if pos_robo[1] == comprimento_quarto and pos_robo[0] < largura_quarto:
            pos_prox_scan = "mover baixo"
        elif pos_robo[1] == comprimento_quarto:
            pos_prox_scan = "desligar"
        else:
            pos_prox_scan = "mover direita"

    else:  # Se a linha for ímpar
        if pos_robo[1] == 0 and pos_robo[0] < largura_quarto:
            pos_prox_scan = "mover baixo"
        elif pos_robo[1] == 0:
            pos_prox_scan = "desligar"
        else:
            pos_prox_scan = "mover esquerda"

    return pos_prox_scan


def escaneando(pos_robo: list[int]) -> None:
    """ Referente ao modo escaneando do robô."""

    sujeira = olhar_ao_redor(pos_robo)

    if sujeira != "nenhuma":
        limpando(pos_robo, sujeira)
    else:
        pos_prox_scan = prox_scan(pos_robo)
        match pos_prox_scan:
            case "mover baixo":
                mover_baixo(pos_robo)
            case "mover direita":
                mover_direita(pos_robo)
            case "mover esquerda":
                mover_esquerda(pos_robo)
            case "desligar":
                desligar(pos_robo)


def limpando(pos_robo: list[int], sujeira: str, pos_retorno: list[int] = None) -> None:
    """ Referente ao modo limpando do robô.

    Parâmetros:
        pos_robo (list[int]): indica a posição do robô no
        início da limpeza.
        sujeira (str): indica a posição da sujeira encontrada pela função escaneando.
        pos_retorno (list[int]), opcional: Só será passado caso a função limpando seja
        chamada pela função voltar_escanear. Nesse caso, indica a posição que o robô
        deve retornar após completar a limpeza.

    Retorna:
        None.
    """

    # Se o robô acabou de alterar para o modo limpando e ainda não possui
    # posição de retorno definida.
    if pos_retorno == None:
        pos_retorno = pos_robo[:]
        pos_prox_scan = prox_scan(pos_robo)
        match pos_prox_scan:
            case "mover direita":
                pos_prox_scan = [pos_robo[0], pos_robo[1] + 1]
            case "mover esquerda":
                pos_prox_scan = [pos_robo[0], pos_robo[1] - 1]
            case "mover baixo":
                pos_prox_scan = [pos_robo[0] + 1, pos_robo[1]]

    # Caso o robô ainda não tenha retornado para a posição em que parou o escaneamento
    # qunado encontrou a sujeira.
    else:
        pos_prox_scan = prox_scan(pos_retorno)
        match pos_prox_scan:
            case "mover direita":
                pos_prox_scan = [pos_retorno[0], pos_retorno[1] + 1]
            case "mover esquerda":
                pos_prox_scan = [pos_retorno[0], pos_retorno[1] - 1]
            case "mover baixo":
                pos_prox_scan = [pos_retorno[0] + 1, pos_retorno[1]]
    
    while sujeira != "nenhuma":
        match sujeira:
            case "direita":
                mover_direita(pos_robo)
            case "esquerda":
                mover_esquerda(pos_robo)
            case "baixo":
                mover_baixo(pos_robo)
            case "cima":
                mover_cima(pos_robo)
        # Se o robô parou na posição em que seria o próximo escaneamento.
        if pos_robo == pos_prox_scan:
            pos_prox_scan = prox_scan(pos_robo)
            pos_retorno = pos_robo[:]
            match pos_prox_scan:
                case "mover direita":
                    pos_prox_scan = [pos_robo[0], pos_robo[1] + 1]
                case "mover esquerda":
                    pos_prox_scan = [pos_robo[0], pos_robo[1] - 1]
                case "mover baixo":
                    pos_prox_scan = [pos_robo[0] + 1, pos_robo[1]]
        sujeira = olhar_ao_redor(pos_robo)

    if pos_robo == pos_prox_scan:
        escaneando(pos_robo)
    else:
        voltar_escanear(pos_robo, pos_retorno)


def voltar_escanear(pos_robo: list[int], pos_retorno: list[int]) -> None:
    """ Volta o robô para a posição adequada após sair do modo limpando.

    Parâmetros:
        pos_robo (list[int]): indica a posição do robô.
        pos_retorno (list[int]): indica a posição de retorno do robô.

    Retorna:
        None.
    """

    linha_robo = pos_robo[0]
    coluna_robo = pos_robo[1]
    linha_esperada = pos_retorno[0]
    coluna_esperada = pos_retorno[1]

    if coluna_robo > coluna_esperada:
        while coluna_robo > coluna_esperada:
            pos_robo = mover_esquerda(pos_robo)
            coluna_robo = pos_robo[1]
            sujeira = olhar_ao_redor(pos_robo)
            # Caso o robô encontre alguma sujeira no caminho de retorno, chama
            # a função limpando e encerra a chamada da função atual.
            if sujeira != "nenhuma":
                limpando(pos_robo, sujeira, pos_retorno)
                return
    
    elif coluna_robo < coluna_esperada:
        while coluna_robo < coluna_esperada:
            pos_robo = mover_direita(pos_robo)
            coluna_robo = pos_robo[1]
            sujeira = olhar_ao_redor(pos_robo)
            if sujeira != "nenhuma":
                limpando(pos_robo, sujeira, pos_retorno)
                return
             
    if linha_robo > linha_esperada:
        while linha_robo > linha_esperada:
            pos_robo = mover_cima(pos_robo)
            linha_robo = pos_robo[0]
            sujeira = olhar_ao_redor(pos_robo)
            if sujeira != "nenhuma":
                limpando(pos_robo, sujeira, pos_retorno)
                return
    
    elif linha_robo < linha_esperada:
        while linha_robo < linha_esperada:
            pos_robo = mover_baixo(pos_robo)
            linha_robo = pos_robo[0]
            sujeira = olhar_ao_redor(pos_robo)
            if sujeira != "nenhuma":
                limpando(pos_robo, sujeira, pos_retorno)
                return


def desligar(pos_robo: list[int]) -> None:
    """ Responsável por finalizar o programa, alterando fim para True."""

    global fim
    # Se o robô terminou no canto inferior direito.
    if pos_robo == [largura_quarto, comprimento_quarto]:
        fim = True
    # Se o robô terminou no canto inferior esquerdo.
    else:
        for _ in range(comprimento_quarto):
            mover_direita(pos_robo)
        fim = True


def printar_saida() -> None:
    """ Printa o arranjo atual do quarto para o usuário."""

    for i in range(len(quarto)):
        print(" ".join(quarto[i]))
    
    print()


def main():
    pos_robo: list[int] = [0, 0]   # [linha do robo, coluna do robo]

    numero_linhas = int(input())
    for _ in range(numero_linhas):
        linha = input().split()
        quarto.append(linha)

    global comprimento_quarto, largura_quarto
    comprimento_quarto = len(quarto[0]) - 1   # Máxima pos x do robo
    largura_quarto = len(quarto) - 1   # Máxima pos y do robo

    printar_saida()   # Printa a posição inicial

    global fim
    while not fim:
        escaneando(pos_robo)


if __name__ == "__main__":
    # Define variáveis globais
    quarto: list[list[str]] = []
    comprimento_quarto: int = 0
    largura_quarto: int = 0   
    fim: bool = False   # Define quando o programa deve parar
    main()
