class Carta:
    def __init__(self, carta: str) -> None:
        self.carta = carta
        self.rank: str = carta[: len(self.carta) - 1]
        self.naipe: str = carta[len(self.carta) - 1:]

        def numero_carta(self) -> int:
            """Devolve um inteiro que representa a força da carta.
            Vão de 1 a 52 e, quanto maior é o inteiro, mais forte ela é."""

            NAIPES_DICT = {
                "O": 1,
                "E": 2,
                "C": 3,
                "P": 4,
            }

            RANK_DICT = {
                "A": 0,
                "J": 10,
                "Q": 11,
                "K": 12,
            }

            try:
                num_rank_carta: int = int(self.rank) - 1
            except ValueError:
                num_rank_carta: int = RANK_DICT[self.rank]

            num_naipe_carta: int = NAIPES_DICT[self.naipe]

            num_carta: int = num_rank_carta * 4 + num_naipe_carta
            return num_carta

        self.num = numero_carta(self)

    def __repr__(self) -> str:
        return self.carta

    def __str__(self) -> str:
        return self.carta

    def __gt__(self, carta):
        if isinstance(carta, self.__class__):
            if self.num > carta.num:
                return True
            else:
                return False

    def __lt__(self, carta):
        if isinstance(carta, self.__class__):
            if self.num < carta.num:
                return True
            else:
                return False


class Deck:
    def __init__(self, cartas: list[Carta]) -> None:
        self.cartas = cartas

    def ordena(self) -> list[Carta]:
        """Implementa o insertion sort para ordenar a lista de cartas"""

        lista = self.cartas
        for i in range(1, len(lista)):
            carta = lista[i]
            j = i - 1
            while j >= 0 and lista[j] < carta:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = carta
        return lista

    def busca_indice(self, carta: Carta) -> int:
        """Recebe uma instância de carta como parâmetro e retorna o índice que
        ela ocuparia na lista de cartas, de modo que a mantivesse ordenada.
        Baseia-se no algoritmo da busca binária.
        """

        lista = self.cartas
        e = 0
        d = len(lista) - 1
        while e <= d:
            m = (e + d) // 2
            if lista[m] > carta:
                e = m + 1
            else:
                d = m - 1
        return e

    def descartar(self, ult_carta: Carta) -> tuple:
        """Recebe a última carta da pilha como parâmetro e realiza o descarte."""

        i: int = self.busca_indice(ult_carta)
        self.cartas.insert(i, ult_carta)
        descarte: list[Carta] = []

        # Se o jogador tem uma carta de mesmo ranking da última carta jogada
        if (i - 1 <= 0 and self.cartas[i - 1].rank == ult_carta.rank or
            i + 1 < len(self.cartas) and self.cartas[i + 1].rank == ult_carta.rank):

            aux = i
            while (aux + 1 < len(self.cartas) and
                   self.cartas[aux + 1].rank == ult_carta.rank):
                descarte.insert(0, self.cartas[aux + 1])
                aux += 1

            aux = i
            while (aux - 1 >= 0 and
                   self.cartas[aux - 1].rank == ult_carta.rank):
                descarte.append(self.cartas[aux - 1])
                aux -= 1

            carta_jogada = ult_carta.rank
            blefe = False

        # Se ele não tem e precisa blefar
        elif i == 0:
            l = len(self.cartas) - 1
            rank = self.cartas[l].rank
            descarte.append(self.cartas[l])
            l -= 1
            while (l > 0 and
                   self.cartas[l].rank == rank):
                descarte.append(self.cartas[l])
                l -= 1
            carta_jogada = ult_carta.rank
            blefe = True

        # Se ele não tem carta de mesmo rank mas não precisa blefar
        else:
            descarte.append(self.cartas[i - 1])
            rank = self.cartas[i - 1].rank
            aux = i - 1
            while (aux - 1 >= 0 and
                   self.cartas[aux - 1].rank == rank):
                descarte.append(self.cartas[aux - 1])
                aux -= 1
            carta_jogada = descarte[0].rank
            blefe = False

        self.cartas.remove(ult_carta)
        for descartada in descarte:
            self.cartas.remove(descartada)

        num_jogadas = len(descarte)

        return descarte, carta_jogada, num_jogadas, blefe

    def descarte_inicial(self) -> tuple:
        """Função chamada para realizar o primeiro descarte da rodada.
        Descarta todas as cartas de menor valor no deck do jogador.
        """

        l: int = len(self.cartas) - 1
        rank: str = self.cartas[l].rank
        descarte: list[Carta] = [self.cartas[l]]

        l -= 1
        while l >= 0 and self.cartas[l].rank == rank:
            descarte.append(self.cartas[l])
            l -= 1

        carta_jogada: Carta = descarte[0].rank
        num_jogadas: int = len(descarte)

        for descartada in descarte:
            self.cartas.remove(descartada)

        return descarte, carta_jogada, num_jogadas

    def append(self, iterable) -> None:
        for elem in iterable:
            self.cartas.append(elem)

    def len(self) -> int:
        return len(self.cartas)

    def __str__(self) -> str:
        lista_str = [str(carta) for carta in self.cartas]
        return " ".join(lista_str)

    def __repr__(self) -> str:
        lista_str = [str(carta) for carta in self.cartas]
        return " ".join(lista_str)


def jogador_da_vez() -> int:
    """Retorna o jogador que deverá jogar neste turno."""

    global turno

    if turno > NUM_JOGADORES:
        turno = 1
    jogador: int = turno

    return jogador


def jogo_acabou(deck: Deck) -> bool:
    """Retorna booleano que informa se o jogo acabou ou não."""

    global acabou

    if deck.len() == 0:
        print(f"Jogador {turno} é o vencedor!")
        acabou = True

    return acabou


def rodada() -> None:
    """Executa uma rodada completa, desde o primeiro descarte até a jogada em
    que houve dúvida."""

    global turno, decks

    pilha: list[Carta] = []
    printar_todos_jog()

    jogador: int = jogador_da_vez()
    deck_jog: Deck = decks[jogador - 1]

    # Primeira jogada
    descarte, carta_jogada, num_jogadas = deck_jog.descarte_inicial()
    pilha += descarte
    printar_apos_jogada(carta_jogada, num_jogadas, pilha)
    turno += 1

    if jogo_acabou(deck_jog):
        return

    # Segunda jogada até a última antes de duvidar
    n = 2
    ultima_carta = None
    blefe = False
    while n < NUM_TURNOS_DUVIDO:
        jogador = jogador_da_vez()
        deck_jog = decks[jogador - 1]

        if not blefe:
            ultima_carta = pilha[len(pilha) - 1]

        descarte, carta_jogada, num_jogadas, blefe = deck_jog.descartar(ultima_carta)
        pilha += descarte
        printar_apos_jogada(carta_jogada, num_jogadas, pilha)

        if jogo_acabou(deck_jog):
            return

        turno += 1
        n += 1

    # Jogada em que houve dúvida
    jogador = jogador_da_vez()
    deck_jog = decks[jogador - 1]

    if not blefe:
        ultima_carta = pilha[len(pilha) - 1]

    descarte, carta_jogada, num_jogadas, blefe = deck_jog.descartar(ultima_carta)
    pilha += descarte
    printar_apos_jogada(carta_jogada, num_jogadas, pilha)

    turno += 1
    jog_que_duvidou = jogador_da_vez()
    print(f"Jogador {jog_que_duvidou} duvidou.")

    if blefe:
        deck_jog.append(pilha)
        deck_jog.ordena()
    else:
        deck_jog_duvidou = decks[jog_que_duvidou - 1]
        deck_jog_duvidou.append(pilha)
        deck_jog_duvidou.ordena()

        if deck_jog.len() == 0:
            global acabou
            acabou = True
            printar_todos_jog()
            print(f"Jogador {jogador} é o vencedor!")
            return


def printar_apos_jogada(carta_jogada: Carta, num_jogadas: int,
                        pilha: list[Carta]) -> None:
    """Printa a jogada que foi feita e a pilha de descarte."""

    print(f"[Jogador {turno}] {num_jogadas} carta(s) {carta_jogada}")
    pilha = [str(x) for x in pilha]
    print(f"Pilha: {' '.join(pilha)}")


def printar_todos_jog() -> None:
    """Printa a mão de todos os jogadores e a pilha de descarte."""

    for n in range(1, NUM_JOGADORES + 1):
        print(f"Jogador {n}")
        if decks[n - 1].len() != 0:
            print(f"Mão: {decks[n - 1]}")
        else:
            print("Mão:")

    print("Pilha:")


def main() -> None:
    while not acabou:
        rodada()


if __name__ == "__main__":
    NUM_JOGADORES: int = int(input())

    decks: list = []
    for _ in range(NUM_JOGADORES):
        entrada = input().split(", ")
        entrada = [Carta(x) for x in entrada]
        deck_n: Deck = Deck(entrada)
        deck_n.ordena()
        decks.append(deck_n)

    NUM_TURNOS_DUVIDO: int = int(input())
    turno: int = 1
    acabou: bool = False
    main()
