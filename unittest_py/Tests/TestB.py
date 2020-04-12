from TestMainModule.UnitTestBase import Base_unit_test, your_skip_decorator
import unittest
import sys

class TestB(Base_unit_test):
    @your_skip_decorator()
    def test_sum(self):
        self.assertEqual(2+4, 6)

    @your_skip_decorator()
    def test_diff(self):
        self.assertTrue(4, 4)
        self.assertFalse(False, True)
            
#     @your_skip_decorator()
#     def test_windows_support(self):
#         self.fail("shouldn't happen")
#         pass