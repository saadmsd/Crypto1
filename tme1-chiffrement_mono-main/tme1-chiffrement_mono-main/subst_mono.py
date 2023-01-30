#!/usr/bin/python3

# Usage: python3 subst_mono.py clef c/d phrase
# Returns the result without additional text
import sys
phrase = sys.argv[3]
cd = sys.argv[2]
cle = sys.argv[1]

alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_subst='OULSGCZQIYFEBMPDJWXKVANHRT'
def chiffrement(mot):
    return mot.translate(str.maketrans(alph,cle))
def dechiffrement(mot):
    return mot.translate(str.maketrans(cle,alph))

if (cd == "c"): 
    print(chiffrement(phrase))
else:
    print(dechiffrement(phrase))
