# Einar Karl Pétursson
# 23/8/2019
import csv
invoices = []


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


def readFile(filename):  # Les skrána með csv.reader og smíðar invoice object úr  hverri línu fyrir sig.
    file = None
    try:
        file = open(filename, "r", newline='\r\n', encoding="utf-8")
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            invoice = Invoice(row[0], row[1], row[2], row[3])
            invoices.append(invoice)
    except IOError:
        print('An error occured trying to read the file')
    finally:
        print('(Skrá Lesin)')
        if file != None:
            file.close()


def delInvoice():
    print("Delete Invoice")
    index = -1
    partnumber = input("Partnumber to delete: ")
    for invoice in invoices:
        index = index + 1
        if invoice.partNumber == partnumber:
            del invoices[index]
            break


def updateInvoice():
    print("Update Invoice")
    partnumberToUpdate = input("Partnr: ")
    newprice = input("PriceperItem")
    for invoice in invoices:
        if invoice.partNumber == partnumberToUpdate:
            invoice.pricePerItem = newprice
            break


def writeFile(filename):  # Skrifar innihald listans invoiceList í skrána invoice.csv
    file = None
    try:
        file = open(filename, "w", newline='\r\n', encoding="utf-8")
        for invoice in invoices:
            line = invoice.partNumber + ";" + invoice.partDescription + ";" + invoice.quantity + ";" + invoice.pricePerItem + "\n"
            file.write(line)
    except IOError:
        print("An error has occured")
    finally:
        print("Finished")
        if file != None:
            file.close()


def addInvoice():  # Bætir reikningi við listann
    pass


def printInvoices():  # Prentar(á skjáinn) alla reikninga ásamt heildarupphæð reiknings.
    for invoice in invoices:
        invoice.printInvoice()
    print("")


print("(Les Skrá)")
readFile('invoice.csv')
print("---Skrá Prentuð---\n")
printInvoices()
addInvoice()
delInvoice()
print("update")
updateInvoice()

print("---Skrá Prentuð---\n")
printInvoices()
writeFile('invoice.csv')