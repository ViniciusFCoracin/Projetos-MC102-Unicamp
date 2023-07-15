def contar_brigas(pares_que_brigam: list, animal_e_proc: dict) -> int: 
    """ Retorna o número de brigas que ocorreram no dia.
    
    O primeiro parâmetro é uma list contendo lists com os nomes dos pares de animais que brigam.
    o segundo parâmetro é um dict, cujas chaves são o nome dos animais que solicitaram atendimento
    naquele dia e cujos valores são a quantidade disponível de procedimentos.

    O retorno é um inteiro que representa o número de brigas que ocorreram no dia.
    """

    brigas: int = 0
    for par in pares_que_brigam:
        if (par[0] in animal_e_proc) and (par[1] in animal_e_proc):
            brigas += 1

    return brigas

def atendido_ou_nao(proc_e_quant: dict, animal_e_proc: dict) -> list:
    """Retorna uma list que contém o resultado do atendimento dos animais no dia.
    
    O primeiro parâmetro é um dict cujas chaves são os procedimentos e cujos valores são
    as quantidades disponíveis de cada. O segundo é um dict cujas chaves são os nomes dos
    animais que vão ao veterinário naquele dia e cujos valores são os procedimentos requisitados
    por cada um.

    O retorno é uma list contendo 3 lists (que podem ser vazias): a primeira contendo os nomes
    dos animais atendidos, a segunda a dos não atendidos e a terceira a dos que solicitaram
    procedimentos não disponíveis
    """

    atendidos: list = []
    nao_atendidos: list = []
    proc_n_disp: list = []

    for animal in animal_e_proc:
        procedimento: str = animal_e_proc[animal]
        try:
            # Se o procedimento procurado está presente como chave no dicionário
            if proc_e_quant[procedimento] == 0:
                nao_atendidos.append(animal)
            else:
                atendidos.append(animal)
                proc_e_quant[procedimento] = proc_e_quant[procedimento] - 1
        except KeyError:
            # Se o procedimento procurado não é chave no dicionário, então não está disponível
            proc_n_disp.append(animal)

    return [atendidos, nao_atendidos, proc_n_disp]

def printar_saida(dia: int, numero_brigas: int, atendidos : list,
                   nao_atendidos: list, nao_disponivel: list) -> None:
    """ Printa as informações do número de brigas e atendimentos em determinado dia"""

    print(f"Dia: {dia}")
    print(f"Brigas: {numero_brigas}")
    if atendidos != []:
        print("Animais atendidos: ", end = "")
        for i in range(len(atendidos) - 1):
            print(atendidos[i], end=", ")
        print(atendidos[len(atendidos) - 1])

    if nao_atendidos != []:
        print("Animais não atendidos: ", end = "")
        for i in range(len(nao_atendidos) - 1):
            print(nao_atendidos[i], end=", ")
        print(nao_atendidos[len(nao_atendidos) - 1])

    if nao_disponivel != []:
        for animal in nao_disponivel:
            print(f"Animal {animal} solicitou procedimento não disponível.")

    print("")

        
numero_dias: int = int(input())

dia = 1
while dia <= numero_dias:
    # Recebe cada par de animal que briga numa list e armazena todos os pares em outra list
    quantidade_de_pares: int = int(input())
    pares_que_brigam: list = []
    for i in range(quantidade_de_pares):
        par: list = input().split()
        pares_que_brigam.append(par)


    # Recebe os procedimentos disponíveis e as entradas numa list e organiza num dict
    entrada_proced_e_quant: list = input().split()
    procedimentos_e_quantidade: dict = {}
    for i in range(0, len(entrada_proced_e_quant), 2):
        procedimentos_e_quantidade[entrada_proced_e_quant[i]] = int(entrada_proced_e_quant[i + 1])

    # Recebe os procedimentos solicitados por cada animal em lists e organiza em dicts
    numero_animais: int = int(input())
    animal_e_proc: dict = {}
    for i in range(numero_animais):
        entrada_anim_e_proc: list = input().split()
        animal_e_proc[entrada_anim_e_proc[0]] = entrada_anim_e_proc[1]

    numero_brigas = contar_brigas(pares_que_brigam, animal_e_proc)
    resultados = atendido_ou_nao(procedimentos_e_quantidade, animal_e_proc)
    atendidos = resultados[0]
    nao_atendidos = resultados[1]
    nao_disponivel = resultados[2]
    printar_saida(dia, numero_brigas, atendidos, nao_atendidos, nao_disponivel)

    dia += 1
