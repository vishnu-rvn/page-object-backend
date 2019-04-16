from testcases import testcase_one, testcase_two
from src.base import BaseTCList


class TCList(BaseTCList):
    tc1 = testcase_one.TestCaseOne
    tc2 = testcase_two.TestCaseTwo
