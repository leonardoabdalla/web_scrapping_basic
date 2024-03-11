from selenium import webdriver
from time import sleep
import webbrowser
from termcolor import colored as color
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import os

class web_scrapping_vendas:
    def raspagem_de_dados():

        try:
            options = webdriver.FirefoxOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--start-maximized')

            browser = webdriver.Firefox()
            browser.get("https://www.google.com.br")

            search_input = browser.find_element("name", "q")
            search_input.send_keys("Geladeira Eletrolux Frossfree")
            search_input.send_keys(Keys.ENTER)
            sleep(3)
            shopping = browser.find_element(By.CSS_SELECTOR, ".IUOThf > div:nth-child(1) > a:nth-child(1)")
            shopping.click()
            sleep(3)
            price = browser.find_element("name", "upper")
            price.send_keys("2000")
            sleep(2)
            send_price = browser.find_element(By.CLASS_NAME, "sh-dr__prs")
            send_price.click()
            sleep(2)
            number_of_doors = browser.find_element(By.XPATH, '//span[text()="Geladeiras com 2 portas"]/ancestor::a')
            number_of_doors.click()
            sleep(2)
            items = []

            for refrigerator in browser.find_elements(By.CLASS_NAME, "sh-dgr__gr-auto"):
                new_item = {}
                new_item["title"] = (
                    refrigerator.find_element(By.TAG_NAME, "h3").get_attribute("innerHTML")
                )
                new_item['link'] = (
                    refrigerator.find_element(By.TAG_NAME, "a").get_attribute("href")
                )
                new_item['price'] = (
                    refrigerator.find_element(By.XPATH, "//span/b").text
                )
                new_item['name_store'] = (
                    refrigerator.find_element(By.XPATH, "/html/body/div[5]/div/div[4]/div[3]/div/div[3]/div[1]/g-scrolling-carousel/div[1]/div/div/div[1]/a/div[2]/div/div[2]/span").text
                )
                new_item['img'] = (
                    refrigerator.find_element(By.TAG_NAME, "img").get_attribute("src")
                )
                items.append(new_item)

            print(items)
            print(color("Page Title is : %s" %browser.title), 'green')
            input(color("Enter para sair", 'red'))
            browser.quit()
        
        except NoSuchElementException:
            print("Element not found")

        except ElementClickInterceptedException:
            print("Unable to click on element")

    def contato_com_cliente():

        try:

            url_whats = "https://web.whatsapp.com/"

            '''

            firefox = webbrowser.Mozilla(r"C:\Program Files\Mozilla Firefox\firefox.exe")

            firefox.open(url_whats)

            input(color("Se já escaneou ENTER", 'green'))

            time.sleep(1)

            '''
        
            options = webdriver.FirefoxOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--start-maximized')

            myprofile = webdriver.FirefoxProfile(os.enviroment[r'PATH_USER'])
            driver = webdriver.Firefox(firefox_profile=myprofile)
            driver.get(url_whats)

            sleep(5)

            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]")
            element.click()
            sleep(2)
            sendMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
            name = "testando api para ver se vai dar certo"
            for i in name:
                sendMessage.send_keys(i)

            sleep(2)
            sendMessage.send_keys(Keys.ENTER)

            sleep(3)

            print(color("Page Title is : %s" %driver.title), 'green')
            input(color("Enter para sair", 'red'))
            driver.quit()

        except NoSuchElementException:
            print("Element not found")

        except ElementClickInterceptedException:
            print("Unable to click on element")
    
    raspagem_de_dados()
    # contato_com_cliente()

web_scrapping_vendas()