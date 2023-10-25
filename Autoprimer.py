# autoFprimer

seq = "agatagcacacgtggatcgatccatcgatcgggatcgtccagtacggctaattgtacg"

w = 5
total_GC = 0
for i in range(14, 19):
	if seq[i] == 'c' or seq[i] == 'g':
		total_GC += 1
print(14, seq[14:19], total_GC/w)

for i in range(15, len(seq)-w+1):
	off = seq[i-1]
	on = seq[i-1 + w]
	if off == 'g' or off == 'c':
		total_GC -= 1
	if on == 'g' or on == 'c':
		total_GC += 1
	if total_GC/w == 0.6:
		print(i, seq[i:i+w], total_GC/w)
