from TestMainModule.UnitTestBase import Base_unit_test, your_skip_decorator

class TestA(Base_unit_test):
    @your_skip_decorator()
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @your_skip_decorator()
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())