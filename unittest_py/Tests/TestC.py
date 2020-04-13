from TestMainModule.UnitTestBase import UnitTestBase, your_skip_decorator

class TestC(UnitTestBase):
    @your_skip_decorator()
    def test_simple_test1(self):
        self.assertFalse(False, False)

    @your_skip_decorator()
    def test_simple_test2(self):
        self.assertTrue(True, True)
    
    @your_skip_decorator()
    def test_simple_test3(self):
        self.assertTrue(True, True)
