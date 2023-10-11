# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random
n = 30
s = ''
total_AT = 0
for i in range(n):
	s += random.choice('ATTATAGCCG')
for i in range(len(s)):
	nt = s[i]
	if nt == 'A' or nt == 'T':
		total_AT += 1
print(n, s, total_AT/n)


"""
# alternatively	
t = 0
for i in range(n):
	t += i
	
f = 1
for i in range(1, n):
	f *= i

S = ''
AT = 0.612345
for i in range(n):
	if random.random() < AT
		if random.random() < 0.5: s += 'A'
		else:		s += 'T'
	else:
		if random.random() < 0.5: s += 'C'
		else:		s += 'G'
	
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
