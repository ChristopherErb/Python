"""
Girafee code:
All Vowels = "G"

DOG = DGG
CAT = CGT
PYTHON = PGTHGN
ALL VOWELS EQUALS G = GLL VGWGLS GQGGLS G
"""

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUYaeiouy":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Please input a phrase")))
