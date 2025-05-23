from jegyfoglalas import JegyFoglalas
from datetime import datetime


class FoglalasiRendszer:
    def __init__(self, legitarsasag):
        self.legitarsasag = legitarsasag
        self.foglalasok = []

    def jegy_foglalasa(self, utas_nev, jaratszam):
        jarat = self.legitarsasag.jarat_keresese(jaratszam)
        if jarat:
            # Ellenőrizzük, hogy a járat még nem indult el
            if jarat.indulas_idopont < datetime.now():
                print("A járat már elindult, nem lehet foglalni.")
                return None

            foglalas = JegyFoglalas(utas_nev, jarat)
            self.foglalasok.append(foglalas)
            print(f"Foglalás sikeres: {foglalas}")
            return jarat.jegyar
        else:
            print("Nincs ilyen járatszám!")
            return None

    def foglalas_lemondasa(self, utas_nev, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                print("Foglalás sikeresen lemondva.")
                return True
        print("Nem található ilyen foglalás.")
        return False

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek aktív foglalások.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas)

    def foglalasok_jaratonkent(self):
        statisztika = {}
        for foglalas in self.foglalasok:
            jaratszam = foglalas.jarat.jaratszam
            if jaratszam in statisztika:
                statisztika[jaratszam] += 1
            else:
                statisztika[jaratszam] = 1

        if not statisztika:
            print("Nincs egyetlen foglalás sem.")
        else:
            print("\nFoglalások járatonként:")
            for jaratszam, db in statisztika.items():
                print(f"{jaratszam} - {db} foglalás")

    def foglalasok_mentese_csv(self, fajlnev="foglalasok.csv"):
        import csv
        with open(fajlnev, mode="w", newline='', encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["utas_nev", "jaratszam", "celallomas", "jegyar"])
            for foglalas in self.foglalasok:
                writer.writerow([
                    foglalas.utas_nev,
                    foglalas.jarat.jaratszam,
                    foglalas.jarat.celallomas,
                    foglalas.jarat.jegyar
                ])
        print(f"Foglalások sikeresen elmentve: {fajlnev}")

    def ossz_bevetel(self):
        osszeg = sum(foglalas.jarat.jegyar for foglalas in self.foglalasok)
        print(f"\nÖsszes bevétel: {osszeg} Ft")
        return osszeg
