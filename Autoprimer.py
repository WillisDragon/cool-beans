# autoFprimer

seq = "agatagcacacgtggatcgatccatcgatcgtgatcgtccagtacggctaattgtacg"


for i in range(len(seq)-20):
	for j in range(i+20, i+28):
		total_GC = 0
		total_AT = 0
		oligo = seq[i:j]
		nt = oligo[i:j]
		if nt == 'c' or nt == 'g':
			total_GC += 1
		if nt == 'a' or nt == 't':
			total_AT += 1
		
		print(oligo, total_GC, total_AT)


















"""
w = 5
total_GC = 0
for i in range(10, 15):
	if seq[i] == 'c' or seq[i] == 'g':
		total_GC += 1
print(i, seq[i:i+w], total_GC/w)

for i in range(15, len(seq)-w+1):
	off = seq[i-1]
	on = seq[i-1 + w]
	if off == 'g' or off == 'c':
		total_GC -= 1
	if on == 'g' or on == 'c':
		total_GC += 1
	if total_GC/w == 0.6:
		print(i, seq[i:i+w], total_GC/w)
"""
