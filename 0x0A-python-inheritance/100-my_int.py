#!/usr/bin/python3

""" Class that inherits from int """


class MyInt(int):
    """Class hass == and != operators inverted"""
    def __eq__(self, other):
        """equality operator behavior"""
        return super().__ne__(other)

    def __ne__(self, other):
        """operator behavior no equality"""
        return super().__eq__(other)
