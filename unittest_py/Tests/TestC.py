from TestMainModule.UnitTestBase import Base_unit_test, your_skip_decorator

class TestC(Base_unit_test):
    @your_skip_decorator(True)
    def test_simple_test1(self):
        self.assertFalse(False, False)

    @your_skip_decorator(False)
    def test_simple_test2(self):
        self.assertTrue(True, True)
    
    @your_skip_decorator(True)
    def test_simple_test3(self):
        self.assertTrue(True, True)

