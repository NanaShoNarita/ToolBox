from bs4 import BeautifulSoup as BS
import os
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


master_scrape = []

state = "Pennsylvania"
wiki_pg = "https://en.wikipedia.org/wiki/List_of_towns_and_boroughs_in_"
wiki_state = wiki_pg + state


def wiki_towns(url):
    global driver
    driver = webdriver.Firefox()
    driver.get(url)
    pageSource = driver.execute_script("return document.body.innerHTML;")
    soup = BS(pageSource, "html.parser")
    twn = town_select(soup)
    return(twn)


def pause():
    wait = WebDriverWait(driver, 90)
    wait.until(EC.presence_of_element_located(
        (By.ID, 'displaymodes')))


def town_select(s):
    table = str(s.select('tbody'))
    t = BS(table, "html.parser")
    table = str(t.select('a')).replace('[', '').replace(']', '').split('Pennsylvania')
    table = [x for x in table if 'title' in x]
    table = str([x for x in table if 'County' not in x]).replace('" ', '').replace(', ', '')
    table = str(table.split('Template')[0]).replace("'", "").replace('"', '')
    table = table.split('title=')
    table = [x for x in table if len(x) > 2]
    return(table)


towns_list = wiki_towns(wiki_state)

state_var = [', Pennsylvania', ', PA', ',Pennsylvania', ',PA', '_Pennsylvania', '_PA', ',PennState']

src_var1 = []
i = 0
for s in state_var:
    for t in towns_list:
        nt = t + s
        src_var1.append(nt)

driver.close()


def src_input(url, pa_list):
    global driver
    driver = webdriver.Firefox()
    driver.get(url)
    for p in pa_list:
        driver.find_element_by_css_selector("i.fa-search").click()
        driver.find_element_by_css_selector(
            '#q').send_keys(p)
        driver.find_element_by_css_selector("span.fa").click()
        pg_data = driver.execute_script("return document.body.innerHTML;")
        soup = BS(pg_data, "html.parser")
        if 'No results' in str(soup):
            print('no dice')
        else:
            links = soup.find_all(class_="album-link")
            for l in links:
                n = str(l.get("href"))
                master_scrape.append(n)

    driver.close()


def capture_links(x):
    x = [str(y) for y in x]
    with open('/Users/belack/Python/searchPA/results.txt', 'w') as f:
        f.write(x)
        f.close()


src_input(erome, src_var1)
