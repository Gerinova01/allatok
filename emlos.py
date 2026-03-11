from allat import Allat
class Emlos(Allat):
    def __init__(self, nev, faj, eletkor, elohely, szorzet_szine):
        super().__init__(nev, faj, eletkor, elohely, "közepes")
        self.szorzet_szine = szorzet_szine

    def __str__(self):
        return f"{self.nev} {self.faj} {self.eletkor} éves élőhelye {self.elohely}, szőrzete {self.szorzet_szine} "
