import unittest
class A:
    def sayHello(self):
        return 'Hello World'

class MyTest(unittest.TestCase):
  def test_something(self):
    a = A()
    my_dict = {"x": a}
    self.assertEqual(a, my_dict["x"])  # OK
    self.assertIs(a, "x")  # Noncompliant