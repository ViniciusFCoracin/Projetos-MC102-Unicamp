print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")

user_entry = int(input("Seu SO anterior era Linux?\n(0) Não\n(1) Sim\n"))
caminhos_list = ["Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições:",
                 "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são:",
                 "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são:"
                ]
caminho = None
linux_dist = None

if user_entry == 0:
    user_entry = int(input("Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim\n"))
    if user_entry == 0:
        linux_dist = "Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro."
    elif user_entry == 1:
        linux_dist = "ElementaryOS, ApricityOS."
    caminho = 1

elif user_entry == 1:
    user_entry = int(input("É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e invasão de sistemas\n"))
    if user_entry == 0:
        linux_dist = "Ubuntu Mint, Fedora."
        caminho = 2
    if user_entry == 1:
        user_entry = int(input("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim\n"))
        if user_entry == 0:
            user_entry = int(input("Já utilizou Arch Linux?\n(0) Não\n(1) Sim\n"))
            if user_entry == 0:
                linux_dist = "Antergos, Arch Linux."
                caminho = 2
            elif user_entry == 1:
                linux_dist = "Gentoo, CentOS, Slackware."
                caminho = 0
        elif user_entry == 1:
            user_entry = int(input("Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim\n"))
            if user_entry == 0:
                linux_dist = "OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu."
                caminho = 2
            elif user_entry == 1:
                linux_dist = "Manjaro, ApricityOS."
                caminho = 0
    if user_entry == 2:
        linux_dist = "Kali Linux, Black Arch."
        caminho = 2

if linux_dist:
    print(caminhos_list[caminho], linux_dist)
else:
    print("Opção inválida, recomece o questionário.")