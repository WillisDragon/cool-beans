# autoFprimer

seq = "ggatggcacacgtggatcgatccatcgatattatattatagcgccgtgatcgaaaaatccagtacttttggctaattgtacg"

minlen = 20
maxlen = 27
minTm = 57
maxTm = 60
for i in range(len(seq)-minlen):
	for j in range(i+minlen, i+maxlen+1):
		GC_count = 0
		AT_count = 0
#make oligo
		oligo = seq[i:j]
		for k in range(len(oligo)):
			nt = oligo[k]
			length = len(oligo)
			if nt == 'c' or nt == 'g':
				GC_count += 1
			if nt == 'a' or nt == 't':
				AT_count += 1
# calc 3' GC
		threeGC_count = 0
		threeprime = oligo[length - 5:]
		for l in range(len(threeprime)):
			threent = threeprime[l]
			if threent == 'c' or threent == 'g':
				threeGC_count += 1
# find/count substrings
		badsubstring = oligo.find("aaaaa")
		
		
# calc Tm
		Tm = 64.9 + 41*(GC_count - 16.4)/(AT_count + GC_count)
		if Tm >= minTm and Tm <= maxTm:
			if threeGC_count/5 == 0.6:	
				if badsubstring == -1:
					print(oligo, f'{Tm:.1f}', f'{GC_count/len(oligo):.2f}')


















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
