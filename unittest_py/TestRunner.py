import os
from utils.log import get_logger
from utils.fileLog import Logs
import unittest
from unittest import TestLoader, TestSuite
import xmlrunner
from TestMainModule.UnitTestBase import TestList
from argparse import ArgumentParser
  
log_console = get_logger()
log_file = Logs("TestRunner_log.txt")
  

if __name__ == '__main__':
    log_console.info("TestRunner start")
    log_file.write("TestRunner start")
      
    #1. parse arguments  
    parser = ArgumentParser()
    parser.add_argument('-ts', '--testsuite', nargs='+', help="Test suite name (without extension)", default=['*'])
    parser.add_argument('-tc', '--testcase', nargs='+', help="Test case name", default=['*'])
    parsed_args = parser.parse_args()
      
    #2. add test suite & test case to be run
    testsuite = parsed_args.testsuite
    testcase = parsed_args.testcase
    log_console.info("testsuite:{}".format(testsuite))
    log_console.info("testcase:{}".format(testcase))

    for el in testsuite:
        TestList.add(test_suite=el)
        
    for el in testcase:
        TestList.add(test_case=el)
       
    #3. show tests to be run 
    TestList.print_list()
    

    test_loader = TestLoader()
    suite_list = [test_loader.discover('Tests', pattern='{}.py'.format(x)) for x in testsuite]
    #suite_list.skipTest("test_simple_test2")
    test_loader = TestLoader()
    suite = TestSuite(suite_list)
    #unittest.TextTestRunner(verbosity=2).run(suite) #without generating .xml output
    xmlrunner.XMLTestRunner(output='report.xml', verbosity=2).run(suite)
