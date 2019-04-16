from src import base


class TestCaseTwo(base.BaseTestCase):
    __title__ = 'second test case'

    def step_four(self):
        return 'one'+self.driver

    def step_five(self):
        return 'two'+self.driver

    def step_six(self):
        return 'three'+self.driver
