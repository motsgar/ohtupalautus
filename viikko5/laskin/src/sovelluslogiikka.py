class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.edelliset_arvot = []

    def miinus(self, operandi):
        self.edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.edelliset_arvot.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self.edelliset_arvot.append(self._arvo)
        self._arvo = arvo

    def kumoa(self):
        if len(self.edelliset_arvot) == 0:
            return
        self._arvo = self.edelliset_arvot.pop()

    def arvo(self):
        return self._arvo
