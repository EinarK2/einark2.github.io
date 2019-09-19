# Einar Karl Pétursson
# 19/9/2019


class Nemi:
    def __init__(self, kt, nafn, kyn, heimilisfang, gsm, mail):
        self.kt = kt
        self.nafn = nafn
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.gsm = gsm
        self.mail = mail

    def prentainfo(self):
        print("Kennitala: {}\nNafn: {}\nKyn: {}\nHeimilisfang: {}\nSímanúmer: {}\nNetfang: {}"
        .format(self.kt, self.nafn, self.kyn, self.heimilisfang, self.gsm, self.mail))


class Grunnskolanemi:
    def __init__(self, forradamadur, nafnskola):
        self.forradamadur = forradamadur
        self.nafnskola = nafnskola


class Framhaldsskolanemi:
    def __init__(self, braut, busetustyrkur):
        self.braut = braut
        self.busetustyrkur = busetustyrkur


class Haskolanemi:
    def __init__(self, bsc, msc, phd, namslan):
        self.BSc = bsc
        self.MSc = msc
        self.PHd = phd
        self.namslan = namslan

