class PGM_Image:
    def __init__(self, path: str) -> None:
        self.path = path
        with open(path, "r") as image:
            linhas = image.readlines()
            self.version: str = linhas[0]
            self.header: str = linhas[1]
            self.num_columns, self.num_rows = [int(x) for x in linhas[2].split()]
            self.max_pixel: int = int(linhas[3])
            self.image: list[list[int]] = []

            for n in range(4, len(linhas)):
                linha = linhas[n].split()
                linha = [int(x) for x in linha if x.isnumeric()]
                self.image.append(linha)

    def regiao_conexa(self, tolerancia: int, column: int,
                      row: int, cor_balde: int = None) -> list[tuple]:
        """Retorna uma lista contendo as coordenadas dos pixels da região conexa.

        Parâmetros:
            tolerancia (int): Máxima diferença na intensidade do pixel para incluir
            na região conexa.
            column, row (int): Coordenadas do pixel semente.
            cor_balde = None (int): Só possuíra valor diferente de None quando esta função
            for chamada pela função bucket.

        Retorna:
            list[tuple] contendo inteiros que representam as coordenadas dos pixeis conexos.
        """

        cor_seed: int = self.image[row][column]
        pixels_conexos: list[tuple] = [(row, column)]
        verificado: dict = {}
        for r in range(len(self.image)):
            for c in range(len(self.image[0])):
                verificado[(r, c)] = False
        verificado[row, column] = True
        
        def regiao_conexa_rec(column_rec: int ,row_rec: int) -> None:
            """Recursivamente descobre os pixels pertencentes à região conexa.
            Adiciona as coordenadas de tais pixels a pixels_conexos, variável
            declarada na função regiao_conexa."""

            # Para cima
            if row_rec - 1 >= 0 and not verificado[row_rec - 1, column_rec]:
                verificado[row_rec - 1, column_rec] = True
                if abs(cor_seed - self.image[row_rec - 1][column_rec]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec - 1][column_rec]):
                        pixels_conexos.append((row_rec - 1, column_rec))
                        regiao_conexa_rec(column_rec, row_rec - 1)

            # Para baixo
            if row_rec + 1 < self.num_rows and not verificado[row_rec + 1, column_rec]:
                verificado[row_rec + 1, column_rec] = True
                if abs(cor_seed - self.image[row_rec + 1][column_rec]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec + 1][column_rec]):
                        pixels_conexos.append((row_rec + 1, column_rec))
                        regiao_conexa_rec(column_rec, row_rec + 1)

            # Para a esquerda
            if column_rec - 1 >= 0 and not verificado[row_rec, column_rec - 1]:
                verificado[row_rec, column_rec - 1] = True
                if abs(cor_seed - self.image[row_rec][column_rec - 1]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec][column_rec - 1]):
                        pixels_conexos.append((row_rec, column_rec - 1))
                        regiao_conexa_rec(column_rec - 1, row_rec)

            # Para a direita
            if (column_rec + 1 < self.num_columns and
                not verificado[row_rec, column_rec + 1]):
                verificado[row_rec, column_rec + 1] = True
                if abs(cor_seed - self.image[row_rec][column_rec + 1]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec][column_rec + 1]):
                        pixels_conexos.append((row_rec, column_rec + 1))
                        regiao_conexa_rec(column_rec + 1, row_rec)

            # Para diagonal superior esquerda
            if (row_rec - 1 >= 0 and column_rec - 1 >= 0
                and not verificado[row_rec - 1, column_rec - 1]):
                verificado[row_rec - 1, column_rec - 1] = True
                if abs(cor_seed - self.image[row_rec - 1][column_rec - 1]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec - 1][column_rec - 1]):
                        pixels_conexos.append((row_rec - 1, column_rec - 1))
                        regiao_conexa_rec(column_rec - 1, row_rec - 1)

            # Para diagonal superior direita
            if (row_rec - 1 >= 0 and column_rec + 1 < self.num_columns
                and not verificado[row_rec - 1, column_rec + 1]):
                verificado[row_rec - 1, column_rec + 1] = True
                if abs(cor_seed - self.image[row_rec - 1][column_rec + 1]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec - 1][column_rec + 1]):
                        pixels_conexos.append((row_rec - 1, column_rec + 1))
                        regiao_conexa_rec(column_rec + 1, row_rec - 1)

            # Para diagonal inferior esquerda
            if (row_rec + 1 < self.num_rows and column_rec - 1 >= 0
                and not verificado[row_rec + 1, column_rec - 1]):
                verificado[row_rec + 1, column_rec - 1] = True
                if abs(cor_seed - self.image[row_rec + 1][column_rec - 1]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec + 1][column_rec - 1]):
                        pixels_conexos.append((row_rec + 1, column_rec - 1))
                        regiao_conexa_rec(column_rec - 1, row_rec + 1)

            # Para diagonal inferior direita
            if (row_rec + 1 < self.num_rows and column_rec + 1 < self.num_columns
                and not verificado[row_rec + 1, column_rec + 1]):
                verificado[row_rec + 1, column_rec + 1] = True
                if abs(cor_seed - self.image[row_rec + 1][column_rec + 1]) <= tolerancia:
                    if (cor_balde is None or
                        cor_balde is not None and cor_balde != self.image[row_rec + 1][column_rec + 1]):
                        pixels_conexos.append((row_rec + 1, column_rec + 1))
                        regiao_conexa_rec(column_rec + 1, row_rec + 1)

        regiao_conexa_rec(column, row)
        return pixels_conexos
    
    def bucket(self, cor: int, tolerancia: int, column: int, row: int) -> None:
        """Altera a cor de todos os pixels pertencentes à região conexa."""

        pixels_conexos = self.regiao_conexa(tolerancia, column, row, cor)
        for r, c in pixels_conexos:
            self.image[r][c] = cor

    def negative(self, tolerancia: int, column: int, row: int) -> None:
        """Inverte a cor de todos os pixels pertences à região conexa."""

        pixels_conexos = self.regiao_conexa(tolerancia, column, row)
        for r, c in pixels_conexos:
            self.image[r][c] = self.max_pixel - self.image[r][c]
    
    def cmask(self, tolerancia: int, column: int, row: int) -> None:
        """Coloca a intensidade de todos os pixels pertencentes à região conexa
        como 0 e o restante como 255."""

        pixels_conexos = self.regiao_conexa(tolerancia, column, row)
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                self.image[i][j] = 255
        for r, c in pixels_conexos:
            self.image[r][c] = 0

    def save(self) -> None:
        """Printa o arquivo."""
        
        print(self.version, end = "")
        print("# Imagem criada pelo lab13")
        print(f"{self.num_columns} {self.num_rows}")
        print(self.max_pixel)
        for linha in self.image:
            linha = [str(x) for x in linha]
            print(" ".join(linha))


def main() -> None:
    path: str = input()
    image = PGM_Image(path)

    num_oper: int = int(input())
    for _ in range(num_oper):
        entrada = input().split()
        if entrada[0] == "bucket":
            image.bucket(int(entrada[1]), int(entrada[2]),
                         int(entrada[3]), int(entrada[4]))
        elif entrada[0] == "negative":
            image.negative(int(entrada[1]), int(entrada[2]), int(entrada[3]))
        elif entrada[0] == "cmask":
            image.cmask(int(entrada[1]), int(entrada[2]), int(entrada[3]))
        elif entrada[0] == "save":
            image.save()


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(16385)
    main()
