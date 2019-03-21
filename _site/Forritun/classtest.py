# Einar Karl Pétursson
# 19/3/2019


class Reikna():
    def samlagning(tala1, tala2):
        utkoma = tala1+tala2
        return utkoma

    def margfoldun(tala1, tala2):
        utkoma = tala1*tala2
        return utkoma

    def deiling(tala1, tala2):
        utkoma = tala1/tala2
        return utkoma


print(Reikna.samlagning(5,7))


class Persona():
    def __init__(self, n, a, h):
        self.nafn = n
        self.aldur = a
        self.heimili = h

    def __str__(self):
        return "Nafn: " + self.nafn + " aldur:" + str(self.aldur)


p1 = Persona("Einar Karl", 16, "Álfaheiði 18")
p2 = Persona("Guðmundur", 16, "Örugglega heimilislaus")
print("Nafn:", p1.nafn, p1.aldur, p1.heimili)
print(p2.nafn, p2.aldur, p2.heimili)