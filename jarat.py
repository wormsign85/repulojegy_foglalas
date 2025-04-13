from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar, indulas_idopont):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.indulas_idopont = indulas_idopont

    @abstractmethod
    def jarat_tipus(self):
        pass

    def __str__(self):
        return f"{self.jarat_tipus()} - {self.jaratszam} ({self.celallomas}) | Ár: {self.jegyar} Ft | Indulás: {self.indulas_idopont}"


class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi járat"


class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi járat"
