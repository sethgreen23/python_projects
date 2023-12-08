#!/usr/bin/python3
"""
Testing module for the calsses Base , Rectangles
In this module we will test all the available Functionalities
and Comme up with adequate testes
"""
import unittest
from models.base import Base


class TestBaseIdValidValues(unittest.TestCase):
    """
    TestBaseIdValidValues is a class that test
    id valid values and make sure that we get
    good information out of it
    """

    def test_id_two_classes(self):
        """
        test the output of two classes indexes
        """

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_three_classes(self):
        """
        test the output of three classes
        """

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_provided(self):
        """
        test with provided id in
        the object creation
        """

        b1 = Base(12)
        b2 = Base(-12)
        b3 = Base(-15)
        b4 = Base()
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, -12)
        self.assertEqual(b3.id, -15)
        self.assertEqual(b4.id, 1)



if __name__ == '__main__':
    unittest.main()
