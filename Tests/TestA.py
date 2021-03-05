import sys
import os
from TestMainModule.UnitTestBase import UnitTestBase, skip_decorator
import logging

class TestA(UnitTestBase):
    def setUp(self):
        super().setUp()
        logging.info("Initialize testA")


    @skip_decorator()
    def test_A(self):
        status = True
        self.assertEqual(status, True)


