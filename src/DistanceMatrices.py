
__author__ = 'mohr'

from collections import OrderedDict

"""
Distance matrices for distances between amino acids derived from different BLOSUM matrices
"""

BLOSUM45_distances = OrderedDict([('A', OrderedDict(
    [('A', '0.5'), ('R', '0.85'), ('N', '0.8'), ('D', '0.85'), ('C', '0.8'), ('Q', '0.8'), ('E', '0.8'), ('G', '0.75'),
     ('H', '0.85'), ('I', '0.8'), ('L', '0.8'), ('K', '0.8'), ('M', '0.8'), ('F', '0.85'), ('P', '0.8'), ('S', '0.7'),
     ('T', '0.75'), ('W', '0.85'), ('Y', '0.85'), ('V', '0.75')])), ('R', OrderedDict(
    [('A', '0.85'), ('R', '0.4'), ('N', '0.75'), ('D', '0.8'), ('C', '0.9'), ('Q', '0.7'), ('E', '0.75'), ('G', '0.85'),
     ('H', '0.75'), ('I', '0.9'), ('L', '0.85'), ('K', '0.6'), ('M', '0.8'), ('F', '0.85'), ('P', '0.85'), ('S', '0.8'),
     ('T', '0.8'), ('W', '0.85'), ('Y', '0.8'), ('V', '0.85')])), ('N', OrderedDict(
    [('A', '0.8'), ('R', '0.75'), ('N', '0.45'), ('D', '0.65'), ('C', '0.85'), ('Q', '0.75'), ('E', '0.75'),
     ('G', '0.75'), ('H', '0.7'), ('I', '0.85'), ('L', '0.9'), ('K', '0.75'), ('M', '0.85'), ('F', '0.85'),
     ('P', '0.85'), ('S', '0.7'), ('T', '0.75'), ('W', '0.95'), ('Y', '0.85'), ('V', '0.9')])), ('D', OrderedDict(
    [('A', '0.85'), ('R', '0.8'), ('N', '0.65'), ('D', '0.4'), ('C', '0.9'), ('Q', '0.75'), ('E', '0.65'), ('G', '0.8'),
     ('H', '0.75'), ('I', '0.95'), ('L', '0.9'), ('K', '0.75'), ('M', '0.9'), ('F', '0.95'), ('P', '0.8'),
     ('S', '0.75'), ('T', '0.8'), ('W', '0.95'), ('Y', '0.85'), ('V', '0.9')])), ('C', OrderedDict(
    [('A', '0.8'), ('R', '0.9'), ('N', '0.85'), ('D', '0.9'), ('C', '0.15'), ('Q', '0.9'), ('E', '0.9'), ('G', '0.9'),
     ('H', '0.9'), ('I', '0.9'), ('L', '0.85'), ('K', '0.9'), ('M', '0.85'), ('F', '0.85'), ('P', '0.95'), ('S', '0.8'),
     ('T', '0.8'), ('W', '1.0'), ('Y', '0.9'), ('V', '0.8')])), ('Q', OrderedDict(
    [('A', '0.8'), ('R', '0.7'), ('N', '0.75'), ('D', '0.75'), ('C', '0.9'), ('Q', '0.45'), ('E', '0.65'),
     ('G', '0.85'), ('H', '0.7'), ('I', '0.85'), ('L', '0.85'), ('K', '0.7'), ('M', '0.75'), ('F', '0.95'),
     ('P', '0.8'), ('S', '0.75'), ('T', '0.8'), ('W', '0.85'), ('Y', '0.8'), ('V', '0.9')])), ('E', OrderedDict(
    [('A', '0.8'), ('R', '0.75'), ('N', '0.75'), ('D', '0.65'), ('C', '0.9'), ('Q', '0.65'), ('E', '0.45'),
     ('G', '0.85'), ('H', '0.75'), ('I', '0.9'), ('L', '0.85'), ('K', '0.7'), ('M', '0.85'), ('F', '0.9'),
     ('P', '0.75'), ('S', '0.75'), ('T', '0.8'), ('W', '0.9'), ('Y', '0.85'), ('V', '0.9')])), ('G', OrderedDict(
    [('A', '0.75'), ('R', '0.85'), ('N', '0.75'), ('D', '0.8'), ('C', '0.9'), ('Q', '0.85'), ('E', '0.85'),
     ('G', '0.4'), ('H', '0.85'), ('I', '0.95'), ('L', '0.9'), ('K', '0.85'), ('M', '0.85'), ('F', '0.9'),
     ('P', '0.85'), ('S', '0.75'), ('T', '0.85'), ('W', '0.85'), ('Y', '0.9'), ('V', '0.9')])), ('H', OrderedDict(
    [('A', '0.85'), ('R', '0.75'), ('N', '0.7'), ('D', '0.75'), ('C', '0.9'), ('Q', '0.7'), ('E', '0.75'),
     ('G', '0.85'), ('H', '0.25'), ('I', '0.9'), ('L', '0.85'), ('K', '0.8'), ('M', '0.75'), ('F', '0.85'),
     ('P', '0.85'), ('S', '0.8'), ('T', '0.85'), ('W', '0.9'), ('Y', '0.65'), ('V', '0.9')])), ('I', OrderedDict(
    [('A', '0.8'), ('R', '0.9'), ('N', '0.85'), ('D', '0.95'), ('C', '0.9'), ('Q', '0.85'), ('E', '0.9'), ('G', '0.95'),
     ('H', '0.9'), ('I', '0.5'), ('L', '0.65'), ('K', '0.9'), ('M', '0.65'), ('F', '0.75'), ('P', '0.85'),
     ('S', '0.85'), ('T', '0.8'), ('W', '0.85'), ('Y', '0.75'), ('V', '0.6')])), ('L', OrderedDict(
    [('A', '0.8'), ('R', '0.85'), ('N', '0.9'), ('D', '0.9'), ('C', '0.85'), ('Q', '0.85'), ('E', '0.85'), ('G', '0.9'),
     ('H', '0.85'), ('I', '0.65'), ('L', '0.5'), ('K', '0.9'), ('M', '0.65'), ('F', '0.7'), ('P', '0.9'), ('S', '0.9'),
     ('T', '0.8'), ('W', '0.85'), ('Y', '0.75'), ('V', '0.7')])), ('K', OrderedDict(
    [('A', '0.8'), ('R', '0.6'), ('N', '0.75'), ('D', '0.75'), ('C', '0.9'), ('Q', '0.7'), ('E', '0.7'), ('G', '0.85'),
     ('H', '0.8'), ('I', '0.9'), ('L', '0.9'), ('K', '0.5'), ('M', '0.8'), ('F', '0.9'), ('P', '0.8'), ('S', '0.8'),
     ('T', '0.8'), ('W', '0.85'), ('Y', '0.8'), ('V', '0.85')])), ('M', OrderedDict(
    [('A', '0.8'), ('R', '0.8'), ('N', '0.85'), ('D', '0.9'), ('C', '0.85'), ('Q', '0.75'), ('E', '0.85'),
     ('G', '0.85'), ('H', '0.75'), ('I', '0.65'), ('L', '0.65'), ('K', '0.8'), ('M', '0.45'), ('F', '0.75'),
     ('P', '0.85'), ('S', '0.85'), ('T', '0.8'), ('W', '0.85'), ('Y', '0.75'), ('V', '0.7')])), ('F', OrderedDict(
    [('A', '0.85'), ('R', '0.85'), ('N', '0.85'), ('D', '0.95'), ('C', '0.85'), ('Q', '0.95'), ('E', '0.9'),
     ('G', '0.9'), ('H', '0.85'), ('I', '0.75'), ('L', '0.7'), ('K', '0.9'), ('M', '0.75'), ('F', '0.35'), ('P', '0.9'),
     ('S', '0.85'), ('T', '0.8'), ('W', '0.7'), ('Y', '0.6'), ('V', '0.75')])), ('P', OrderedDict(
    [('A', '0.8'), ('R', '0.85'), ('N', '0.85'), ('D', '0.8'), ('C', '0.95'), ('Q', '0.8'), ('E', '0.75'),
     ('G', '0.85'), ('H', '0.85'), ('I', '0.85'), ('L', '0.9'), ('K', '0.8'), ('M', '0.85'), ('F', '0.9'), ('P', '0.3'),
     ('S', '0.8'), ('T', '0.8'), ('W', '0.9'), ('Y', '0.9'), ('V', '0.9')])), ('S', OrderedDict(
    [('A', '0.7'), ('R', '0.8'), ('N', '0.7'), ('D', '0.75'), ('C', '0.8'), ('Q', '0.75'), ('E', '0.75'), ('G', '0.75'),
     ('H', '0.8'), ('I', '0.85'), ('L', '0.9'), ('K', '0.8'), ('M', '0.85'), ('F', '0.85'), ('P', '0.8'), ('S', '0.55'),
     ('T', '0.65'), ('W', '0.95'), ('Y', '0.85'), ('V', '0.8')])), ('T', OrderedDict(
    [('A', '0.75'), ('R', '0.8'), ('N', '0.75'), ('D', '0.8'), ('C', '0.8'), ('Q', '0.8'), ('E', '0.8'), ('G', '0.85'),
     ('H', '0.85'), ('I', '0.8'), ('L', '0.8'), ('K', '0.8'), ('M', '0.8'), ('F', '0.8'), ('P', '0.8'), ('S', '0.65'),
     ('T', '0.5'), ('W', '0.9'), ('Y', '0.8'), ('V', '0.75')])), ('W', OrderedDict(
    [('A', '0.85'), ('R', '0.85'), ('N', '0.95'), ('D', '0.95'), ('C', '1.0'), ('Q', '0.85'), ('E', '0.9'),
     ('G', '0.85'), ('H', '0.9'), ('I', '0.85'), ('L', '0.85'), ('K', '0.85'), ('M', '0.85'), ('F', '0.7'),
     ('P', '0.9'), ('S', '0.95'), ('T', '0.9'), ('W', '0.0'), ('Y', '0.6'), ('V', '0.9')])), ('Y', OrderedDict(
    [('A', '0.85'), ('R', '0.8'), ('N', '0.85'), ('D', '0.85'), ('C', '0.9'), ('Q', '0.8'), ('E', '0.85'), ('G', '0.9'),
     ('H', '0.65'), ('I', '0.75'), ('L', '0.75'), ('K', '0.8'), ('M', '0.75'), ('F', '0.6'), ('P', '0.9'),
     ('S', '0.85'), ('T', '0.8'), ('W', '0.6'), ('Y', '0.35'), ('V', '0.8')])), ('V', OrderedDict(
    [('A', '0.75'), ('R', '0.85'), ('N', '0.9'), ('D', '0.9'), ('C', '0.8'), ('Q', '0.9'), ('E', '0.9'), ('G', '0.9'),
     ('H', '0.9'), ('I', '0.6'), ('L', '0.7'), ('K', '0.85'), ('M', '0.7'), ('F', '0.75'), ('P', '0.9'), ('S', '0.8'),
     ('T', '0.75'), ('W', '0.9'), ('Y', '0.8'), ('V', '0.5')]))])

BLOSUM50_distances = OrderedDict([('A', OrderedDict(
    [('A', '0.5'), ('R', '0.85'), ('N', '0.8'), ('D', '0.85'), ('C', '0.8'), ('Q', '0.8'), ('E', '0.8'), ('G', '0.75'),
     ('H', '0.85'), ('I', '0.8'), ('L', '0.85'), ('K', '0.8'), ('M', '0.8'), ('F', '0.9'), ('P', '0.8'), ('S', '0.7'),
     ('T', '0.75'), ('W', '0.9'), ('Y', '0.85'), ('V', '0.75')])), ('R', OrderedDict(
    [('A', '0.85'), ('R', '0.4'), ('N', '0.8'), ('D', '0.85'), ('C', '0.95'), ('Q', '0.7'), ('E', '0.75'), ('G', '0.9'),
     ('H', '0.75'), ('I', '0.95'), ('L', '0.9'), ('K', '0.6'), ('M', '0.85'), ('F', '0.9'), ('P', '0.9'), ('S', '0.8'),
     ('T', '0.8'), ('W', '0.9'), ('Y', '0.8'), ('V', '0.9')])), ('N', OrderedDict(
    [('A', '0.8'), ('R', '0.8'), ('N', '0.4'), ('D', '0.65'), ('C', '0.85'), ('Q', '0.75'), ('E', '0.75'),
     ('G', '0.75'), ('H', '0.7'), ('I', '0.9'), ('L', '0.95'), ('K', '0.75'), ('M', '0.85'), ('F', '0.95'),
     ('P', '0.85'), ('S', '0.7'), ('T', '0.75'), ('W', '0.95'), ('Y', '0.85'), ('V', '0.9')])), ('D', OrderedDict(
    [('A', '0.85'), ('R', '0.85'), ('N', '0.65'), ('D', '0.35'), ('C', '0.95'), ('Q', '0.75'), ('E', '0.65'),
     ('G', '0.8'), ('H', '0.8'), ('I', '0.95'), ('L', '0.95'), ('K', '0.8'), ('M', '0.95'), ('F', '1.0'), ('P', '0.8'),
     ('S', '0.75'), ('T', '0.8'), ('W', '1.0'), ('Y', '0.9'), ('V', '0.95')])), ('C', OrderedDict(
    [('A', '0.8'), ('R', '0.95'), ('N', '0.85'), ('D', '0.95'), ('C', '0.1'), ('Q', '0.9'), ('E', '0.9'), ('G', '0.9'),
     ('H', '0.9'), ('I', '0.85'), ('L', '0.85'), ('K', '0.9'), ('M', '0.85'), ('F', '0.85'), ('P', '0.95'),
     ('S', '0.8'), ('T', '0.8'), ('W', '1.0'), ('Y', '0.9'), ('V', '0.8')])), ('Q', OrderedDict(
    [('A', '0.8'), ('R', '0.7'), ('N', '0.75'), ('D', '0.75'), ('C', '0.9'), ('Q', '0.4'), ('E', '0.65'), ('G', '0.85'),
     ('H', '0.7'), ('I', '0.9'), ('L', '0.85'), ('K', '0.65'), ('M', '0.75'), ('F', '0.95'), ('P', '0.8'),
     ('S', '0.75'), ('T', '0.8'), ('W', '0.8'), ('Y', '0.8'), ('V', '0.9')])), ('E', OrderedDict(
    [('A', '0.8'), ('R', '0.75'), ('N', '0.75'), ('D', '0.65'), ('C', '0.9'), ('Q', '0.65'), ('E', '0.45'),
     ('G', '0.9'), ('H', '0.75'), ('I', '0.95'), ('L', '0.9'), ('K', '0.7'), ('M', '0.85'), ('F', '0.9'), ('P', '0.8'),
     ('S', '0.8'), ('T', '0.8'), ('W', '0.9'), ('Y', '0.85'), ('V', '0.9')])), ('G', OrderedDict(
    [('A', '0.75'), ('R', '0.9'), ('N', '0.75'), ('D', '0.8'), ('C', '0.9'), ('Q', '0.85'), ('E', '0.9'), ('G', '0.35'),
     ('H', '0.85'), ('I', '0.95'), ('L', '0.95'), ('K', '0.85'), ('M', '0.9'), ('F', '0.95'), ('P', '0.85'),
     ('S', '0.75'), ('T', '0.85'), ('W', '0.9'), ('Y', '0.9'), ('V', '0.95')])), ('H', OrderedDict(
    [('A', '0.85'), ('R', '0.75'), ('N', '0.7'), ('D', '0.8'), ('C', '0.9'), ('Q', '0.7'), ('E', '0.75'), ('G', '0.85'),
     ('H', '0.25'), ('I', '0.95'), ('L', '0.9'), ('K', '0.75'), ('M', '0.8'), ('F', '0.8'), ('P', '0.85'), ('S', '0.8'),
     ('T', '0.85'), ('W', '0.9'), ('Y', '0.65'), ('V', '0.95')])), ('I', OrderedDict(
    [('A', '0.8'), ('R', '0.95'), ('N', '0.9'), ('D', '0.95'), ('C', '0.85'), ('Q', '0.9'), ('E', '0.95'),
     ('G', '0.95'), ('H', '0.95'), ('I', '0.5'), ('L', '0.65'), ('K', '0.9'), ('M', '0.65'), ('F', '0.75'),
     ('P', '0.9'), ('S', '0.9'), ('T', '0.8'), ('W', '0.9'), ('Y', '0.8'), ('V', '0.55')])), ('L', OrderedDict(
    [('A', '0.85'), ('R', '0.9'), ('N', '0.95'), ('D', '0.95'), ('C', '0.85'), ('Q', '0.85'), ('E', '0.9'),
     ('G', '0.95'), ('H', '0.9'), ('I', '0.65'), ('L', '0.5'), ('K', '0.9'), ('M', '0.6'), ('F', '0.7'), ('P', '0.95'),
     ('S', '0.9'), ('T', '0.8'), ('W', '0.85'), ('Y', '0.8'), ('V', '0.7')])), ('K', OrderedDict(
    [('A', '0.8'), ('R', '0.6'), ('N', '0.75'), ('D', '0.8'), ('C', '0.9'), ('Q', '0.65'), ('E', '0.7'), ('G', '0.85'),
     ('H', '0.75'), ('I', '0.9'), ('L', '0.9'), ('K', '0.45'), ('M', '0.85'), ('F', '0.95'), ('P', '0.8'),
     ('S', '0.75'), ('T', '0.8'), ('W', '0.9'), ('Y', '0.85'), ('V', '0.9')])), ('M', OrderedDict(
    [('A', '0.8'), ('R', '0.85'), ('N', '0.85'), ('D', '0.95'), ('C', '0.85'), ('Q', '0.75'), ('E', '0.85'),
     ('G', '0.9'), ('H', '0.8'), ('I', '0.65'), ('L', '0.6'), ('K', '0.85'), ('M', '0.4'), ('F', '0.75'), ('P', '0.9'),
     ('S', '0.85'), ('T', '0.8'), ('W', '0.8'), ('Y', '0.75'), ('V', '0.7')])), ('F', OrderedDict(
    [('A', '0.9'), ('R', '0.9'), ('N', '0.95'), ('D', '1.0'), ('C', '0.85'), ('Q', '0.95'), ('E', '0.9'), ('G', '0.95'),
     ('H', '0.8'), ('I', '0.75'), ('L', '0.7'), ('K', '0.95'), ('M', '0.75'), ('F', '0.35'), ('P', '0.95'),
     ('S', '0.9'), ('T', '0.85'), ('W', '0.7'), ('Y', '0.55'), ('V', '0.8')])), ('P', OrderedDict(
    [('A', '0.8'), ('R', '0.9'), ('N', '0.85'), ('D', '0.8'), ('C', '0.95'), ('Q', '0.8'), ('E', '0.8'), ('G', '0.85'),
     ('H', '0.85'), ('I', '0.9'), ('L', '0.95'), ('K', '0.8'), ('M', '0.9'), ('F', '0.95'), ('P', '0.25'), ('S', '0.8'),
     ('T', '0.8'), ('W', '0.95'), ('Y', '0.9'), ('V', '0.9')])), ('S', OrderedDict(
    [('A', '0.7'), ('R', '0.8'), ('N', '0.7'), ('D', '0.75'), ('C', '0.8'), ('Q', '0.75'), ('E', '0.8'), ('G', '0.75'),
     ('H', '0.8'), ('I', '0.9'), ('L', '0.9'), ('K', '0.75'), ('M', '0.85'), ('F', '0.9'), ('P', '0.8'), ('S', '0.5'),
     ('T', '0.65'), ('W', '0.95'), ('Y', '0.85'), ('V', '0.85')])), ('T', OrderedDict(
    [('A', '0.75'), ('R', '0.8'), ('N', '0.75'), ('D', '0.8'), ('C', '0.8'), ('Q', '0.8'), ('E', '0.8'), ('G', '0.85'),
     ('H', '0.85'), ('I', '0.8'), ('L', '0.8'), ('K', '0.8'), ('M', '0.8'), ('F', '0.85'), ('P', '0.8'), ('S', '0.65'),
     ('T', '0.5'), ('W', '0.9'), ('Y', '0.85'), ('V', '0.75')])), ('W', OrderedDict(
    [('A', '0.9'), ('R', '0.9'), ('N', '0.95'), ('D', '1.0'), ('C', '1.0'), ('Q', '0.8'), ('E', '0.9'), ('G', '0.9'),
     ('H', '0.9'), ('I', '0.9'), ('L', '0.85'), ('K', '0.9'), ('M', '0.8'), ('F', '0.7'), ('P', '0.95'), ('S', '0.95'),
     ('T', '0.9'), ('W', '0.0'), ('Y', '0.65'), ('V', '0.9')])), ('Y', OrderedDict(
    [('A', '0.85'), ('R', '0.8'), ('N', '0.85'), ('D', '0.9'), ('C', '0.9'), ('Q', '0.8'), ('E', '0.85'), ('G', '0.9'),
     ('H', '0.65'), ('I', '0.8'), ('L', '0.8'), ('K', '0.85'), ('M', '0.75'), ('F', '0.55'), ('P', '0.9'),
     ('S', '0.85'), ('T', '0.85'), ('W', '0.65'), ('Y', '0.35'), ('V', '0.8')])), ('V', OrderedDict(
    [('A', '0.75'), ('R', '0.9'), ('N', '0.9'), ('D', '0.95'), ('C', '0.8'), ('Q', '0.9'), ('E', '0.9'), ('G', '0.95'),
     ('H', '0.95'), ('I', '0.55'), ('L', '0.7'), ('K', '0.9'), ('M', '0.7'), ('F', '0.8'), ('P', '0.9'), ('S', '0.85'),
     ('T', '0.75'), ('W', '0.9'), ('Y', '0.8'), ('V', '0.5')]))])

BLOSUM90_distances = OrderedDict([('A', OrderedDict(
    [('A', '0.55'), ('R', '0.89'), ('N', '0.89'), ('D', '0.88'), ('C', '0.9'), ('Q', '0.9'), ('E', '0.9'),
     ('G', '0.91'), ('H', '0.89'), ('I', '0.89'), ('L', '0.89'), ('K', '0.9'), ('M', '0.89'), ('F', '0.88'),
     ('P', '0.9'), ('S', '0.92'), ('T', '0.91'), ('W', '0.88'), ('Y', '0.88'), ('V', '0.9')])), ('R', OrderedDict(
    [('A', '0.89'), ('R', '0.45'), ('N', '0.9'), ('D', '0.88'), ('C', '0.87'), ('Q', '0.92'), ('E', '0.9'),
     ('G', '0.88'), ('H', '0.91'), ('I', '0.88'), ('L', '0.88'), ('K', '0.93'), ('M', '0.89'), ('F', '0.88'),
     ('P', '0.88'), ('S', '0.9'), ('T', '0.89'), ('W', '0.88'), ('Y', '0.88'), ('V', '0.88')])), ('N', OrderedDict(
    [('A', '0.89'), ('R', '0.9'), ('N', '0.36'), ('D', '0.92'), ('C', '0.88'), ('Q', '0.91'), ('E', '0.9'),
     ('G', '0.9'), ('H', '0.91'), ('I', '0.88'), ('L', '0.88'), ('K', '0.91'), ('M', '0.88'), ('F', '0.88'),
     ('P', '0.88'), ('S', '0.91'), ('T', '0.91'), ('W', '0.87'), ('Y', '0.88'), ('V', '0.88')])), ('D', OrderedDict(
    [('A', '0.88'), ('R', '0.88'), ('N', '0.92'), ('D', '0.36'), ('C', '0.87'), ('Q', '0.9'), ('E', '0.92'),
     ('G', '0.89'), ('H', '0.89'), ('I', '0.87'), ('L', '0.87'), ('K', '0.9'), ('M', '0.88'), ('F', '0.87'),
     ('P', '0.88'), ('S', '0.9'), ('T', '0.89'), ('W', '0.86'), ('Y', '0.88'), ('V', '0.87')])), ('C', OrderedDict(
    [('A', '0.9'), ('R', '0.87'), ('N', '0.88'), ('D', '0.87'), ('C', '0.18'), ('Q', '0.88'), ('E', '0.86'),
     ('G', '0.88'), ('H', '0.87'), ('I', '0.89'), ('L', '0.89'), ('K', '0.88'), ('M', '0.89'), ('F', '0.88'),
     ('P', '0.88'), ('S', '0.89'), ('T', '0.89'), ('W', '0.88'), ('Y', '0.88'), ('V', '0.89')])), ('Q', OrderedDict(
    [('A', '0.9'), ('R', '0.92'), ('N', '0.91'), ('D', '0.9'), ('C', '0.88'), ('Q', '0.36'), ('E', '0.93'),
     ('G', '0.88'), ('H', '0.92'), ('I', '0.88'), ('L', '0.88'), ('K', '0.92'), ('M', '0.91'), ('F', '0.88'),
     ('P', '0.89'), ('S', '0.9'), ('T', '0.9'), ('W', '0.88'), ('Y', '0.88'), ('V', '0.88')])), ('E', OrderedDict(
    [('A', '0.9'), ('R', '0.9'), ('N', '0.9'), ('D', '0.92'), ('C', '0.86'), ('Q', '0.93'), ('E', '0.45'),
     ('G', '0.88'), ('H', '0.9'), ('I', '0.88'), ('L', '0.88'), ('K', '0.91'), ('M', '0.88'), ('F', '0.87'),
     ('P', '0.89'), ('S', '0.9'), ('T', '0.9'), ('W', '0.87'), ('Y', '0.88'), ('V', '0.88')])), ('G', OrderedDict(
    [('A', '0.91'), ('R', '0.88'), ('N', '0.9'), ('D', '0.89'), ('C', '0.88'), ('Q', '0.88'), ('E', '0.88'),
     ('G', '0.45'), ('H', '0.88'), ('I', '0.87'), ('L', '0.87'), ('K', '0.89'), ('M', '0.88'), ('F', '0.87'),
     ('P', '0.88'), ('S', '0.9'), ('T', '0.88'), ('W', '0.88'), ('Y', '0.87'), ('V', '0.87')])), ('H', OrderedDict(
    [('A', '0.89'), ('R', '0.91'), ('N', '0.91'), ('D', '0.89'), ('C', '0.87'), ('Q', '0.92'), ('E', '0.9'),
     ('G', '0.88'), ('H', '0.27'), ('I', '0.88'), ('L', '0.88'), ('K', '0.9'), ('M', '0.88'), ('F', '0.89'),
     ('P', '0.88'), ('S', '0.89'), ('T', '0.89'), ('W', '0.88'), ('Y', '0.92'), ('V', '0.88')])), ('I', OrderedDict(
    [('A', '0.89'), ('R', '0.88'), ('N', '0.88'), ('D', '0.87'), ('C', '0.89'), ('Q', '0.88'), ('E', '0.88'),
     ('G', '0.87'), ('H', '0.88'), ('I', '0.55'), ('L', '0.92'), ('K', '0.88'), ('M', '0.92'), ('F', '0.9'),
     ('P', '0.88'), ('S', '0.88'), ('T', '0.9'), ('W', '0.88'), ('Y', '0.89'), ('V', '0.93')])), ('L', OrderedDict(
    [('A', '0.89'), ('R', '0.88'), ('N', '0.88'), ('D', '0.87'), ('C', '0.89'), ('Q', '0.88'), ('E', '0.88'),
     ('G', '0.87'), ('H', '0.88'), ('I', '0.92'), ('L', '0.55'), ('K', '0.88'), ('M', '0.93'), ('F', '0.91'),
     ('P', '0.88'), ('S', '0.88'), ('T', '0.89'), ('W', '0.88'), ('Y', '0.89'), ('V', '0.91')])), ('K', OrderedDict(
    [('A', '0.9'), ('R', '0.93'), ('N', '0.91'), ('D', '0.9'), ('C', '0.88'), ('Q', '0.92'), ('E', '0.91'),
     ('G', '0.89'), ('H', '0.9'), ('I', '0.88'), ('L', '0.88'), ('K', '0.45'), ('M', '0.89'), ('F', '0.88'),
     ('P', '0.89'), ('S', '0.9'), ('T', '0.9'), ('W', '0.87'), ('Y', '0.88'), ('V', '0.88')])), ('M', OrderedDict(
    [('A', '0.89'), ('R', '0.89'), ('N', '0.88'), ('D', '0.88'), ('C', '0.89'), ('Q', '0.91'), ('E', '0.88'),
     ('G', '0.88'), ('H', '0.88'), ('I', '0.92'), ('L', '0.93'), ('K', '0.89'), ('M', '0.36'), ('F', '0.9'),
     ('P', '0.88'), ('S', '0.89'), ('T', '0.9'), ('W', '0.89'), ('Y', '0.89'), ('V', '0.91')])), ('F', OrderedDict(
    [('A', '0.88'), ('R', '0.88'), ('N', '0.88'), ('D', '0.87'), ('C', '0.88'), ('Q', '0.88'), ('E', '0.87'),
     ('G', '0.87'), ('H', '0.89'), ('I', '0.9'), ('L', '0.91'), ('K', '0.88'), ('M', '0.9'), ('F', '0.36'),
     ('P', '0.88'), ('S', '0.88'), ('T', '0.88'), ('W', '0.91'), ('Y', '0.93'), ('V', '0.89')])), ('P', OrderedDict(
    [('A', '0.9'), ('R', '0.88'), ('N', '0.88'), ('D', '0.88'), ('C', '0.88'), ('Q', '0.89'), ('E', '0.89'),
     ('G', '0.88'), ('H', '0.88'), ('I', '0.88'), ('L', '0.88'), ('K', '0.89'), ('M', '0.88'), ('F', '0.88'),
     ('P', '0.27'), ('S', '0.89'), ('T', '0.89'), ('W', '0.87'), ('Y', '0.88'), ('V', '0.88')])), ('S', OrderedDict(
    [('A', '0.92'), ('R', '0.9'), ('N', '0.91'), ('D', '0.9'), ('C', '0.89'), ('Q', '0.9'), ('E', '0.9'), ('G', '0.9'),
     ('H', '0.89'), ('I', '0.88'), ('L', '0.88'), ('K', '0.9'), ('M', '0.89'), ('F', '0.88'), ('P', '0.89'),
     ('S', '0.55'), ('T', '0.92'), ('W', '0.88'), ('Y', '0.88'), ('V', '0.89')])), ('T', OrderedDict(
    [('A', '0.91'), ('R', '0.89'), ('N', '0.91'), ('D', '0.89'), ('C', '0.89'), ('Q', '0.9'), ('E', '0.9'),
     ('G', '0.88'), ('H', '0.89'), ('I', '0.9'), ('L', '0.89'), ('K', '0.9'), ('M', '0.9'), ('F', '0.88'),
     ('P', '0.89'), ('S', '0.92'), ('T', '0.45'), ('W', '0.88'), ('Y', '0.89'), ('V', '0.9')])), ('W', OrderedDict(
    [('A', '0.88'), ('R', '0.88'), ('N', '0.87'), ('D', '0.86'), ('C', '0.88'), ('Q', '0.88'), ('E', '0.87'),
     ('G', '0.88'), ('H', '0.88'), ('I', '0.88'), ('L', '0.88'), ('K', '0.87'), ('M', '0.89'), ('F', '0.91'),
     ('P', '0.87'), ('S', '0.88'), ('T', '0.88'), ('W', '0.0'), ('Y', '0.93'), ('V', '0.88')])), ('Y', OrderedDict(
    [('A', '0.88'), ('R', '0.88'), ('N', '0.88'), ('D', '0.88'), ('C', '0.88'), ('Q', '0.88'), ('E', '0.88'),
     ('G', '0.87'), ('H', '0.92'), ('I', '0.89'), ('L', '0.89'), ('K', '0.88'), ('M', '0.89'), ('F', '0.93'),
     ('P', '0.88'), ('S', '0.88'), ('T', '0.89'), ('W', '0.93'), ('Y', '0.27'), ('V', '0.88')])), ('V', OrderedDict(
    [('A', '0.9'), ('R', '0.88'), ('N', '0.88'), ('D', '0.87'), ('C', '0.89'), ('Q', '0.88'), ('E', '0.88'),
     ('G', '0.87'), ('H', '0.88'), ('I', '0.93'), ('L', '0.91'), ('K', '0.88'), ('M', '0.91'), ('F', '0.89'),
     ('P', '0.88'), ('S', '0.89'), ('T', '0.9'), ('W', '0.88'), ('Y', '0.88'), ('V', '0.55')]))])
