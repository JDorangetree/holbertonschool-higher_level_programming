#!/usr/bin/python3
""" Unittest for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testBase(unittest.TestCase):
    """Clase for unittest of super clase"""

    def setUp(self):
        """setup for all methods"""
        Base._Base__nb_objects = 0

    def test_is_instance(self):
        Base1 = Base()
        self.assertIsInstance(Base1, Base)

    def test_set_id(self):
        Base1 = Base(2)
        self.assertEqual(Base1.id, 2)

    def test_empty_instance(self):
        Base1 = Base()
        self.assertEqual(Base1.id, 1)

    def test_noneid(self):
        Base1 = Base(None)
        self.assertEqual(Base1.id, 1)

    def test_issubclase_Rectangle(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_issubclase_Square(self):
        self.assertTrue(issubclass(Square, Base))
