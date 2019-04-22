from selenium import webdriver
import os

from .utilities import cache


BASE_DIR = os.path.dirname(__file__)
DRIVER_PATH = "C:\\Users\\v.raveendran\\Documents\\object_model\\backend\\driver_engine\\drivers\\chromedriver.exe"


class InitDriver:
    def __init__(self):
        self._driver = None

    def create_driver(self):
        self._driver = webdriver.Chrome(DRIVER_PATH)

    @property
    def driver(self):
        return self._driver