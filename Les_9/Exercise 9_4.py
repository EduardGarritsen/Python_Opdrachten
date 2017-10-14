import csv

with open('newfile.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))

    writer.writerow(('121','ABC123','Highlight pen','231','0.56'))
    writer.writerow(('123','PQR678','Nietmachine','587','9.99'))
    writer.writerow(('128','ZYX163','Burealamp','34','19.95'))
    writer.writerow(('137','MLK709','Monitorstandaard','66','32.50'))
    writer.writerow(('271','TRS665','Ipad hoes','155','19.01'))


with open('newfile.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    your_list = list(reader)
