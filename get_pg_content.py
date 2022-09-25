import requests
from bs4 import BeautifulSoup as bs

pg = 'https://theawesomer.com'


def pg_content(webpg):
    r = requests.get(webpg)
    c = r.content
    return(c)


def make_soup(pg):
    pg_txt = pg_content(pg)
    s = bs(pg_txt, 'html.parser')
    return(s)


apg = make_soup(pg)
print(apg)
