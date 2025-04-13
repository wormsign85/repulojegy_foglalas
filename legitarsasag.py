class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        if not self.jaratok:
            print("Nincsenek járatok.")
        else:
            for jarat in self.jaratok:
                print(jarat)

    def jarat_keresese(self, jaratszam):
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None
