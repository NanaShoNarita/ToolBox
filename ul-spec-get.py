import requests
from bs4 import BeautifulSoup as bs
import pdfkit
import os

main_pg = 'https://iq.ul.com/awm/File.aspx?FN=E51301'
spec_pg = 'https://iq.ul.com/awm/'
pth = os.path.abspath('/Users/belack/Python/UL-Specs/PDFs/')


def pg_content(webpg):
    r = requests.get(webpg)
    c = r.content
    return(c)


def make_soup(pg):
    s = bs(pg, 'html.parser')
    return(s)


list_pg = pg_content(main_pg)
apg = make_soup(list_pg)
# print(apg)

links = []

for a in apg.find_all('a', href=True):
    links.append((str(a)))

filter1 = 'stylepage'

spec = [x for x in links if filter1 in x]

for s in spec:
    n = make_soup(s)
    l = n.find('a').get('href')
    lk = spec_pg + str(l)
    t = n.text.strip()
    file_name = 'UL-' + t + '.pdf'
    save_file = os.path.join(pth, file_name)
    pdfkit.from_url(lk, save_file)
