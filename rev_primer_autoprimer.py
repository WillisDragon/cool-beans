# rev_primer_autoprimer
seq = "ggatggggcacgtggatcgatccatcgatattatattatagcgccgtgatcttttttccagtacttttggctaattgtacg"
seqRC = ""
for i in range(len(seq)):
	ntRC = seq[len(seq)-1-i]
	if ntRC == "a":
		seqRC = seqRC + "t"
	elif ntRC == "t":
		seqRC = seqRC + "a"
	elif ntRC == "g":
		seqRC = seqRC + "c"
	else:		seqRC = seqRC + "g"	
minlen = 20
maxlen = 27
minTm = 55
maxTm = 60
for i in range(len(seqRC)-minlen):
	for j in range(i+minlen, i+maxlen+1):
		GC_count = 0
		AT_count = 0
#make oligo
		oligo = seqRC[i:j]
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
		GCclamp = oligo.count("gg") + oligo.count("cc") + oligo.count("gc") + oligo.count("cg") - oligo.count("ggg") + oligo.count("ccg") - oligo.count("gcg") - oligo.count("cgg") - oligo.count("ggc") - oligo.count("ccc") - oligo.count("gcc") - oligo.count("cgc") - oligo.count("ggc")
# calc Tm
		Tm = 64.9 + 41*(GC_count - 16.4)/(AT_count + GC_count)
		if Tm >= minTm and Tm <= maxTm:
			if threeGC_count/5 == 0.6:
				if SScount == 0:
					if GCclamp >= 3:
						if GCclamp <6:
							print(oligo, "Tm:", f'{Tm:.1f}', "GC:", f'{GC_count/len(oligo):.2f}', "size:", len(oligo))



