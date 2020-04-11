import os
from utils.log import get_logger
from utils.fileLog import Logs
import unittest
from unittest import TestLoader, TestSuite
import xmlrunner
from argparse import ArgumentParser

log_console = get_logger()
log_file = Logs("TestRunner_log.txt")

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
   # test_loader.testMethodPrefix = "test_diff"
    suite_list = [test_loader.discover('Tests', pattern='{}.py'.format(x)) for x in testsuite]
    test_loader = TestLoader()
    suite = TestSuite(suite_list)
    #unittest.TextTestRunner(verbosity=2).run(suite) #without generating .xml output
    xmlrunner.XMLTestRunner(output='report.xml', verbosity=2).run(suite)