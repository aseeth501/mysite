#testing

#unit testing:
'''
==>The process of testing whether perticular unit is working
properly or not is called unittesting, means individual component testing
==>Developer is responsible for unit testing'''


#integration testing

'''
==>integration means end to end testing, means total functionality testing
==>The process of testing total application(end-to-end)
==> QA team is responsible for integration testing'''

#How to perform unittesting in python:
'''
I)module name: unittest
II)class name : TestCase
III)instance methods: 3 methods

1.setUp() method
2.test() method
3.tearDown() method

Note:
==> first and third methods names are fixed we dont change the method names.
==> But we can change the second methos name that is test()  method with one
condition, that is prefix name must 'test' than u can write any thing.

ex:test1() or test_method1() any thing u take but prifix must 'test'.    

==> Here setUp() and tearDown() execute for every test case.


IV)classmethods: 2

1.setUpClass(cls)
2.tearDownClass(cls)

NOte:
==> Here setUpClass() and tearDownClass() execute only once for common testcase
functionality.

'''

#ex1:
'''import unittest

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("setUp method execution...")
        
    def test_method(self):
        print("test method execution...")

    def test2(self):
        print("2nd test case")

    def tearDown(self):
        print("tearDown method execution...")

unittest.main()'''

'''import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass method execution...")
    
    def setUp(self):
        print("setUp method execution...")
        
    def test_method1(self):
        print("test_method1 execution...")

    def test_method2(self):
        print("test_method2 execution...")

    def tearDown(self):
        print("tearDown method execution...")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass method execution...")


unittest.main()'''

#ex6:print the value of key 'd21' in nested dictionary:

'''dict={'a':1,'b':3,'c':56,'d':{'d1':11,"d2":{'d21':221},'d3':33},'e':56}
print(dict['d']['d2']['d21'])'''


#ex10:

#s = "s1r2i3n45i6v7a89s$"
import re
#matcher=re.finditer("/W","s1r2i3n45i6v7a89s$")
#for match in matcher:
#    print(match.start(),"......",match.group())


b =re.findall("\w","s1r2i3n45i6v7a89s$") 
#print(b)
for char in b:
    d = ''.join(char)
    print(d,end="")


















        
