# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
dnarev = dna[::-1]
for i in range(len(dnarev)):
	nt = dnarev[i]
	if nt == 'A': print('T', end='')
	elif nt == 'T': print('A', end='')
	elif nt == 'G': print('C', end='')
	else:		print('G', end='')


"""

python3 26anti.py
TTTTTTTTTTTCAGT
"""
