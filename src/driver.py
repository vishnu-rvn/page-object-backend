from selenium import webdriver
from utils import cache
import json
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
CHROME_PATH = os.path.join(BASE_PATH, 'drivers/chromedriver.exe')
FIREFOX_PATH = os.path.join(BASE_PATH, 'drivers/geckodriver.exe')
IE_PATH = os.path.join(BASE_PATH, 'drivers/IEDriverServer.exe')
SETTINGS_PATH = os.path.join(BASE_PATH, 'settings.json')


def parse_settings_driver():
    with open(SETTINGS_PATH, 'r') as file:
        content = json.load(file)
    return content.get('driver')


@cache
def get_driver():
    browser = parse_settings_driver()
    try:
        if browser.strip().lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-extensions')
            return webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=options)
        elif browser.strip().lower() == 'firefox':
            return webdriver.Firefox(FIREFOX_PATH)
        elif browser.strip().lower() == 'ie':
            return webdriver.Ie(IE_PATH)
        else:
            raise NameError('Invalid browser name')
    except FileNotFoundError:
        raise FileNotFoundError('Browser needs to be in path, {} current path invalid'.format(CHROME_PATH))
