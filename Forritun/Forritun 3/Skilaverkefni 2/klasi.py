# Einar Karl Pétursson
# 4/9/2019 - 11/9/2019


class Verkalydsfelag:
    def __init__(self, nafn, felagsnumer, laun, kennitala):
        self.nafn = nafn
        self.felagsnumer = felagsnumer
        self.laun = laun
        self.kennitala = kennitala

        # Reiknar skatt meðlims
    def skatt(self):
        print(int(self.laun)*0.36)  # Skattur 36%

        # Reikna skatt meðlims
    def utborgud_laun(self):
        print(int(self.laun)-(int(self.laun)*0.36))

    def nafn_laun(self):
        print(self.nafn + " " + self.laun)
        # Prentar út upplýsingar

    def kt(self):
        print(self.kennitala)

    def prenta_upplisyngar_um_medlim(self):
        print('Nafn: {}\nFélagsnúmer: {}\nLaun: {}\nKennitala: {} \n'
        .format(self.nafn, self.felagsnumer, self.laun, self.kennitala))
