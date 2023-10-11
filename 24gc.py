# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places


dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

total_GC = 0
total_nts = 0

for i in range(len(dna)):
	nt = dna[i]
	if nt == 'G' or nt == 'C':
		total_GC += 1
	total_nts += 1
		
		
print(f'{total_GC/total_nts:.2f}')	
	
	





"""
python3 24gc.py
0.42
"""
