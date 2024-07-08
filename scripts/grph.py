import numpy as np
#open file
file = open("inputs/rosalind_grph.txt")
mylist = file.read().splitlines()
file.close()

#get sequences from fasta
seqs = list() #store the sequences as strings
names = list() #store the each header
old_i = 1
names.append(mylist[0][1:]) #the first name is not appended in the loop
for i in range(1,len(mylist)):
    if mylist[i][0] == ">":
        seqs.append(("".join(mylist[old_i:i])).strip()) #join the sequences that are across multiple lines
        old_i = i+1
        names.append(mylist[i][1:]) #store the header (without the ">")
seqs.append("".join(mylist[old_i:])) #that for loop doesn't work for the last one

#Check each pair of sequences to see if the start of one corresponds to the end of another
for i in range(0,len(seqs)):
    for j in range(0,len(seqs)):
        if i != j: #must not be the same sequence
            if seqs[i][:3] == seqs[j][-3:]:
                print(names[j], names[i])
