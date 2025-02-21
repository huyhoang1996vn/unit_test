import unittest

def add(x, y):
    return x+y

class TestFunction(unittest.TestCase):
    def setUp(self):
        # method that runs before each test.
        self.message = 'Message wrong'

    def test_add(self):
        print("=======d")
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(1,2), 32, self.message)


print("===__name__", __name__)
if __name__ == "__main__":
    unittest.main()

'''
Explanation of __name__ and "__main__"
__name__: A special built-in variable in Python that represents the name of the module.
"__main__": When a script is run directly, 
            Python sets the __name__ variable to 
"__main__": If the script is imported as a module in another script, 
            __name__ will instead be set to the module's name.
'''

