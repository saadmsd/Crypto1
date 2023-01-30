#!/usr/bin/python3
import sys	

# Usage: python3 frequence.py fichier_texte


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Occurences = {}
length = 0


file = open(sys.argv[1], "r")
for line in file:
	for c in line:
		if c in alphabet:
			length += 1
			if c in Occurences:
				Occurences[c] += 1
			else:
				Occurences[c] = 1


# Print the frequences
for c in alphabet:
	if c in Occurences:
		print (c, Occurences[c] / length * 100)
	else:
		print (c, 0.0)





