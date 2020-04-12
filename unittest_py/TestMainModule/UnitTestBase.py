'''
Created on Apr 10, 2020

@author: zhalat
'''
import unittest

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


