from src.driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class Actions:
    def __init__(self):
        self.driver = get_driver()

    def __call__(self, operation, args=None, *element):

        driver = self.driver

        def _find_element(*element):
            return WebDriverWait(driver, 100).until(
                lambda x: driver.find_element(*element)
            )

        if operation == 'click':
            getattr(_find_element(*element), operation)()
        else:
            getattr(_find_element(*element), operation)(args)


act = Actions()
act.driver.get('https://soatest.alsc.bayer.biz/ALSCWebApp/login.html')
element = By.NAME, 'sSubmit'
username = By.ID, 'logintxt'
act('send_keys', 'hello', *username)
act('click', None, *element)
time.sleep(10)
act.driver.quit()
