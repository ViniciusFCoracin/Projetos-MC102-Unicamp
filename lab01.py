jogada_sheila = input().lower()
jogada_reginaldo = input().lower()

# Primeiro testa se houve empate
if jogada_sheila == jogada_reginaldo:
    print("empate")

# Se não houve, testa todos os casos em que Sheila ganharia
elif jogada_sheila == "tesoura" and (jogada_reginaldo in ["papel", "lagarto"]):
    print("Interestelar")
elif jogada_sheila == "papel" and (jogada_reginaldo in ["pedra", "spock"]):
    print("Interestelar")
elif jogada_sheila == "pedra" and (jogada_reginaldo in ["tesoura", "lagarto"]):
    print("Interestelar")
elif jogada_sheila == "lagarto" and (jogada_reginaldo in ["papel", "spock"]):
    print("Interestelar")
elif jogada_sheila == "spock" and (jogada_reginaldo in ["tesoura", "pedra"]):
    print("Interestelar")

# Se nenhum dos casos correspondeu, é porque Reginaldo ganhou
else:
    print("Jornada nas Estrelas")