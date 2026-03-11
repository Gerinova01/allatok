from allat import Allat
class Emlos(Allat):
    def __init__(self, nev, faj, eletkor, elohely, szorzet_szine):
        super().__init__(nev, faj, eletkor, elohely, "közepes")
        self.szorzet_szine = szorzet_szine

    def __str__(self):
        return f"{self.nev} {self.faj} {self.eletkor} éves élőhelye {self.elohely}, szőrzete {self.szorzet_szine} "

class Macska(Emlos):
    def __init__(self, nev, eletkor, elohely, szorzet_szine):
        super().__init__(nev, "macska", eletkor, elohely, szorzet_szine)

    def doromboral(self):
        print(f"{self.nev} épp doromborál")


class Kutya(Emlos):
    def __init__(self, nev, eletkor, elohely, szorzet_szine):
        super().__init__(nev, "kutya", eletkor, elohely, szorzet_szine)

    def ugatol(self):
        print(f"{self.nev} épp ugatol")