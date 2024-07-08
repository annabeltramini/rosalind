import numpy as np
import re

#open file
file = open("inputs/rosalind_splc.txt")
mylist = file.read().splitlines()
file.close()

file = open("inputs/codontable.txt")
cod = file.read().splitlines()
file.close()

#Create dictionary with codon:aa code
cod_dict = {}
for i in cod:
    dnacode = i.split('\t')[0]
    cod_dict[dnacode] = i.split('\t')[1]

#get sequences from fasta and remove the header lines
seqs = list()
old_i = 1
for i in range(1,len(mylist)):
    if mylist[i][0] == ">":
        seqs.append(("".join(mylist[old_i:i])).strip())
        old_i = i+1
seqs.append("".join(mylist[old_i:])) #that for loop doesn't work for the last one


exons = seqs[0] #seq[0] is entire unspliced sequence
for i in range(1,len(seqs)): #for each intron sequence
    exons = exons.replace(seqs[i],"") #remove it from the unspliced sequence

#Translate the spliced seq into aa seq
orf = list()
for b in range(0,len(exons),3):
    orf += cod_dict[exons[b:b+3]]
print("".join(orf))
