import os
import logging
import unittest
import xmlrunner
from unittest import TestLoader, TestSuite
from argparse import ArgumentParser

import utils.logging_cfg
from utils.write2file import Write2File
from TestMainModule.UnitTestBase import TestList


if __name__ == '__main__':
    logging.info("TestRunner start")
       
    #1. parse arguments  
    parser = ArgumentParser()
    parser.add_argument('-ts', '--testsuite', nargs='+', help="Test suite name", default=['*'])
    parser.add_argument('-tc', '--testcase', nargs='+', help="Test case name", default=['*'])
    parsed_args = parser.parse_args()
       
    #2. add test suite & test case to be run
    testsuite = parsed_args.testsuite
    testcase = parsed_args.testcase
    logging.info("testsuite:{}".format(testsuite))
    logging.info("testcase:{}".format(testcase))
     
#     for el in testsuite:
#         TestList.add(test_suite=el)
#         
#     for el in testcase:
#         TestList.add(test_case=el)
#        
#     #3. show tests to be run 
#     TestList.validate_list()
#     
#     #4. run test 
#     test_loader = TestLoader()
#     suite_list = [test_loader.discover('Tests', pattern='{}.py'.format(x)) for x in testsuite]
#     test_loader = TestLoader()
#     suite = TestSuite(suite_list)
#     xmlrunner.XMLTestRunner(output='report.xml', verbosity=2).run(suite)
#     #without generating .xml output
#     #unittest.TextTestRunner(verbosity=2).run(suite) 
#     
#     log_console.info("TestRunner end")
#     log_file.write("TestRunner end")

