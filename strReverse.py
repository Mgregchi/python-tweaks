#!/usr/bin/python3

import strLen  # , joinStr


def reverse(str):
    length = strLen.lenght(str) + 1
    ind = -1
    reversedStr = ""

    while ind != -length:
        #print(f"Length: {ind}")
        # print(str[ind])
        reversedStr += str[ind]
        #joinStr.conc(reversedStr, str[ind])
        ind += -1
    return reversedStr
    #print(f"Normal: {str}\nReversed: {reversedStr}")
