def user_entries() -> list[dict, list]:
    """ Obtém as entradas do usuário e as organiza.

    As entradas relativas aos filmes são organizadas em um dict chamado filme.
    Cada chave desse dicionário é um novo dicionário, com o nome de cada
    filme. Por sua vez, cada um desses dicts possui as chaves 'pontos totais',
    'quantas venceu', 'não avaliado' e 'nome', além de cinco outros dicts, um
    para cada categoria simples que os filmes concorrem.

    As entradas relativas às avaliações são armazenadas numa list
    bidimensional, em que cada uma das lists internas possui 4 elementos: o
    avaliador, a categoria, o filme e a nota.

    Retorna uma list contendo dois elementos:
    o dict filmes, e a list avaliacoes.
    """

    quant_filmes: int = int(input())
    filmes: dict = {}
    for _ in range(quant_filmes):
        filme: str = input()
        filmes[filme] = {
            "filme que causou mais bocejos": {
                "pontos": 0,
                "avaliacoes": 0,
                "media": 0
            },
            "filme que foi mais pausado": {
                "pontos": 0,
                "avaliacoes": 0,
                "media": 0
            },
            "filme que mais revirou olhos": {
                "pontos": 0,
                "avaliacoes": 0,
                "media": 0
            },
            "filme que não gerou discussão nas redes sociais": {
                "pontos": 0,
                "avaliacoes": 0,
                "media": 0
            },
            "enredo mais sem noção": {
                "pontos": 0,
                "avaliacoes": 0,
                "media": 0
            },
            "pontos totais": 0,
            "não avaliado": True,
            "quantas venceu": 0,
            "nome": filme,
        }

    quant_aval: int = int(input())
    avaliacoes: list[list[str]] = []
    for _ in range(quant_aval):
        avaliacao: list[str] = input().split(", ")
        avaliacoes.append(avaliacao)

    return [filmes, avaliacoes]


def calcular_notas(filmes: dict, avaliacoes: list):
    """ Computa os pontos e calcula as médias.

    Recebe como parâmetros o dict filmes e a list avaliacoes.

    Retorna o dict filmes modificado, contendo os pontos em cada categoria,
    médias, pontos totais e se o filme foi avaliado pelo menos uma vez ou não.
    """

    # Em cada categoria, calcula os pontos e a média.
    for avaliacao in avaliacoes:
        avaliador, categoria, filme, nota = avaliacao
        nota = int(nota)

        filmes[filme][categoria]["pontos"] += nota
        filmes[filme][categoria]["avaliacoes"] += 1
        filmes[filme][categoria]["media"] = filmes[filme][categoria]["pontos"] / filmes[filme][categoria]["avaliacoes"]

    # Calcula a soma de todos os pontos e se foi avaliado pelo menos uma vez.
    for filme in filmes:
        soma = 0
        for categoria in filmes[filme]:
            if type(filmes[filme][categoria]) == dict:
                soma += filmes[filme][categoria]["media"]
                if filmes[filme][categoria]["avaliacoes"] != 0:
                    filmes[filme]["não avaliado"] = False
        filmes[filme]["pontos totais"] = soma

    return filmes


def definir_vencedores(filmes):
    """ Recebe o dict filmes e retorna os vencedores."""

    vencedores = {
        # categoria: [nota_vencedor, avaliacoes_vencedor, vencedor]
        "filme que causou mais bocejos": [0, 0, None],
        "filme que foi mais pausado": [0, 0, None],
        "filme que mais revirou olhos": [0, 0, None],
        "filme que não gerou discussão nas redes sociais": [0, 0, None],
        "enredo mais sem noção": [0, 0, None],
    }

    vencedores_especiais = {
        "não merecia estar aqui": [],
        "pior filme do ano": None
    }

    for filme in filmes:
        for categoria in filmes[filme]:
            if categoria in vencedores:
                if filmes[filme][categoria]["media"] > vencedores[categoria][0]:
                    vencedores[categoria][0] = filmes[filme][categoria]["media"]
                    vencedores[categoria][1] = filmes[filme][categoria]["avaliacoes"]
                    vencedores[categoria][2] = filmes[filme]["nome"]
                elif (filmes[filme][categoria]["media"] == vencedores[categoria][0]
                      and filmes[filme][categoria]["avaliacoes"] > vencedores[categoria][1]):
                    vencedores[categoria][0] = filmes[filme][categoria]["media"]
                    vencedores[categoria][1] = filmes[filme][categoria]["avaliacoes"]
                    vencedores[categoria][2] = filmes[filme]["nome"]

        if filmes[filme]["não avaliado"]:
            vencedores_especiais["não merecia estar aqui"].append(filmes[filme]["nome"])

    for categoria in vencedores:
        vencedor = vencedores[categoria][2]
        filmes[vencedor]["quantas venceu"] += 1

    for filme in filmes:
        pior = filmes[filme]["nome"]
        pontos_pior = filmes[filme]["pontos totais"]
        pior_venceu_quantas = filmes[filme]["quantas venceu"]
        break

    for filme in filmes:
        if filmes[filme]["quantas venceu"] > pior_venceu_quantas:
            pior = filmes[filme]["nome"]
            pontos_pior = filmes[filme]["pontos totais"]
            pior_venceu_quantas = filmes[filme]["quantas venceu"]
        elif filmes[filme]["quantas venceu"] == pior_venceu_quantas:
            if filmes[filme]["pontos totais"] > pontos_pior:
                pior = filmes[filme]["nome"]
                pontos_pior = filmes[filme]["pontos totais"]
                pior_venceu_quantas = filmes[filme]["quantas venceu"]

    vencedores_especiais["pior filme do ano"] = pior

    return [vencedores, vencedores_especiais]


def printar_saida(vencedores, vencedores_especiais):
    """ Printa os resultados para o usuário."""

    print("#### abacaxi de ouro ####")
    print()
    print("categorias simples")
    print("categoria: filme que causou mais bocejos")
    print(f"- {vencedores['filme que causou mais bocejos'][2]}")
    print("categoria: filme que foi mais pausado")
    print(f"- {vencedores['filme que foi mais pausado'][2]}")
    print("categoria: filme que mais revirou olhos")
    print(f"- {vencedores['filme que mais revirou olhos'][2]}")
    print("categoria: filme que não gerou discussão nas redes sociais")
    print(f"- {vencedores['filme que não gerou discussão nas redes sociais'][2]}")
    print("categoria: enredo mais sem noção")
    print(f"- {vencedores['enredo mais sem noção'][2]}")
    print()
    print("categorias especiais")
    print("prêmio pior filme do ano")
    print(f"- {vencedores_especiais['pior filme do ano']}")
    print("prêmio não merecia estar aqui")

    if len(vencedores_especiais["não merecia estar aqui"]) == 0:
        print("- sem ganhadores")
    else:
        print(f'- {", ".join(vencedores_especiais["não merecia estar aqui"])}')


def main():
    filmes, avaliacoes = user_entries()
    filmes = calcular_notas(filmes, avaliacoes)
    vencedores, vencedores_especiais = definir_vencedores(filmes)
    printar_saida(vencedores, vencedores_especiais)


if __name__ == "__main__":
    main()
