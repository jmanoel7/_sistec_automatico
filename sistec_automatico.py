# -*- coding: utf-8 -*-


import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from browser import get_browser


get_browser().get('https://sistec.mec.gov.br/')
sleep(5)
xpath = '//*[@id="tipo"]'
time_out = 2

while True:
    try:
        select_element = get_browser().find_element(By.XPATH, xpath)
    except NoSuchElementException:
        sleep(time_out)
        continue
    break

sistec_html = select_element.get_property('outerHTML')
sistec_html = sistec_html.encode('utf-8')
f = open('/home/joaomanoel/temp/sistec.html', 'wb')
f.write(sistec_html)
f.close()

cookies = []
cookie_phpsessid = get_browser().get_cookie('PHPSESSID')
cookie_phpsessid = json.dumps(cookie_phpsessid, indent=4)
cookies.append(cookie_phpsessid)
cookies = ',\n'.join(cookies)
cookies = '[\n%s\n]' % cookies
cookies = cookies.encode('utf-8')
f = open('/home/joaomanoel/temp/cookies.json', 'wb')
f.write(cookies)
f.close()

get_browser().get('http://aguia:8080/sistec_download')
sleep(time_out)

xpath = '//*[@id="cookies"]'
cookie_element = get_browser().find_element(By.XPATH, xpath)
cookie_element.send_keys('/home/joaomanoel/temp/cookies.json')

xpath = '//*[@id="sistec"]'
sistec_element = get_browser().find_element(By.XPATH, xpath)
sistec_element.send_keys('/home/joaomanoel/temp/sistec.html')

xpath = '/html/body/div[1]/form/p[3]/input'
upload_element = get_browser().find_element(By.XPATH, xpath)
upload_element.click()
