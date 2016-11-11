# Webscraper in Python2

from bs4 import BeautifulSoup
from urllib import FancyURLopener
import re

import sys
from imp import reload

from unidecode import unidecode
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
import unicodedata


class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()


def limpiar(var):
    return unidecode(var.replace('Raz\xc3\xb3n social: ', '').replace('Nombre comercial: ', '|').replace('RUC: ', '|').
                     replace('Inicio de actividades: ', '|').replace('Actividad de comercio exterior: ', '|').
                     replace('Direci\xc3\xb3n: ', '|').replace('Tel\xc3\xa8fono: ', '|').replace('Fax: ', '|').
                     replace('Condici\xc3\xb3n: ', '|').replace('Estado: ', '|').
                     replace('Datos actualizados al: ', '|')).replace('Telefono: ', '|').replace('TelA(c)fono: ', '|').\
        encode('ascii')

# Open and read of urls and industries
f = open('file-split-urlciiu.txt', 'r')
g = open('file-split-ciiu.txt', 'r')
industriesURL = f.readlines()
industries = g.readlines()

# Print header
f = open('file-lista-empresas.txt', 'w')
f.write('Razon social|Nombre comercial|RUC|Inicio de actividades'
        '|Comercio Exterior|Direccion|Telefono|Fax|Condicion|Estado|Fecha actualizada|CIIU'+'\n')

y = 0  # Industry counter
# Iterates each industry URL
for element1 in industriesURL:
    x = 1  # URL counter starting at 1
    new_element = element1[:-2].replace('\xc3', 'n')  # Clean the URL from variable items and special characters
    soup = BeautifulSoup(myopener.open(new_element + '0').read())  # Scrape and read URL counter 0
    list = soup.find_all('tr')  # Search for 'tr' tag and get company information
    # Iterates each company of URL counter 0, list[1] is a header
    for elem in list[1:]:
        a = str(unidecode(elem.get_text()).encode('ascii')).split('\n')  # Split ID, name1, name2
        companyURL = 'http://www.razonsocialperu.com/empresa/detalle/' + a[1] + '\n'  # URL using company ID
        companySoup = BeautifulSoup(myopener.open(companyURL).read())\
            .find_all('ul', class_='iconlist-color clearfix')  # Scrape, read and find specific company fields
        # Iterates each field
        for item in companySoup:
            f.write(limpiar(item.get_text()).replace('\n', '') + '|' + industries[y])  # Printing after cleaning fields
    # Iterates each company of URL counter 1+, while next option is available
    while BeautifulSoup(myopener.open(new_element + str(x)).read()).find('li', class_="disabled") is None:
        soup = BeautifulSoup(myopener.open(new_element + str(x)).read())  # Scrape and read UR counter 1+
        try:  # Exception of codification
            try:
                list = soup.find_all('tr')  # Find all 'tr' tag and get company information
                for elem in list[1:]:
                    a = str(unidecode(elem.get_text()).encode('ascii')).split('\n')
                    companyURL = 'http://www.razonsocialperu.com/empresa/detalle/' + a[1] + '\n'
                    companySoup = BeautifulSoup(myopener.open(companyURL).read())\
                        .find_all('ul', class_='iconlist-color clearfix')
                    for item in companySoup:
                        f.write(limpiar(item.get_text().replace('\n', '')) + '|' + industries[y])
            except UnicodeError:
                print 'UnicodeError'
        except UnicodeEncodeError:
            print 'UnicodeEncodeError'
        x += 1  # Increase the URL counter
    y += 1  # Go to next industry
