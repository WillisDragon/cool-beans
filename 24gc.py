# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places


dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

total_G_and_C = 0
total_letters = 0

for i in range(len(dna)):
	letter = dna[i]
	if letter == 'G' or letter == 'C':
		total_G_and_C += 1
	total_letters += 1
		
		
print(f'{total_G_and_C/total_letters:.2f}')	
	
	





"""
python3 24gc.py
0.42
"""
