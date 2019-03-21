# Einar Karl Pétursson
# 19/3/2019


class FyrstiKlasi:
    def nafnAldur(nafn, aldur):
        print("Halló", nafn, "þú ert", aldur, "ára gamall")

    def tolur(tala1, tala2):
        return "Það eru", tala1-tala2, "tölur á milli", tala1, "og", tala2


nafn = input("NAFN: ")
aldur = int(input("ALDUR: "))
FyrstiKlasi.nafnAldur(nafn, aldur)


class AnnarKlasi:
    def hm(self):
        pass


class ThridjiKlasi:
    def __init__(self, t1, t2):
        self.tala1 = t1
        self.tala2 = t2

    def samlagning(self):
        utkoma = self.tala1 + self.tala2
        return utkoma

    def margfoldun(self):
        utkoma = self.tala1 * self.tala2
        return utkoma

    def deiling(self):
        utkoma = self.tala1 / self.tala2
        return utkoma

t1 = ThridjiKlasi(20,50)
t2 = ThridjiKlasi(100,5)
print("t1 lagt saman er:", t1.samlagning())
print("t2 lagt saman er:", t2.samlagning())