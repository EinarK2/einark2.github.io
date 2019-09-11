# Einar Karl Pétursson
import csv
from klasi import Verkalydsfelag
verkalydsfelag = []


def opnaSkra():
    with open('verkalydsfelag.csv', 'r', newline='', encoding='utf-8')as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)
            hlutur = Verkalydsfelag(row[0], row[1], row[2, row[3]])
            verkalydsfelag.append(hlutur)
    # Þetta fall á að opna skrána verkalydsfelag.csv. Lesa skrána.
    # Því næst býr fallið til tilvik(object,hlut) úr hverri línu skráarinnar og setur í lista.
    # Listinn innheldur þá hluti sem gerðir eru úr klasanum Verkalydsfelag.


def skrifaSkra():
    file = open('verkalydsfelag.csv', "w", newline='\r\n', encoding="utf-8")
    for medlimir in verkalydsfelag:
        line = medlimir.nafn + ";" + medlimir.felagsnumer + ";" + medlimir.laun + ";" + medlimir.kennitala + "\n"
        file.write(line)


def nyrMedlimur():
    pass  # bætir inn nýjum meðlimi tilviki(object,hluti)


def eydaMedlimi():
    pass  # eyðir tilviki(object,hluti)


def breytaMedlimi():
    pass  # breytir tilviki(object,hluti)


def prentaVerkalydsfelag():
    pass  # skrifar á skjáinn allt sem er í skránni(innhald listans af tilvikum)


def nafnLaun():
    pass  # skrifar á skjáinn nafn og laun hvers meðlimar fyrir sig.


def utborgudlaun():
    pass  # Útborguð laun hvers meðlimar verkalýðsfélagsins


def heildarskattar():
    pass  # skrifar á skjáinn heildarskatta allra meðlima verkalýðsfélagsins


def mittFall(): # nefnið fallið einhverju lýsandi nafni
    pass  # frjálst val. Samt eitthvað spennandi og flott

val = ""
while val != 0:
    print("valmynd")
    print("1. \n2. \n 3. \n")
    val = input("Veldu")
    if val == "1":
        pass
    elif val == "2":
        pass