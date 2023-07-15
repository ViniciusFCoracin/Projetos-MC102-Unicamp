def reverter(i: int, j: int) -> str:
    genoma = genoma_atual
    
    primeira_parte = genoma[ : i]
    segunda_parte = genoma[i : j + 1]
    terceira_parte = genoma[j + 1 : ]

    segunda_parte_inv = []
    for g in range(len(segunda_parte) - 1, -1, -1):
        segunda_parte_inv.append(segunda_parte[g])
    segunda_parte_inv = "".join(segunda_parte_inv)

    genoma = primeira_parte + segunda_parte_inv + terceira_parte

    return genoma


def transpor(i: int, j: int, k: int) -> str:
    genoma = genoma_atual

    primeira_parte = genoma[ : i]
    segunda_parte = genoma[i : j + 1]
    terceira_parte = genoma[j + 1 : k + 1]
    quarta_parte = genoma[k + 1 : ]
    genoma = primeira_parte + terceira_parte + segunda_parte + quarta_parte

    return genoma


def combinar(g: str, i: int) -> str:
    genoma = genoma_atual
    
    primeira_parte = genoma[ : i]
    segunda_parte = genoma[i : ]

    genoma = primeira_parte + g + segunda_parte
    return genoma


def concatenar(s: str) -> str:
    genoma = genoma_atual

    genoma += s
    return genoma


def remover(i: int, j: int) -> str:
    genoma = genoma_atual

    primeira_parte = genoma[ : i]
    terceira_parte = genoma[j + 1 : ]

    genoma = primeira_parte + terceira_parte
    return genoma



def transpor_e_reverter(i: int, j: int, k: int) -> str:
    global genoma_atual
    genoma_atual = transpor(i, j, k)
    genoma_atual = reverter(i, k)

    return genoma_atual


def buscar(g: str) -> None:
    lista = genoma_atual.split(g)
    print(len(lista) - 1)


def buscar_bidirecional(g: str) -> None:
    lista1 = genoma_atual.split(g)
    lista2 = reverter(0, len(genoma_atual) - 1).split(g)

    print(len(lista1) + len(lista2) - 2)


def mostrar() -> None:
    print(genoma_atual)


genoma_atual = input()

while True:
    entrada = input()

    match entrada.split()[0]:
        case "reverter":
           i = int(entrada.split()[1])
           j = int(entrada.split()[2])
           genoma_atual = reverter(i, j)
        case "transpor":
           i = int(entrada.split()[1])
           j = int(entrada.split()[2])
           k = int(entrada.split()[3])
           genoma_atual = transpor(i, j, k)
        case "combinar":
           g = entrada.split()[1]
           i = int(entrada.split()[2])
           genoma_atual = combinar(g, i)
        case "concatenar":
           g = entrada.split()[1]
           genoma_atual = concatenar(g)
        case "remover":
           i = int(entrada.split()[1])
           j = int(entrada.split()[2])
           genoma_atual = remover(i, j)
        case "transpor_e_reverter":
           i = int(entrada.split()[1])
           j = int(entrada.split()[2])
           k = int(entrada.split()[3])
           genoma_atual = transpor_e_reverter(i, j, k)
        case "buscar":
           g = entrada.split()[1]
           buscar(g)
        case "buscar_bidirecional":
           g = entrada.split()[1]
           buscar_bidirecional(g)
        case "mostrar":
            mostrar()
        case "sair":
            break
        case _:
            raise ValueError