from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self, pelaaja1, pelaaja2):
        self._pelaaja1 = pelaaja1
        self._pelaaja2 = pelaaja2

    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = self._pelaaja1.anna_siirto()
            tokan_siirto = self._pelaaja2.anna_siirto()

            if not self._onko_ok_siirto(ekan_siirto) or not self._onko_ok_siirto(tokan_siirto):
                break
            
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            self._pelaaja1.aseta_siirto(tokan_siirto)
            self._pelaaja2.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"