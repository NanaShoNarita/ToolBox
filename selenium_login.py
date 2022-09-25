from bs4 import BeautifulSoup as BS
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re


ids = {}

srch = {}

rslts = {'tit': {'next': '.pageNav-jump'},
         'thots': {'next': '.pageNav-jump'},
         'vef': {'next': '.pageNav-jump'}}

test_keys = ['url', 'user', 'pwd', 'usr_input', 'pwd_input', 'login_btn']

test_sites = ['tit']

key_len = len(test_keys)
site_len = len(test_sites)

i = 0
h = 0

for s in test_sites:
    u = ids[f'{s}']
    for k in test_keys:
        d = u[f'{k}']
        print(d)


def pause():
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")


def send_text(css, txt):
    driver.find_element_by_css_selector(
        css).send_keys(txt)


def btn_click(css):
    driver.find_element_by_css_selector(css).click()


def pg_login(x):
    url = x['url']
    global driver
    driver = webdriver.Firefox()
    driver.get(url)
    # pause()
    user_box = x['usr_input']
    user_name = x['user']
    pwd_box = x['pwd_input']
    user_pwd = x['pwd']
    lg_btn = x['login_btn']
    # pause()
    send_text(user_box, user_name)
    send_text(pwd_box, user_pwd)
    btn_click(lg_btn)


def pg_sce():
    sce = driver.execute_script("return document.body.innerHTML;")
    return(sce)


def pg_srch(x):
    url = x['url']
    thrd = x['thrd_btn']
    input = x['search_input']
    src_start = Keys.ENTER
    driver.get(url)
    fnd = 'Hummelstown'
    pause()
    send_text(input, fnd)
    # btn_click(thrd)
    send_text(input, src_start)
    pause()
    pS = pg_sce()
    return(pS)


def src_runs(x):
    soup = BS(x, "html.parser")
    runs = str(soup.find_all('div', {'class': 'pageNavSimple'}))
    runs = BS(runs, "html.parser")
    runs = str(runs.find_all('a'))
    runs = runs.split('\n')
    runs = str([x for x in runs if ' of ' in x][0]).split(' of ')[1]
    return(runs)


def link_return(x, lst):
    soup = BS(x, "html.parser")
    k = str(soup.find_all('h3', {'class': 'contentRow-title'}))
    links = BS(k, ("html.parser"))
    k = links.find_all('a')
    for n in k:
        n = str(n['href'])
        lst.append(n)


def nxt_pg(x, n):
    n = str(n)
    rplc = re.compile(r'(.*/).*&q')
    m = '&page=' + n + '&q'
    new = re.sub(rplc, r'\1' + m, x)
    return(new)


found = []
for t in test_sites:
    p = 1
    pg_login(ids[t])
    r = pg_srch(srch[t])
    pause()
    link_return(r, found)
    t = src_runs(r)
    t = int(t)
    while p < t:
        print(len(found))
        p = p + 1
        address = driver.current_url
        new_pg = nxt_pg(address, p)
        print(new_pg)
        driver.get(new_pg)
        pause()
        r = pg_sce()
        link_return(r, found)

    driver.close()
