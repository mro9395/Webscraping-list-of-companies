from urllib.request import FancyURLopener
from bs4 import BeautifulSoup


class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


myopener = MyOpener()

mainURL = 'http://www.razonsocialperu.com/'
html_industries = myopener.open(mainURL).read()
soup = BeautifulSoup(html_industries)

print(soup.prettify())
print('=' * 100)

# Using soup
# industries=soup.find_all('a',class_='list-group-item')


# f=open('file-soup.txt','w')
# test = {}
# for element in industries:
# test[element.a.get_text()]["link"]=element.a["href"]
# print(element.a.get())
# print(test[element]["link"])
# print(element.get_text())             #works
# f.write(element.get_text()+'\n')      #works

# for item in test.keys():
# print(item)
# print(test[item]["link"])



# print(industries)

# Using split
industries = str(soup.find_all('a', class_='list-group-item'))
industries = industries.split("- ")

f = open('file-split-ciiu.txt', 'w')
print(industries)
for x in range(1, len(industries)):
    print(industries[x].split("<")[0])
    f.write(industries[x].split("<")[0] + '\n')

f = open('file-split-urlciiu.txt', 'w')
for x in range(0, len(industries) - 1):
    print(industries[x].split("//")[1].split('"')[0])
    f.write('http://' + industries[x].split("//")[1].split('"')[0] + '\n')
    # url=url + industries[x].split("//")[1].split('"')[0])
