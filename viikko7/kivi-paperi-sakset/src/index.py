from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class Ihminen:
    def __init__(self, nimi):
        self.nimi = nimi

    def anna_siirto(self):
        return input(f"{self.nimi} siirto: ")
    
    def aseta_siirto(self, siirto):
        pass
    
def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            pelaaja1 = Ihminen("Ensimmäinen pelaaja")
            pelaaja2 = Ihminen("Toinen pelaaja")
            peli = KiviPaperiSakset(pelaaja1, pelaaja2)
        elif vastaus.endswith("b"):
            pelaaja = Ihminen("Ihminen")
            tekoaly = Tekoaly(lambda siirto: print(f"Tekoäly valitsi: {siirto}"))
            peli = KiviPaperiSakset(pelaaja, tekoaly)
        elif vastaus.endswith("c"):
            pelaaja = Ihminen("Ihminen")
            tekoaly = TekoalyParannettu(10, lambda siirto: print(f"Parempi tekoäly valitsi: {siirto}"))
            peli = KiviPaperiSakset(pelaaja, tekoaly)
        else:
            break
    
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        peli.pelaa()


if __name__ == "__main__":
    main()
