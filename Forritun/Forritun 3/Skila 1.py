# Einar Karl Pétursson
# 23/8/2019


class Invoice:

    # creates a new Invoice with the specified values
    def __init__(self, partNumber, partDescription, quantity, pricePerItem):
        self.partNumber = partNumber
        self.partDescription = partDescription
        self.quantity = quantity
        self.pricePerItem = pricePerItem

    # Calculate InvoiceAmount
    def getInvoiceAmount(self):
        return self.quantity * self.pricePerItem

    def printInvoice(self):
        print('Partnumber: {}\nPart Description: {}\nQuantity: {}\nPrice Per Item: {}'
        .format(self.partNumber, self.partDescription, self.quantity, self.pricePerItem))


def readFile(nafnTxtSkra):  # Les skrána með csv.reader og smíðar invoice object úr  hverri línu fyrir sig.
    # try except finally
    try:
        skra = open(nafnTxtSkra, "r", encoding="utf-8")  # opnar skrá
        listi = (skra.read().split(';'))  # Les innihald án bila????
        skra.close()  # Lokar skrá
        return listi  # Skilar lista
    except:
        print("Það er ekkert í skránni")


def writeFile():  # Skrifar innihald listans invoiceList í skrána invoice.csv
    pass  # try except finally


def addInvoice():  # Bætir reikningi við listann
    pass


def printInvoices():  # Prentar(á skjáinn) alla reikninga ásamt heildarupphæð reiknings.
    pass


print("Les Skrá")
listi = readFile('invoice.csv')
print(listi)