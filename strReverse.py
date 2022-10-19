#!/usr/bin/python3

import strLen  # , joinStr


def reverse(str):
    """
    Currently Works for strings only.

    TODO: Add support for Integers and iterables
    """
    length = strLen.lenght(str) + 1
    ind = -1
    reversedStr = ""

    while ind != -length:
        reversedStr += str[ind]
        #joinStr.conc(reversedStr, str[ind])
        ind += -1
    return reversedStr
