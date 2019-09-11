# Einar Karl Pétursson
# 4/9/2019 - 11/9/2019
import csv
verkalydsfelag = []
medlimir = []
from klasi import Verkalydsfelag


def opnaSkra():
    file = None
    try:
        file = open('verkalydsfelag.csv', 'r', newline='', encoding='utf-8')
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            medlimir = Verkalydsfelag(row[0], row[1], row[2], row[3])
            verkalydsfelag.append(medlimir)
    except IOError:
        print('An error occured trying to read the file')
    finally:
        print('(Skrá Lesin)')
        if file != None:
            file.close()
    # Þetta fall á að opna skrána verkalydsfelag.csv. Lesa skrána.
    # Því næst býr fallið til tilvik(object,hlut) úr hverri línu skráarinnar og setur í lista.
    # Listinn innheldur þá hluti sem gerðir eru úr klasanum Verkalydsfelag.


def skrifaSkra():
    file = None
    try:
        file = open('verkalydsfelag.csv', "w", newline='\r\n', encoding="utf-8")
        for medlimir in verkalydsfelag:
            line = medlimir.nafn + ";" + medlimir.felagsnumer + ";" + medlimir.laun + ";" + medlimir.kennitala + "\n"
            file.write(line)
    except IOError:
        print("An error has occured")
    finally:
        print("Finished")
        if file != None:
            file.close()


def nyrMedlimur():
    nafn = input("Nafn til að bæta við: ")
    felagsnumer = input("Félagsnúmer: ")
    laun = input("Laun: ")
    kennitala = input("Kennitala: ")
    verkalydsfelag.append(Verkalydsfelag(nafn, felagsnumer, laun, kennitala))
    # bætir inn nýjum meðlimi tilviki(object,hluti)


def eydaMedlimi():
    index = -1
    partnumber = input("Meðlimsnúmer til að eyða: ")
    for medlimir in verkalydsfelag:
        index = index + 1
        if medlimir.partNumber == partnumber:
            del verkalydsfelag[index]
            break


def breytaMedlimi():
    nafnbreyta = input("Nafn meðlims til að breyta: ")
    nyttnafn = input("Nýtt nafn: ")
    nyttfelagsnumer = input("Nýtt Félagsnúmer: ")
    nyttlaun = input("Nýtt Laun: ")
    nyttkennitala = input("Nýtt Kennitala: ")
    for medlimir in verkalydsfelag:
        if medlimir.nafn == nafnbreyta:
            medlimir.nafn = nyttnafn
            medlimir.felagsnumer = nyttfelagsnumer
            medlimir.laun = nyttlaun
            medlimir.kennitala = nyttkennitala
            break
    # breytir tilviki(object,hluti)


def prentaVerkalydsfelag():
    for medlimir in verkalydsfelag:
        medlimir.prenta_upplisyngar_um_medlim()
    # skrifar á skjáinn allt sem er í skránni(innhald listans af tilvikum)


def nafnLaun():
    print("Nafn og Laun:")
    for medlimir in verkalydsfelag:
        medlimir.nafn_laun()
    # skrifar á skjáinn nafn og laun hvers meðlimar fyrir sig.


def utborgudlaun():
    print("Útborguð laun:")
    for medlimir in verkalydsfelag:
        medlimir.utborgud_laun()
    # Útborguð laun hvers meðlimar verkalýðsfélagsins


def heildarskattar():
    print("Heildarskattar:")
    for medlimir in verkalydsfelag:
        medlimir.skatt()
    # skrifar á skjáinn heildarskatta allra meðlima verkalýðsfélagsins


def kennitolur():
    print("Kennitölur:")
    for medlimir in verkalydsfelag:
        medlimir.kt()


val = ""
while val != "0":
    print("\n------ Valmynd ------\n")
    print("1. Opna Skrá\n2. Skrifa í skrá (Ef bætt eða breytt var)\n3. Nýr meðlimur\n4. Eyða meðlim\n5. Breyta meðlim")
    print("6. Prenta Verkalýðsfélag\n7. Nafn og Laun\n8. Útborguð laun\n9. Heildarskattar\n10. Mitt Fall (Kennitala)")
    val = input("Veldu 1-10 eða 0 til að hætta ")
    print()
    if val == "1":
        opnaSkra()
    elif val == "2":
        skrifaSkra()
    elif val == "3":
        nyrMedlimur()
    elif val == "4":
        eydaMedlimi()
    elif val == "5":
        breytaMedlimi()
    elif val == "6":
        prentaVerkalydsfelag()
    elif val == "7":
        nafnLaun()
    elif val == "8":
        utborgudlaun()
    elif val == "9":
        heildarskattar()
    elif val == "10":
        kennitolur()
    elif val == "0":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")
