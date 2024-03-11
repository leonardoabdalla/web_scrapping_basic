from selenium import webdriver

import time


class cookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {}

        self.driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver-win64")

        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def clicar_no_cookie(self):
        pass

    def pega_melhor_upgrade(self):
        pass

biscoito = cookieClicker()
biscoito.abrir_site()