from jarat import BelfoldiJarat, NemzetkoziJarat
from legitarsasag import LegiTarsasag
from foglalasirendszer import FoglalasiRendszer

def main():
    # Létrehozunk egy légitársaságot
    legitarsasag = LegiTarsasag("SkyFly")

    # Hozzáadunk 3 járatot
    legitarsasag.jarat_hozzaadasa(BelfoldiJarat("BF123", "Budapest", 15000))
    legitarsasag.jarat_hozzaadasa(NemzetkoziJarat("NZ456", "London", 50000))
    legitarsasag.jarat_hozzaadasa(NemzetkoziJarat("NZ789", "New York", 120000))

    # Létrehozzuk a foglalási rendszert
    rendszer = FoglalasiRendszer(legitarsasag)

    # Előre feltöltött foglalások
    rendszer.jegy_foglalasa("Kiss Anna", "BF123")
    rendszer.jegy_foglalasa("Nagy Péter", "NZ456")
    rendszer.jegy_foglalasa("Szabó Lili", "NZ789")
    rendszer.jegy_foglalasa("Tóth Ádám", "BF123")
    rendszer.jegy_foglalasa("Molnár Dóra", "NZ456")
    rendszer.jegy_foglalasa("Varga Gábor", "NZ789")

    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("5. Járatonkénti foglalás statisztika")
        print("6. Foglalások mentése fájlba")

        print("0. Kilépés")
        valasztas = input("Válassz egy műveletet: ")

        if valasztas == "1":
            legitarsasag.jaratok_listazasa()
        elif valasztas == "2":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            rendszer.jegy_foglalasa(nev, jaratszam)
        elif valasztas == "3":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            rendszer.foglalas_lemondasa(nev, jaratszam)
        elif valasztas == "4":
            rendszer.foglalasok_listazasa()
        elif valasztas == "5":
            rendszer.foglalasok_jaratonkent()
        elif valasztas == "6":
            rendszer.foglalasok_mentese_csv()
        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
