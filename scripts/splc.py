import numpy as np
import re

#open file
file = open("/Users/anna/Documents/Rosalind_git/inputs/rosalind_splc.txt")
mylist = file.read().splitlines()
file.close()

file = open("inputs/codontable.txt")
cod = file.read().splitlines()
file.close()

cod_dict = {}
for i in cod:
    rnacode = i.split('\t')[0]
    cod_dict[rnacode] = i.split('\t')[1]

#get sequences from fasta
seqs = list()
old_i = 1
for i in range(1,len(mylist)):
    if mylist[i][0] == ">":
        seqs.append(("".join(mylist[old_i:i])).strip())
        old_i = i+1
seqs.append("".join(mylist[old_i:])) #that for loop doesn't work for the last one

exons = seqs[0]
for i in range(1,len(seqs)):
    exons = exons.replace(seqs[i],"")

orf = list()
for b in range(0,len(exons),3):
    orf += cod_dict[exons[b:b+3]]
    

print("".join(orf))
