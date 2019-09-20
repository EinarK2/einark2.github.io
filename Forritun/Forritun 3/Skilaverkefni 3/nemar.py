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

    def __str__(self):
        return "Kennitala: {}\nNafn: {}\nKyn: {}\nHeimilisfang: {}\nSímanúmer: {}\nNetfang: {}"\
            .format(self.kt, self.nafn, self.kyn, self.heimilisfang, self.gsm, self.mail)


class Grunnskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, gsm, mail, forradamadur, nafnskola):
        super().__init__(kt, nafn, kyn, heimilisfang, gsm, mail)
        self.forradamadur = forradamadur
        self.nafnskola = nafnskola

    def __str__(self):
        return "{}\nForráðamaður: {}\nNafn Skóla: {}"\
            .format(super().__str__(), self.forradamadur, self.nafnskola)


class Framhaldsskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, gsm, mail, braut, busetustyrkur):
        super().__init__(kt, nafn, kyn, heimilisfang, gsm, mail)
        self.braut = braut
        self.busetustyrkur = busetustyrkur

    def __str__(self):
        return "{}\nBraut: {}\nBúsetustyrkur: {}".format(super().__str__(), self.braut, self.busetustyrkur)


class Haskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, gsm, mail, grada, namslan):
        super().__init__(kt, nafn, kyn, heimilisfang, gsm, mail)
        self.grada = grada
        '''self.BSc = bsc
        self.MSc = msc
        self.PHd = phd'''
        self.namslan = namslan

    def __str__(self):
        return "{}\nGráða: {}\nNámslán: {}"\
            .format(super().__str__(), self.grada, self.namslan)
