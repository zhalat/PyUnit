import logging
import unittest
from prettytable import PrettyTable


class TestListException(Exception):
    pass


class TestList:
    # empty list means all test shall be run
    test_suite_name_list = []
    test_case_name_list = []

    @staticmethod
    def add(test_suite="*", test_case="*"):
        if test_suite == "*" and test_case == "*":
            return
        else:
            if test_suite != "*":
                TestList.test_suite_name_list.append(test_suite)
            if test_case != "*":
                TestList.test_case_name_list.append(test_case)

    @staticmethod
    def clean_list(self):
        TestList.test_suite_name_list.clear()
        TestList.test_case_name_list.clear()

    @staticmethod
    def is_on_the_list(testSuiteName, testCaseName) -> bool:
        isTestSuiteOk = True
        if len(TestList.test_suite_name_list) != 0:
            isTestSuiteOk = testSuiteName in TestList.test_suite_name_list

        isTestCaseOk = True
        if len(TestList.test_case_name_list) != 0:
            isTestCaseOk = testCaseName in TestList.test_case_name_list

        return isTestSuiteOk and isTestCaseOk

    @staticmethod
    def validate_list():
        if 0 == len(TestList.test_suite_name_list) and len(TestList.test_case_name_list) > 0:
            logging.error("Test case must be assigned to test suite")
            raise (TestListException("Test suite must be provided"))

        # show test list
        x = PrettyTable()
        x.field_names = ["Test Suite", "Test Case"]
        if 0 == len(TestList.test_suite_name_list) and 0 == len(TestList.test_case_name_list):
            x.add_row(["*", "*"])

        for i in range(0, len(TestList.test_suite_name_list) + len(TestList.test_case_name_list)):
            if len(TestList.test_suite_name_list) > 0 and 0 == len(TestList.test_case_name_list) and i == 0:
                x.add_row([TestList.test_suite_name_list[i], "*"])
            elif i < len(TestList.test_suite_name_list) and i < len(TestList.test_case_name_list):
                x.add_row([TestList.test_suite_name_list[i], TestList.test_case_name_list[i]])
            elif i < len(TestList.test_suite_name_list):
                x.add_row([TestList.test_suite_name_list[i], ""])
            elif i < len(TestList.test_case_name_list):
                x.add_row(["", TestList.test_case_name_list[i]])
        logging.info(f"\n{x}")


def skip_decorator():
    def deco(f):
        def wrapper(self, *args, **kwargs):
            if not TestList.is_on_the_list(self.__class__.__name__, self._testMethodName):
                self.skipTest("skipped by user")
            else:
                f(self, *args, **kwargs)

        return wrapper

    return deco


class UnitTestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        logging.info("setUp")

    def tearDown(self):
        logging.info("tearDown")
