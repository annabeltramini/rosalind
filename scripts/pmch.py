import math
#Read file of 1 fasta sequence and remove header
file = open("inputs/rosalind_pmch.txt")
fasta = file.read().splitlines()
file.close()
seq = "".join(fasta[1:]).strip()

#numbers of As in the sequence (= #Us according to instructions)
au = sum([i == "A" for i in seq])
gc = sum([i == "G" for i in seq]) # num of Gs
#Possible perfect matches between A and U * between Gs and Cs
pn = math.factorial(au)*math.factorial(gc)
print(pn)