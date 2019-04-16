import inspect
from selenium.webdriver.support.ui import WebDriverWait
from src.driver import get_driver


class BasePageLocator:
    def __init__(self):
        self.driver = get_driver()

    def element(self, locators):
        driver = self.driver
        web_element = WebDriverWait(driver, 100).until(
            lambda d: driver.find_element(*locators)
        )
        return web_element


class BaseTestCase:

    @classmethod
    def get_tc_steps(cls):
        return dict(filter(lambda x: inspect.isfunction(x[1]), cls.__dict__.items()))


class BaseTCList:

    @classmethod
    def get_tc_list(cls):
        class_dict = dict(filter(lambda x: inspect.isclass(x[1]), cls.__dict__.items()))
        tc_list = []
        for tc_name, tc_class in class_dict.items():
            tc_list.append({
                'value': tc_name,
                'title': tc_class.__title__
            })
        return tc_list

    @classmethod
    def get_tc(cls, tc_name):
        return getattr(cls, tc_name)

    @classmethod
    def get_tc_title(cls, tc_name):
        return getattr(cls, tc_name).__title__
