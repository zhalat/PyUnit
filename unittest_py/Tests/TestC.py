from TestMainModule.UnitTestBase import Base_unit_test

class TestC(Base_unit_test):
    def test_simple_test1(self):
        self.assertFalse(False, False)

    def test_simple_test2(self):
        self.assertTrue(True, True)
