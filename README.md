# skelethon PyUnit framework

### Install required packages
```
pip3 install -r requirements.txt
```
### How to run tests?
```
python3 TestRunner.py [args]
```
### Arguments description
```
to be defined
```
The framework do no require all parameters. If you want to test only nxp side ( with tc parameter)
and you don't want to connect to server, you need to omit stream_id and password. 

IMPORTANT! If you run test which uses disabled unit, the test will fail!

### Adding test to suite
1. Create new file in 'Tests' directory. 
2. Add to the new file tests.
- The test class need to derive from UnitTestBase to get all required utils.
- Each test procedure need start from 'test_' prefix.
- The framework runs setUp/tearDown before/after each  suite


