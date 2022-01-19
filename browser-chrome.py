# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/usr/bin/google-chrome-stable'
    service = Service('/usr/bin/chromedriver')
    browser = webdriver.Chrome(service=service, options=options)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
