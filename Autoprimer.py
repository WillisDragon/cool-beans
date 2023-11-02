# autoFprimer

seq = "ggatggcacacgtggatcgatccatcgatcgtgatcgtccagtacggctaattgtacg"

minlen = 20
maxlen = 27
for i in range(len(seq)-minlen):
	for j in range(i+minlen, i+maxlen+1):
		GC_count = 0
		AT_count = 0
		#make oligo
		oligo = seq[i:j]
		for k in range(len(oligo)):
			nt = oligo[k]
			if nt == 'c' or nt == 'g':
				GC_count += 1
			if nt == 'a' or nt == 't':
				AT_count += 1
		# calc Tm
		Tm = 64.9 + 41*(GC_count - 16.4)/(AT_count + GC_count)
		if Tm >= 57 and Tm <=60:
			print(oligo, f'{Tm:.1f}', f'{GC_count/len(oligo):.2f}', len(oligo), GC_count, AT_count)


















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
