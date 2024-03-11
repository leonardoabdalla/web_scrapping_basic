from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

class speed_test:
    def conection_test():
        try:
            options = webdriver.FirefoxOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--start-maximized')

            firefox = webdriver.Firefox()

            firefox.get("https://www.google.com.br")

            search_input = firefox.find_element("name", "q")
            search_input.send_keys("speed test")


            search_input.send_keys(Keys.ENTER)
            sleep(3)

            speedtest_link = firefox.find_element(By.XPATH, "/html/body/div[5]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
            speedtest_link.click()

            sleep(3)

            click_speed_test = firefox.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
            click_speed_test.click()

            sleep(2)
        except NoSuchElementException:
            print("Element not found")

        except ElementClickInterceptedException:
            print("Unable to click on element")
    conection_test()
speed_test()