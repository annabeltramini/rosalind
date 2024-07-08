import math
file = open("inputs/rosalind_pmch.txt")
fasta = file.read().splitlines()
file.close()
seq = "".join(fasta[1:]).strip()
au = sum([i == "A" for i in seq])
gc = sum([i == "G" for i in seq])
pn = math.factorial(au)*math.factorial(gc)
print(pn)