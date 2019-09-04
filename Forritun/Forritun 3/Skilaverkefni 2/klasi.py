# Einar Karl Pétursson
# 4/9/2019


class Verkalydsfelag:
    def __init__(self, nafn, felagsnumer, laun, kennitala):
        self.nafn = nafn
        self.felagsnumer = felagsnumer
        self.laun = laun
        self.kennitala = kennitala

        # Reiknar skatt meðlims
    def skatt(self):
        return int(self.laun)*0.36  # Skattur 36%

        # Reikna skatt meðlims
    def utborgud_laun(self):
        pass

        # Prentar út upplýsingar
    def prenta_upplisyngar_um_medlim(self):
        pass
