# PyUnit framework skeleton

### What for

PyUnit framework skeleton allows you quick starting with python unit tests.
It contains simple exemplary test suites with test cases.
Each of test cases have decorator which is used for selective chose test cases to be run.

Framework works on the base of classical scheme:

- test suites - container for test cases
- test cases - where you write your unit tests
- setUp()  - method runs before each test case. 
- tearDown() - method runs after each test case

It would be best convenient  for you to just playing around whit code as it is for a while before you made a decision to make changes

### Install required packages

```
pip3 install -r requirements.txt
```
You should have python 3 installed

### Arguments description

```
'-ts',     '--testsuite', help="Test suite name (without extension)", default=['*']
'-tc',     '--testcase',  help="Test case name", default=['*']
```

### How to run tests?

Following diagram show tests structure.

```
unittest_py/Tests
                └── TestA.py
                    ├──test_upper
                    └──test_isupper
                └── TestB.py
                    ├──test_sum
                    ├──test_diff
                    └──test_windows_support
                └── TestC.py
                    ├──test_simple_test1
                    ├──test_simple_test2
                    └──test_simple_test3
```
TestA, TestB, TestC are test suite.  Each of them has its own test cases.
The framework do no require all parameters.  By default all test suites and all test cases will be run. 
You can decide which test should be run. See some example:

- I want to run all

  ```python
  python3 TestRunner.py 
  ```

  >   test_isupper (Tests.TestA.TestA) ... ok (0.010s)
  >   test_upper (Tests.TestA.TestA) ... ok (0.001s)
  >   test_diff (Tests.TestB.TestB) ... ok (0.001s)
  >   test_sum (Tests.TestB.TestB) ... ok (0.001s)
  >   test_simple_test1 (Tests.TestC.TestC) ... ok (0.001s)
  >   test_simple_test2 (Tests.TestC.TestC) ... ok (0.001s)
  >   test_simple_test3 (Tests.TestC.TestC) ... ok (0.001s)

- I want to run suites: 
  *TestA*  with *all* test cases
  *TestB*  with *all* test cases

  ```python
  python3 TestRunner.py -ts TestA TestB
  ```

  >   test_isupper (Tests.TestA.TestA) ... ok (0.007s)
  >   test_upper (Tests.TestA.TestA) ... ok (0.001s)
  >   test_diff (Tests.TestB.TestB) ... ok (0.000s)
  >   test_sum (Tests.TestB.TestB) ... ok (0.000s)

- I want to run suites: 
  *TestA* with test case [*test_isupper*]
  *TestB* with [*test_simple_test1*, *test_simple_test3*]

  ```python
  python3 TestRunner.py -ts TestA TestC -tc test_isupper test_simple_test1 test_simple_test3
  ```

  >   test_isupper (Tests.TestA.TestA) ... ok (0.006s)
  >   test_upper (Tests.TestA.TestA) ... skip (0.001s)
  >   test_simple_test1 (Tests.TestC.TestC) ... ok (0.001s)
  >   test_simple_test2 (Tests.TestC.TestC) ... skip (0.001s)
  >   test_simple_test3 (Tests.TestC.TestC) ... ok (0.001s)

### Adding test to suite
1. Create new file in 'Tests' directory. 
2. Add to the new file tests.
- The test class need to derive from UnitTestBase to get all required utils.
- Each test procedure need start from 'test_' prefix.
- The framework runs setUp/tearDown before/after each  suite


