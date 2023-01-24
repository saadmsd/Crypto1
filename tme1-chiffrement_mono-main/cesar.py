#!/usr/bin/python3

# Usage: python3 cesar.py clef c/d phrase
# Returns the result without additional text

import sys

#Écrire un programme permettant de réaliser le chiffrement et déchiffrement de César.

phrase = sys.argv[3]
cd = sys.argv[2]
cle = sys.argv[1]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chiffrement(mot, cle):
    mot_chiffre = ""
    for i in range(len(mot)):
        mot_chiffre += alphabet[(alphabet.index(mot[i]) + alphabet.index(cle[i % len(cle)])) % len(alphabet)]
    return mot_chiffre

def dechiffrement(mot, cle):
    mot_dechiffre = ""
    for i in range(len(mot)):
        mot_dechiffre += alphabet[(alphabet.index(mot[i]) - alphabet.index(cle[i % len(cle)])) % len(alphabet)]
    return mot_dechiffre

if (cd == "c"): 
    print(chiffrement(phrase, cle))
else:
    print(dechiffrement(phrase, cle))




