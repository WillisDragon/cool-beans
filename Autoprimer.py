# autoFprimer
seq = "ggatggggcacgtggatcgatccatcgatattatattatagcgccgtgatcttttttccagtacttttggctaattgtacg"
minlen = 20
maxlen = 27
minTm = 55
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
		SScount = oligo.count("tttttt") + oligo.count("gggg") + oligo.count("aaaaaa") + oligo.count("cccc") + oligo.count("atatata") + oligo.count("agagaga") + oligo.count("acacaca") + oligo.count("tatatat") + oligo.count("tgtgtgt") + oligo.count("tctctct") + oligo.count("gagagag") + oligo.count("gtgtgtg") + oligo.count("gcgcgcg") + oligo.count("cacacac") + oligo.count("ctctctc") + oligo.count("cgcgcgc")
		GCcount = oligo.count("gg") + oligo.count("cc") + oligo.count("gc") + oligo.count("cg") - oligo.count("ggg") + oligo.count("ccg") - oligo.count("gcg") - oligo.count("cgg") - oligo.count("ggc") - oligo.count("ccc") - oligo.count("gcc") - oligo.count("cgc") - oligo.count("ggc")
# calc Tm
		Tm = 64.9 + 41*(GC_count - 16.4)/(AT_count + GC_count)
		if Tm >= minTm and Tm <= maxTm:
			if threeGC_count/5 == 0.6:
				if SScount == 0:
					if GCcount >= 3:
						if GCcount <6:
							print(oligo, "Tm:", f'{Tm:.1f}', "GC:", f'{GC_count/len(oligo):.2f}', "size:", len(oligo))

"""
		aaaaaaSS = oligo.find("aaaaaa")
		ttttttSS = oligo.find("tttttt")
		ggggSS = oligo.find("gggg")
		ccccSS = oligo.find("cccc")

if BScount == 0:








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
