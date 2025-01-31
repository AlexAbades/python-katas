import unittest

from katas.persistent_bugger.persistent_bugger import persistent, persistent_bugg, persistent_bugger_no_recursion

class TestPersistentBugger(unittest.TestCase):
    
    def test_test(self):
        self.assertTrue(True)
    
    def test_persistent_bugger_one_digit(self):
        self.assertEqual(persistent(5), 0)
        
    def test_persistent_bugger_two_digits(self):
        self.assertEqual(persistent(25), 2)
        self.assertEqual(persistent(39), 3)

    def test_persistent_bugg_one_digit(self):
        self.assertEqual(persistent_bugg(5),0)
    
    def test_persistent_bugg_two_digit(self):
        self.assertEqual(persistent_bugg(25),2)
        self.assertEqual(persistent_bugg(39),3)
        
    def test_persistent_bugger_no_recursion_one_digit(self):
        self.assertEqual(persistent_bugger_no_recursion(5),0)
    
    def test_persistent_bugger_no_recursion_two_digit(self):
        self.assertEqual(persistent_bugger_no_recursion(25),2)
        self.assertEqual(persistent_bugger_no_recursion(39),3)