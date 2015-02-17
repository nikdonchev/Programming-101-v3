__author__ = 'Nikolay Donchev'
import math


def fill_tetrahedron(num):
    """
    This function takes one argument that is the edge length
    of a Regular tetrahedron in centimeters and prints
    the amount of water that can be filled in liters.
    """
    volume = (num ** 3) / (6 * math.sqrt(2))
    return round((volume / 1000), 2)