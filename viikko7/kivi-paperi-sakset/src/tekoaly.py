class Tekoaly:
    def __init__(self, siirto_ilmoitus):
        self._siirto = 0
        self._siirto_ilmoitus = siirto_ilmoitus

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        
        if self._siirto == 0:
            siirto = "k"
        elif self._siirto == 1:
            siirto = "p"
        else:
            siirto = "s"

        self._siirto_ilmoitus(siirto)
        return siirto

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
