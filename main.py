from jarat import BelfoldiJarat, NemzetkoziJarat
from legitarsasag import LegiTarsasag
from foglalasirendszer import FoglalasiRendszer
from datetime import datetime

def main():
    # Létrehozunk egy légitársaságot
    legitarsasag = LegiTarsasag("AtaFly_D12H4E")

    # Hozzáadunk 3 járatot
    legitarsasag.jarat_hozzaadasa(BelfoldiJarat("ABC123", "Budapest", 55000, datetime(2025, 3, 1, 12, 0)))
    legitarsasag.jarat_hozzaadasa(NemzetkoziJarat("VA456", "London", 40000, datetime(2025, 6, 1, 15, 30)))
    legitarsasag.jarat_hozzaadasa(NemzetkoziJarat("FT789", "New York", 220000, datetime(2025, 6, 2, 9, 0)))

    # Létrehozzuk a foglalási rendszert
    rendszer = FoglalasiRendszer(legitarsasag)

    # Előre feltöltött foglalások
    rendszer.jegy_foglalasa("Kiss Anna", "ABC123")
    rendszer.jegy_foglalasa("Nagy Péter", "VA456")
    rendszer.jegy_foglalasa("Szabó Lili", "FT789")
    rendszer.jegy_foglalasa("Tóth Ádám", "ABC123")
    rendszer.jegy_foglalasa("Molnár Dóra", "VA456")
    rendszer.jegy_foglalasa("Varga Gábor", "FT789")

    while True:
        print(f"\n--- Repülőjegy Foglalási Rendszer --- ({legitarsasag.nev})")
        print("1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("5. Járatonkénti foglalás statisztika")
        print("6. Foglalások mentése fájlba")
        print("7. Összes jegybevétel megtekintése")
        print("0. Kilépés")
        valasztas = input("Válassz egy műveletet: ")

        if valasztas == "1":
            legitarsasag.jaratok_listazasa()
        elif valasztas == "2":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járat számát: ")
            rendszer.jegy_foglalasa(nev, jaratszam)
        elif valasztas == "3":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járat számát: ")
            rendszer.foglalas_lemondasa(nev, jaratszam)
        elif valasztas == "4":
            rendszer.foglalasok_listazasa()
        elif valasztas == "5":
            rendszer.foglalasok_jaratonkent()
        elif valasztas == "6":
            rendszer.foglalasok_mentese_csv()
        elif valasztas == "7":
            rendszer.ossz_bevetel()
        elif valasztas == "0":
            print("Befejezés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
