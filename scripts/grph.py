import numpy as np
#open file
file = open("/Users/anna/Documents/Rosalind_git/inputs/rosalind_grph.txt")
mylist = file.read().splitlines()
file.close()

#get sequences from fasta
seqs = list()
names = list()
old_i = 1
names.append(mylist[0][1:])
for i in range(1,len(mylist)):
    if mylist[i][0] == ">":
        seqs.append(("".join(mylist[old_i:i])).strip())
        old_i = i+1
        names.append(mylist[i][1:])
seqs.append("".join(mylist[old_i:])) #that for loop doesn't work for the last one

#checked = [[N] * len(seqs)] * len(seqs)
for i in range(0,len(seqs)):
    for j in range(0,len(seqs)):
        if i != j:
            if seqs[i][:3] == seqs[j][-3:]:
                print(names[j], names[i])
