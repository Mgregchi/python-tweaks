#!/usr/bin/python3

from pickle import BYTEARRAY8

numbers = [48, 57]
alphabets_upper = [65, 90]
alphabets_lower = [97, 122]
alphabets = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "I": "i",
    "J": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "O": "o",
    "P": "p",
    "Q": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "W": "w",
    "X": "x",
    "Y": "y",
    "Z": "z"
}
c = b'\0'
print(c)
a = b'a'
b = b'b'
c = b'c'
by = bytes([50, 65, 66, 67, 90])
print("65, 66, 67 = ", by.decode())

print(bytearray("h", encoding="utf"))
print(bytes.decode(a))
print("%d %a", a)

print(BYTEARRAY8)
print(b > a)
print(c > b)
"""
for a in range(65, 123):
    char = bytearray([a])
    print(f"{a}: {char.decode()}\n")
"""
