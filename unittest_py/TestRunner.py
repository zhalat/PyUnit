import os
from utils.log import get_logger
from utils.fileLog import Logs
import unittest
from unittest import TestLoader, TestSuite
import xmlrunner
from argparse import ArgumentParser
  
log_console = get_logger()
log_file = Logs("TestRunner_log.txt")
  
# def set_tests_for_skipping(suite_set, test_names: list):
#     if hasattr(suite_set, '__iter__'):
#         for x in suite_set:
#             set_tests_for_skipping(x, test_names)
#     else:
#         if suite_set._testMethodName not in test_names:
#             setattr(suite_set, 'setUp', lambda: suite_set.skipTest('Test name to does not match to pattern'))
#             print('{} will be skip'.format(suite_set._testMethodName))
  
  
if __name__ == '__main__':
    log_console.info("TestRunner start")
    log_file.write("TestRunner start")
      
    parser = ArgumentParser()
    parser.add_argument('-ts', '--testsuite', nargs='+', help="Test suite name (without extension)", default=['*'])
    parser.add_argument('-tc', '--testcase', nargs='+', help="Test case name", default=['*'])
    parsed_args = parser.parse_args()
      
    #show selected sutie and test case
    testsuite = parsed_args.testsuite
    testcase = parsed_args.testcase
    log_console.info("testsuite:{}".format(testsuite))
    log_console.info("testcase:{}".format(testcase))
      
      
    #load only those tests which mets user requirements
    test_loader = TestLoader()
    #test_loader.testMethodPrefix = "test_simple_test2 "
    suite_list = [test_loader.discover('Tests', pattern='{}.py'.format(x)) for x in testsuite]
    #suite_list.skipTest("test_simple_test2")
    test_loader = TestLoader()
    suite = TestSuite(suite_list)
    #unittest.TextTestRunner(verbosity=2).run(suite) #without generating .xml output
    xmlrunner.XMLTestRunner(output='report.xml', verbosity=2).run(suite)

# # importing libraries 
# import time 
# import math 
#  
# # decorator to calculate duration 
# # taken by any function. 
# def calculate_time(func): 
#      
#     # added arguments inside the inner1, 
#     # if function takes any arguments, 
#     # can be added like this. 
#     def inner1(*args, **kwargs): 
#  
#         # storing time before function execution 
#         begin = time.time() 
#          
#         func(*args, **kwargs) 
#  
#         # storing time after function execution 
#         end = time.time() 
#         print("Total time taken in : ", func.__name__, end - begin) 
#  
#     return inner1 
#  
#  
#  
# # this can be added to any function present, 
# # in this case to calculate a factorial 
# @calculate_time
# def factorial(num): 
#  
#     # sleep 2 seconds because it takes very less time 
#     # so that you can see the actual difference 
#     time.sleep(2) 
#     print(math.factorial(num)) 
#  
# # calling the function. 
# factorial(10) 
