##
# Dati sulla pandemia prelevati dal sito
# https://lab24.ilsole24ore.com/coronavirus/
#
#

import bs4  # BeautifulSoup
import requests
import time

data_rilevamento = time.strftime("\n%d/%m/%Y %H:%M:%S\n")
report = open("C:\\Users\\danie\\Desktop\\ScRiPt\\covid19.txt",'a')

report_txt = ['Nuovi casi',
              'Morti',
              'Dimessi//Guariti',
              'Terapia intensiva',
              'Attualmente positivi',
              'Ricoverati con sintomi',
              'Isolamento domiciliare']
results = []
cov19 = []

page = requests.get('https://lab24.ilsole24ore.com/coronavirus/')
soup = bs4.BeautifulSoup(page.text, "html.parser")

# Estrazione dati dal sito (Scraping)
# Il formato dei 6 dati numerici è :
# h2#num_x.timer.count-number
# dove la 'x' è il numero assegnato al dato
# e va da 1 a 6 , ma non in ordine cronologico
# perchè voglio visualizzarli nella stessa
# sequenza del sito
testa = "h2#num_"

coda = ".timer.count-number"
cerca = testa + "5_top" + coda
element = soup.select(cerca)
if element != []:
    results.append(element[1].text)

coda1 = ".timer.count-number"
for i in range(0, 5):
    # formatto la stringa per poterla cercare
    cerca = testa + str(i) + coda1
    element = soup.select(cerca)
    if element != []:
        results.append(element[0].text)
coda2 = "_top.timer.count-number"
for i in range(5, 8):
    cerca = testa + str(i) + coda2
    element = soup.select(cerca)
    results.append(element[0].text)

# Ordino i dati in una nuova lista
cov19.append(results[3]) # Nuovi casi
cov19.append(results[2]) # Morti
cov19.append(results[0]) # Dimessi
cov19.append(results[5]) # Terapia int.
cov19.append(results[1]) # Positivi
cov19.append(results[4]) # Ricoverati
cov19.append(results[6]) # Isol.domiciliare

# Salvo i dati allineati su file
report.write(data_rilevamento)
for i in range(len(cov19)):
    # print("%24s" % report_txt[i],"%10s" % cov19[i])
    ncov = str(cov19[i])
    print(f"{report_txt[i]}  {ncov.lstrip()}\n")
    # report.write("%-24s%10s\n" % (report_txt[i],cov19[i]))
    report.write("%s %s \n" % (report_txt[i] , ncov.lstrip()) )
report.write("-" * 35)
report.write('\n')
report.close()
