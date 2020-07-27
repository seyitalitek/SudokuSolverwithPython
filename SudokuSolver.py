class Table:
    def __init__(self):
        self.grid = list()
        for i in range(9):
            self.grid.append([])
            for j in range(9):
                self.grid[i].append(Element(i, j, 0))

        self.numberOfUnsolved = 0

        for i in self.grid:
            for e in i:
                if e.value == 0:
                    self.numberOfUnsolved += 1

    def updateUnsolved(self):
        self.numberOfUnsolved = 0
        for i in self.grid:
            for e in i:
                if e.value == 0:
                    self.numberOfUnsolved += 1

    def setElement(self, row, column, neu):
        self.grid[row][column].value = neu

    def getUnsolved(self):
        unsolved = list()
        for row in self.grid:
            for e in row:
                if e.value == 0:
                    e.buildPossibles(self)
                    unsolved.append(e)
        unsolved.sort(key=lambda x: len(x.possibles))
        return unsolved

    def __str__(self):
        output = "\n\n    | | | | | | | | |  -  (j)\n  - "
        for i in range(9):
            c = 0
            for e in self.grid[i]:
                if c % 3 == 2 and c != 8:
                    output += str(e.value if e.value != 0 else " ") + "|"
                else:
                    output += str(e.value if e.value != 0 else " ") + " "
                c += 1
            if i % 3 == 2 and i != 8:
                output += "\n    -----------------\n  - "
            elif i != 8:
                output += "\n  - "
            else:
                output += "\n\n  |\n\n (i)"
        return output


class Element:
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

    def buildPossibles(self, tablo):
        rowothers = list()
        columnothers = list()
        smallsqothers = list()
        for e in tablo.grid[self.row]:
            rowothers.append(e.value)
        for i in range(9):
            columnothers.append(tablo.grid[i][self.column].value)
        for row in tablo.grid:
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

    lst = tablo.getUnsolved()

    if len(lst) == 0:
        return tablo
    elif len(lst[0].possibles) == 0:
        return None
    else:
        for possible in lst[0].possibles:
            x = lst[0].row
            y = lst[0].column
            tablo.grid[x][y].value = possible

            if solve(tablo) is None:
                tablo.grid[x][y].value = 0

            else:

                return tablo
        return None


ornek = Table()

ornek.setElement(0, 0, 8)
ornek.setElement(1, 2, 3)
ornek.setElement(2, 1, 7)
ornek.setElement(1, 3, 6)
ornek.setElement(2, 4, 9)
ornek.setElement(2, 6, 2)
ornek.setElement(3, 1, 5)
ornek.setElement(3, 5, 7)
ornek.setElement(4, 4, 4)
ornek.setElement(4, 5, 5)
ornek.setElement(4, 6, 7)
ornek.setElement(5, 3, 1)
ornek.setElement(5, 7, 3)
ornek.setElement(6, 2, 1)
ornek.setElement(6, 8, 8)
ornek.setElement(6, 7, 6)
ornek.setElement(7, 2, 8)
ornek.setElement(7, 3, 5)
ornek.setElement(7, 7, 1)
ornek.setElement(8, 1, 9)
ornek.setElement(8, 6, 4)
ornek.updateUnsolved()
print(ornek)

solve(ornek)

print(ornek)
