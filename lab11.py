class Monstro:
    def __init__(self, vida: int, dano: int, tipo: str,
                 posy: int, posx: int) -> None:
        self._vida = vida
        self.dano = dano
        self.tipo = tipo
        self.posx = posx
        self.posy = posy
        self.vivo: bool = True
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nova_vida):
        if nova_vida <= 0:
            self._vida = 0
            self.vivo = False
        else:
            self._vida = nova_vida

    def __str__(self) -> str:
        return self.tipo

    def __repr__(self) -> str:
        return self.tipo 

    def mover(self, masmorra: list[list]) -> None:
        num_linhas: int = len(masmorra)
        num_colunas: int = len(masmorra[0])

        match self.tipo:
            case "U":
                if self.posy > 0:
                    self.posy -= 1
            case "D":
                if self.posy < num_linhas - 1:
                    self.posy += 1
            case "L":
                if self.posx > 0:
                    self.posx -= 1
            case "R":
                if self.posx < num_colunas - 1:
                    self.posx += 1

    def atacar(self, link) -> int:
        """ Ataca Link e retorna quanto de dano causou."""

        if self.dano >= link.vida:
            dano = link.vida
        else:
            dano = self.dano
        if self.vivo:
            link.vida -= dano

        return dano


class Link:
    def __init__(self, vida: int, dano: int, posy: int, posx: int) -> None:
        self._vida = vida
        self._dano = dano
        self.posx = posx
        self.posy = posy
        self.vivo: bool = True
        self.passos: int = 0
        self.caminho: list[tuple] = [].copy()

    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nova_vida):
        if nova_vida <= 0:
            self._vida = 0
            self.vivo = False
        else:
            self._vida = nova_vida

    @property
    def dano(self):
        return self._dano
    
    @dano.setter
    def dano(self, novo_dano):
        if novo_dano <= 1:
            self._dano = 1
        else:
            self._dano = novo_dano

    def __str__(self) -> str:
        if self.vivo:
            return "P"
        else:
            return "X"
        
    def __repr__(self) -> str:
        if self.vivo:
            return "P"
        else:
            return "X"

    def def_caminho(self, masmorra: list[list]) -> None:
        """Armazena as tuplas de pares (self.posy, self.posx) a serem
        percorridas por Link numa lista.
        Pode ser que Link não precise ir a todas essas posições pois,
        possivelmente, encontrará a saída ou morrerá antes."""

        num_linhas = len(masmorra)
        num_colunas = len(masmorra[0])
        # Salva a posição inicial
        self.caminho.append((self.posy, self.posx))

        # Vai até a última linha
        while self.posy < num_linhas - 1:
            self.posy += 1
            self.caminho.append((self.posy, self.posx))

        while True:
            # Se a linha for par, movemos para a esquerda
            if self.posy % 2 == 0:
                while self.posx > 0:
                    self.posx -= 1
                    self.caminho.append((self.posy, self.posx))
            # Se a linha for ímpar, movemos para a direita
            else:
                while self.posx < num_colunas - 1:
                    self.posx += 1
                    self.caminho.append((self.posy, self.posx))
            # Ao chegar no canto, subimos uma linha (a menos que
            # já estejamos na linha 0.)
            if self.posy != 0:
                self.posy -= 1
                self.caminho.append((self.posy, self.posx))
            else:
                return

    def mover(self) -> None:
        """ Altera as posições x e y de link baseado em quantos
        passos ele já deu."""

        self.passos += 1
        self.posy = self.caminho[self.passos][0]
        self.posx = self.caminho[self.passos][1]

    def atacar(self, monstro) -> int:
        """Ataca o monstro e retorna quanto de dano causou."""

        if monstro.vida <= self.dano:
            dano = monstro.vida
        else:
            dano = self.dano
        monstro.vida -= dano

        return dano

    def pegar_obj(self, obj) -> None:
        if obj.tipo == "d":
            self.dano += obj.status
        elif obj.tipo == "v":
            self.vida += obj.status


class Objeto:
    def __init__(self, nome: str, tipo: str, posy: int,
                 posx: int, status: int) -> None:
        self.nome = nome
        self.tipo = tipo
        self.posx = posx
        self.posy = posy
        self.status = status

    def __str__(self) -> str:
        return self.tipo
    
    def __repr__(self) -> str:
        return self.tipo 


def entradas():
    """ Recebe as entradas do usuário"""

    hp_link, dano_link =  input().split()
    hp_link = int(hp_link)
    dano_link = int(dano_link)

    num_linhas, num_colunas = input().split()
    num_linhas = int(num_linhas)
    num_colunas = int(num_colunas)

    posy_link, posx_link = input().split(",")
    posy_link = int(posy_link)
    posx_link = int(posx_link)

    posy_saida, posx_saida = input().split(",")
    posy_saida = int(posy_saida)
    posx_saida = int(posx_saida)

    link = Link(hp_link, dano_link, posy_link, posx_link)

    # Informações dos monstros
    num_monstros = int(input())
    monstros: list[Monstro] = []
    for _ in range(num_monstros):
        vida, dano, tipo, pos = input().split()
        vida = int(vida)
        dano = int(dano)
        posy, posx = pos.split(",")
        posy = int(posy)
        posx = int(posx)

        monstro = Monstro(vida, dano, tipo, posy, posx)
        monstros.append(monstro)

    # Informações dos objetos
    num_obj = int(input())
    objetos: list[Objeto] = []
    for _ in range(num_obj):
        nome, tipo, pos, status = input().split()
        posy, posx = pos.split(",")
        posy = int(posy)
        posx = int(posx)
        status = int(status)

        objeto = Objeto(nome, tipo, posy, posx, status)
        objetos.append(objeto)

    # Cria a masmorra
    masmorra = criar_masmorra(num_linhas, num_colunas, posx_saida,
                              posy_saida, link, monstros, objetos)
    link.def_caminho(masmorra)

    return (masmorra, monstros, objetos, link, posx_saida, posy_saida)


def criar_masmorra(num_linhas: int, num_colunas: int, posx_saida: int,
                   posy_saida: int, link: Link, monstros: list[Monstro],
                   objetos: list[Objeto]) -> list[list]:
    """ Cria a matriz bidimensional que representa a masmorra"""

    masmorra: list[list] = []
    for linha in range(num_linhas):
        linha = []
        for _ in range(num_colunas):
            linha.append(".")
        masmorra.append(linha)

    masmorra[link.posy][link.posx] = link

    if masmorra[posy_saida][posx_saida] == ".":
        masmorra[posy_saida][posx_saida] = "*"
    else:
        masmorra[posy_saida][posx_saida] = [masmorra[posy_saida][posx_saida], "*"]

    for mons in monstros:
        if masmorra[mons.posy][mons.posx] == ".":
            masmorra[mons.posy][mons.posx] = mons
        elif isinstance(masmorra[mons.posy][mons.posx], list):
            masmorra[mons.posy][mons.posx].append(mons)
        else:
            masmorra[mons.posy][mons.posx] = [masmorra[mons.posy][mons.posx], mons]

    for obj in objetos:
        if masmorra[obj.posy][obj.posx] == ".":
            masmorra[obj.posy][obj.posx] = obj
        elif isinstance(masmorra[obj.posy][obj.posx], list):
            masmorra[obj.posy][obj.posx].append(obj)
        else:
            masmorra[obj.posy][obj.posx] = [masmorra[obj.posy][obj.posx], obj]

    return masmorra


def printar_saida(masmorra: list[list]) -> None:
    """Printa a situação atual da masmorra para o usuário."""

    for linha in masmorra:
        l = []
        for elem in linha:
            if not isinstance(elem, list):
                l.append(str(elem))
            else:
                printado = False
                for i in elem:
                    if isinstance(i, Link):
                        l.append(str(i))
                        printado = True
                        break
                if not printado:
                    if "*" in elem:
                        l.append("*")
                        printado = True
                if not printado:
                    ult_monstro = None
                    for i in elem:
                        if isinstance(i, Monstro):
                            ult_monstro = i
                    if ult_monstro is not None:
                        l.append(str(ult_monstro))
                        printado = True
                if not printado:
                    ultimo_obj = None
                    for i in elem:
                        if isinstance(i, Objeto):
                            ultimo_obj = i
                    l.append(str(ultimo_obj))
        print(" ".join(l))
    print()


def main():
    masmorra, monstros, objetos, link, px_saida, py_saida = entradas()
    printar_saida(masmorra)
    
    while link.vivo:
        link.mover()
        for mons in monstros:
            mons.mover(masmorra)
        masmorra = criar_masmorra(len(masmorra), len(masmorra[0]), px_saida,
                                  py_saida, link, monstros, objetos)
        
        # Verifica se há apenas um objeto na posição de Link e pega-o se for o caso.
        if isinstance(masmorra[link.posy][link.posx], Objeto):
            obj = masmorra[link.posy][link.posx]
            link.pegar_obj(obj)
            objetos.remove(i)
            print(f"[{obj.tipo}]Personagem adquiriu o objeto {obj.nome} com status de {obj.status}")
                
        # Verifica se há apenas um monstro na posição de Link e inicia a batalha em caso positivo
        elif isinstance(masmorra[link.posy][link.posx], Monstro):
            monstro = masmorra[link.posy][link.posx]
            dano = link.atacar(monstro)
            print(f"O Personagem deu {dano} de dano ao monstro na posicao ({link.posy}, {link.posx})")
            if monstro.vivo:
                dano = monstro.atacar(link)
                print(f"O Monstro deu {dano} de dano ao Personagem. Vida restante = {link.vida}")
            else:
                monstros.remove(monstro)
                
        # Se há vários elementos na posição atual de Link
        elif isinstance(masmorra[link.posy][link.posx], list):
            # Se chegou na saída
            if "*" in masmorra[link.posy][link.posx]:
                printar_saida(masmorra)
                print("Chegou ao fim!")
                return
            else:
                # Procura por objetos na posição atual e pega-os.
                for i in masmorra[link.posy][link.posx]:
                    if isinstance(i, Objeto):
                        link.pegar_obj(i)
                        objetos.remove(i)
                        print(f"[{i.tipo}]Personagem adquiriu o objeto {i.nome} com status de {i.status}")
                # Procura por monstros na posição atual e inicia as batalhas
                for i in masmorra[link.posy][link.posx]:
                    if isinstance(i, Monstro):
                        dano = link.atacar(i)
                        print(f"O Personagem deu {dano} de dano ao monstro na posicao ({link.posy}, {link.posx})")
                        if i.vivo:
                            dano = i.atacar(link)
                            print(f"O Monstro deu {dano} de dano ao Personagem. Vida restante = {link.vida}")
                        elif not i.vivo:
                            monstros.remove(i)
                        if not link.vivo:
                            printar_saida(masmorra)
                            return
        
        printar_saida(masmorra)


if __name__ == "__main__":
    main()
