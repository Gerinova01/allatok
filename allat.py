class Allat:
    def __init__(self,nev, faj, eletkor, elohely, meret):
        self.nev = nev
        self.faj = faj
        self.eletkor = eletkor
        self.elohely = elohely
        self.meret = meret

    def __str__(self):
        return f"{self.nev} {self.faj} {self.eletkor} éves élőhelye {self.elohely}"


class Madar(Allat):
    def __init__(self, nev):
        super().__init__(nev, "madar", 1, "erdő", "kicsi")

    def csiripel(self):
        print(f"{self.nev} csiripel")

class Keteltu(Allat):
    def __init__(self, nev):
        super().__init__(nev, "béka", 2, "tópart", "kicsi")

    def brekeg(self):
        print(f"{self.nev} brekeg")

class Hullo(Allat):
    def __init__(self, nev,):
        super().__init__(nev, "hullo", 3, "szikla", "óriás")

    def napozik(self):
        print(f"{self.nev} napozik")