#!/usr/bin/python3
""" Unittest for rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare(unittest.TestCase):
    """"Clase for unittest of Square class"""

    def setUp(self):
        """setup for all methods"""
        Base._Base__nb_objects = 0

    def test_is_instance(self):
        Square1 = Square(1, 1)
        self.assertIsInstance(Square1, Square)

    def test_no_id(self):
        Square1 = Square(1, 1, 2, 2)
        self.assertTrue(Square1.id, 1)

    def test_no_y(self):
        Square1 = Square(1, 1)
        self.assertEqual(Square1.y, 0)

    def test_no_x(self):
        Square1 = Square(1)
        self.assertEqual(Square1.x, 0)

    def test_size(self):
        Square1 = Square(2, 3)
        self.assertEqual(Square1.size, 2)

    def test_area(self):
        Square1 = Square(2, 3)
        self.assertEqual(Square1.area(), 4)

    def test_update(self):
        Square1 = Square(2, 10)
        Square1.update(size=3)
        self.assertEqual(Square1.size, 3)
