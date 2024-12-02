KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm >= len(self.ljono):
                self._kasvata_taulukkoa()
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            self.ljono.remove(n)
            self.ljono.append(0)
            self.alkioiden_lkm -= 1
            return True
        return False

    def _kasvata_taulukkoa(self):
        uusi_ljono = [0] * (len(self.ljono) + self.kasvatuskoko)
        for i in range(self.alkioiden_lkm):
            uusi_ljono[i] = self.ljono[i]
        self.ljono = uusi_ljono

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            tulos.lisaa(numero)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero not in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
