# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


BROWSER = None


def start_browser():
    options = Options()
    options.binary_location = '/usr/bin/firefox'
    service = Service('/usr/bin/geckodriver')
    browser = webdriver.Firefox(service=service, options=options)
    return browser


def get_browser():
    global BROWSER
    if BROWSER is None:
        BROWSER = start_browser()
    return BROWSER
