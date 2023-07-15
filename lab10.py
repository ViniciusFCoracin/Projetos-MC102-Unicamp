class Maquina:
    def __init__(self, num: int, hp: int, dano_atk: int, fraquezas: dict):
        self.num: int = num
        self.hp: int = hp
        self.dano_atk: int = dano_atk
        self.fraquezas: dict = fraquezas


class Aloy:
    def __init__(self, hp_max: int, flechas: dict):
        self.hp_max: int = hp_max
        self._hp: int = hp_max
        self.flechas_totais: dict = flechas
        self.flechas_combate: dict = flechas.copy()
        self.viva: bool = True

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        if new_hp <= 0:
            self._hp = 0
            self.viva = False
        else:
            self._hp = new_hp

    def tem_flechas(self) -> bool:
        """ Retorna booleano indicando se Aloy ainda possui flechas."""

        for quant in self.flechas_combate.values():
            if quant != 0:
                return True
        return False

    def calcular_dano(self, unid_alvo: Maquina, parte_alvo: str,
                      flecha_usada: str, coords_alvo: tuple) -> int:
        """Calcula o dano que Aloy causou na máquina alvo."""

        dano_max: int = unid_alvo.fraquezas[parte_alvo]["dano_max"]
        cx, cy = unid_alvo.fraquezas[parte_alvo]["coords"]
        fx, fy = coords_alvo
        fraqueza: bool = False

        # Se a parte é vulnerável contra a flecha utilizada
        if (unid_alvo.fraquezas[parte_alvo]["fraqueza"] == flecha_usada or
            unid_alvo.fraquezas[parte_alvo]["fraqueza"] == "todas"):
            fraqueza = True

        # Se o ponto acertado é um ponto crítico
        if cx == fx and cy == fy:
            unid_alvo.fraquezas[parte_alvo]["criticos"] += 1

        dano: int = dano_max - (abs(cx - fx) + abs(cy - fy))

        if not fraqueza:
            dano = dano // 2
        if dano >= 0:
            return dano
        else:   # Não existe dano negativo
            return 0

    def recuperar_hp(self) -> None:
        """Recupera a vida de Aloy."""

        hp_recuperado: int = self.hp + math.floor(self.hp_max * 0.5)
        if hp_recuperado > self.hp_max:
            self.hp = self.hp_max
        else:
            self.hp = hp_recuperado


def relatorio(aloy: Aloy, maquinas: list[Maquina]) -> None:
    """ Devolve relatório de quantas flechas foram utilizadas e quantos
    críticos acertados no combate."""

    print("Flechas utilizadas:")
    for key in aloy.flechas_totais:
        flechas_usadas: int = (aloy.flechas_totais[key] -
                              aloy.flechas_combate[key])
        if flechas_usadas != 0:
            print(f"- {key}: {flechas_usadas}/{aloy.flechas_totais[key]}")

    criticos = False
    for maq in maquinas:
        criticos_maq = False
        for parte in maq.fraquezas:
            if maq.fraquezas[parte]["criticos"] != 0:
                if not criticos:
                    # Se não houve críticos ainda
                    print("Críticos acertados:")
                    criticos = True
                if not criticos_maq:
                    # Se não houve críticos anteriores nesta máquina
                    print(f"Máquina {maq.num}:")
                    criticos_maq = True
                cx, cy = maq.fraquezas[parte]['coords']
                print(f"- ({cx}, {cy}): {maq.fraquezas[parte]['criticos']}x")


def main() -> None:
    hp_max: int = int(input())

    flechas_entrada: list[str] = input().split()
    flechas: dict = {}
    #  Armazena as flechas e as respectivas quantidades num dict
    for i in range(0, len(flechas_entrada) - 1, 2):
        flechas[flechas_entrada[i]] = int(flechas_entrada[i + 1])

    aloy: Aloy = Aloy(hp_max, flechas)

    num_maquinas: int = int(input())
    num_derrotadas: int = 0
    combate: int = 0

    while num_derrotadas < num_maquinas:
        maquinas: list[Maquina] = []
        num_maq_round: int = int(input())
        for i in range(num_maq_round):
            info = input().split()
            info = [int(x) for x in info]
            hp_maq, dano_atk, num_partes = info

            fraquezas: dict = {}
            for _ in range(num_partes):
                info = input().split(", ")
                parte, fraqueza, dano_max, cx, cy = info
                vulnerabilidade = {"fraqueza": fraqueza,
                                   "dano_max": int(dano_max),
                                   "coords": (int(cx), int(cy)),
                                   "criticos": 0,
                                  }
                fraquezas[parte] = vulnerabilidade

            monstro: Maquina = Maquina(i, hp_maq, dano_atk, fraquezas)
            maquinas.append(monstro)

        # Aqui inicia-se o  combate
        maq_vivas = maquinas.copy()
        num_maq_vivas: int = len(maquinas)
        print(f"Combate {combate}, vida = {aloy.hp}")

        while (aloy.viva and
               aloy.tem_flechas() and
               num_maq_vivas > 0):
            flechas_atiradas: int = 0
            while (flechas_atiradas < 3 and
                   aloy.tem_flechas() and
                   num_maq_vivas > 0):
                info = input().split(", ")
                num_unid_alvo, parte_alvo, flecha_usada, fx, fy = info
                coords_alvo: tuple(int) = (int(fx), int(fy))
                num_unid_alvo: int = int(num_unid_alvo)
                unid_alvo: Maquina = maquinas[num_unid_alvo]

                dano: int = aloy.calcular_dano(unid_alvo, parte_alvo, flecha_usada, coords_alvo)
                unid_alvo.hp -= dano
                if unid_alvo.hp <= 0:   # Se a máquina morreu
                    num_maq_vivas -= 1
                    num_derrotadas += 1
                    maq_vivas[num_unid_alvo] = "dead"
                    print(f"Máquina {num_unid_alvo} derrotada")

                aloy.flechas_combate[flecha_usada] -= 1
                flechas_atiradas += 1

            for maq in maq_vivas:
                # Após disparar três flechas, recebe dano de todas as máquinas vivas
                if maq != "dead":
                    aloy.hp -= maq.dano_atk

        print(f"Vida após o combate = {aloy.hp}")
        if not aloy.viva:
            print("Aloy foi derrotada em combate e não retornará a tribo.")
            return
        elif num_maq_vivas == 0:
            relatorio(aloy, maquinas)
            aloy.recuperar_hp()
            aloy.flechas_combate = aloy.flechas_totais.copy()
            combate += 1
        elif not aloy.tem_flechas():
            print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
            return

    print("Aloy provou seu valor e voltou para sua tribo.")


if __name__ == "__main__":
    import math
    main()
