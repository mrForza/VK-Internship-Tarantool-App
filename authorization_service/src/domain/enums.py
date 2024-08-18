from enum import Enum


class ViolatedLength(int, Enum):
    SMALL = 0
    BIG = 1


class MissingSymbols(int, Enum):
    LOWER_CASE = 0
    UPPER_CASE = 1
    DIGITS = 2
    SPECIAL_SYMBOLS = 3
