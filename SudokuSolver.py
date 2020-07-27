class Table:
    def __init__(self):
        self.dizi = list()
        for i in range(9):
            self.dizi.append([])
            for j in range(9):
                self.dizi[i].append(Eleman(i, j, 0))

        self.numberOfUnsolved = 0

        for i in self.dizi:
            for e in i:
                if e.value == 0:
                    self.numberOfUnsolved += 1

    def updateUnsolved(self):
        self.numberOfUnsolved = 0
        for i in self.dizi:
            for e in i:
                if e.value == 0:
                    self.numberOfUnsolved += 1

    def setEleman(self, row, column, neu):
        self.dizi[row][column].value = neu

    def getunsolved(self):
        unsolved = list()
        for row in self.dizi:
            for e in row:
                if e.value == 0:
                    e.buildpossibles(self)
                    unsolved.append(e)
        unsolved.sort(key=lambda x: len(x.possibles))
        return unsolved

    def __str__(self):
        cikti = "\n\n    | | | | | | | | |  -  (j)\n  - "
        for i in range(9):
            c = 0
            for e in self.dizi[i]:
                if c % 3 == 2 and c != 8:
                    cikti += str(e.value if e.value != 0 else " ") + "|"
                else:
                    cikti += str(e.value if e.value != 0 else " ") + " "
                c += 1
            if i % 3 == 2 and i != 8:
                cikti += "\n    -----------------\n  - "
            elif i != 8:
                cikti += "\n  - "
            else:
                cikti += "\n\n  |\n\n (i)"
        return cikti


class Eleman:
    def __init__(self, i, j, value):
        self.digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.row = i
        self.column = j
        self.smallsq = (self.column // 3) + (self.row // 3) * 3
        self.value = value
        self.possibles = list()

    def __str__(self):
        return str(self.possibles)

    def __repr__(self):
        return str(self.value if self.value != 0 else " ")

    def buildpossibles(self, tablo):
        rowothers = list()
        columnothers = list()
        smallsqothers = list()
        for e in tablo.dizi[self.row]:
            rowothers.append(e.value)
        for i in range(9):
            columnothers.append(tablo.dizi[i][self.column].value)
        for row in tablo.dizi:
            for e in row:
                if e.smallsq == self.smallsq:
                    smallsqothers.append(e.value)
        used = [*rowothers, *columnothers, *smallsqothers]
        self.possibles = []

        for number in self.digits:
            if number not in used:
                self.possibles.append(number)


def solve(tablo):
    tablo.updateUnsolved()

    lst = tablo.getunsolved()

    if len(lst) == 0:
        return tablo
    elif len(lst[0].possibles) == 0:
        return None
    else:
        for possible in lst[0].possibles:
            x = lst[0].row
            y = lst[0].column
            tablo.dizi[x][y].value = possible

            if solve(tablo) is None:
                tablo.dizi[x][y].value = 0

            else:

                return tablo
        return None


ornek = Table()

ornek.setEleman(0, 0, 8)
ornek.setEleman(1, 2, 3)
ornek.setEleman(2, 1, 7)
ornek.setEleman(1, 3, 6)
ornek.setEleman(2, 4, 9)
ornek.setEleman(2, 6, 2)
ornek.setEleman(3, 1, 5)
ornek.setEleman(3, 5, 7)
ornek.setEleman(4, 4, 4)
ornek.setEleman(4, 5, 5)
ornek.setEleman(4, 6, 7)
ornek.setEleman(5, 3, 1)
ornek.setEleman(5, 7, 3)
ornek.setEleman(6, 2, 1)
ornek.setEleman(6, 8, 8)
ornek.setEleman(6, 7, 6)
ornek.setEleman(7, 2, 8)
ornek.setEleman(7, 3, 5)
ornek.setEleman(7, 7, 1)
ornek.setEleman(8, 1, 9)
ornek.setEleman(8, 6, 4)
ornek.updateUnsolved()
print(ornek)

solve(ornek)

print(ornek)
