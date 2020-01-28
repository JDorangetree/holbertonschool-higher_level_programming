#!/usr/bin/python3
""" Unittest for rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testRectangle(unittest.TestCase):
    """"Clase for unittest of Rectangle class"""

    def setUp(self):
        """setup for all methods"""
        Base._Base__nb_objects = 0

    def test_is_instance(self):
        Rectangle1 = Rectangle(1, 1)
        self.assertIsInstance(Rectangle1, Rectangle)

    def test_no_id(self):
        Rectangle1 = Rectangle(1, 1, 2, 2)
        self.assertTrue(Rectangle1.id, 1)

    def test_no_x(self):
        Rectangle1 = Rectangle(1, 1)
        self.assertEqual(Rectangle1.x, 0)

    def test_no_y(self):
        Rectangle1 = Rectangle(1, 1)
        self.assertEqual(Rectangle1.y, 0)

    def test_heigt(self):
        Rectangle1 = Rectangle(2, 3)
        self.assertEqual(Rectangle1.height, 3)

    def test_width(self):
        Rectangle1 = Rectangle(2, 3)
        self.assertEqual(Rectangle1.width, 2)

    def test_area(self):
        Rectangle1 = Rectangle(2, 3)
        self.assertEqual(Rectangle1.area(), 6)

    def test_update(self):
        Rectangle1 = Rectangle(2, 3)
        Rectangle1.update(3)
        self.assertEqual(Rectangle1.id, 3)
