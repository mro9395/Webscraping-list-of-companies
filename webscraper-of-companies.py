from urllib.request import FancyURLopener
from bs4 import BeautifulSoup

import sys
from importlib import reload
reload(sys)
#sys.setdefaultencoding('utf-8')
#import codecs
#import unicodedata
from unidecode import unidecode


class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()

f=open('file-split-urlciiu.txt','r')

industries=f.readlines()

f=open('file-list-companies.txt','w')
for element in industries:

    for x in range(0, 90):
        new_element=element[:-2]
        html = myopener.open(new_element+str(x)).read()
        soup = BeautifulSoup(html)
        if soup.find('li', class_="disabled") == None:

            list = soup.find_all('tr')

            for elem in list:
                s=unidecode(elem.get_text())
                a=str(s.encode('ascii'))
                f.write(a)
                f.write("--"*100+'\n')
            f.write('='*100)
            #for x in range(1,len(list)-1):
                #print(list[x].split('</a>')[0])#.split('">')[1])
            #for elem in list:
                #print(elem.get_text())
                #print(elem.split('</a>')[0])

            # companies=list_companies.find_all('tr')
            # companies=str(companies).split("</tr>")
            # print(companies)
            #print('=' * 100)
        else:
            pass

    #time_stamp lines   speed
    #12.01m 00000
    #12.03m 47000   23500 l/m
    #12.05m 78000   19500 l/m
    #12.08m 97000   13850 l/m
    #12.11m 12264   1226 l/m
    #12.16m 16714   1114 l/m
    #12.21m 22380   1119 l/m
    #12.26m 28234   1129 l/m
    #12.31m 38000   1266 l/m
    #12.37m 43174   1199 l/m
    #12.55m 62000   1148 l/m
