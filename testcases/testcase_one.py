from src import base
from pages import login_page, home_page


class TestCaseOne(base.BaseTestCase,
                  login_page.LoginPage,
                  home_page.HomePage):
    __title__ = 'first test case'

    def step_one(self):
        self.driver.get('https://www.phptravels.net/login')

    def step_two(self):
        self.login('user@phptravels.com', 'demouser')

    def step_three(self):
        self.driver.quit()
