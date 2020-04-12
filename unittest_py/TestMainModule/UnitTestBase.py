'''
Created on Apr 10, 2020

@author: zhalat
'''
import unittest

class TestSkipperList:
    skip_test_name_list = []
    
    @staticmethod
    def add(testCaseName):
        TestSkipperList.skip_test_name_list.append(testCaseName)

    @staticmethod
    def clean_skip_list(self):
        TestSkipperList.skip_test_name_list.clear()
        
    @staticmethod
    def is_on_the_list(testCaseName) -> bool: 
        retval = testCaseName in TestSkipperList.skip_test_name_list
        return retval
    
    @staticmethod
    def print_list():
        print(TestSkipperList.skip_test_name_list)

def your_skip_decorator(flag: bool):
    def deco(f):
        def wrapper(self, *args, **kwargs):
            if flag:
                self.skipTest("skipped by user")
            else:
                f(self, *args, **kwargs)
        return wrapper
    return deco

class Base_unit_test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


