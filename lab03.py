jogadores = int(input())
entrada_numeros = input().split()
entrada_intervalos = input().split()

numeros = list(map(lambda x : int(x), entrada_numeros))
intervalos = list(map(lambda x : int(x), entrada_intervalos))

if jogadores % 2 == 0:
    primeira_metade = jogadores / 2
else:
    primeira_metade = (jogadores + 1) / 2

i = 0
ganhador = None
maior_pontuacao = 0
empate = False
while i < jogadores:
    if i < primeira_metade:
        pontos = (intervalos[2*i+1] - intervalos[2*i]) * numeros[i]
    else:
        pontos = (intervalos[2*i+1] - intervalos[2*i]) + numeros[i]

    if pontos > maior_pontuacao:
        maior_pontuacao = pontos
        ganhador = i + 1
        empate = False
    elif pontos == maior_pontuacao:
        empate = True
    
    i += 1

if empate == True:
    print("Rodada de cerveja para todos os jogadores!")
else:
    print(f"O jogador número {ganhador} vai receber o melhor bolo da cidade pois venceu com {maior_pontuacao} ponto(s)!")