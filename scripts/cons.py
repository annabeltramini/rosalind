import numpy as np

#open file
file = open("inputs/rosalind_cons.txt")
mylist = file.read().splitlines()
file.close()

#get sequences from fasta file
seqs = list()
old_i = 1
##Join each group of lines that are part of thesequences and not headers
for i in range(1,len(mylist)):
    if mylist[i][0] == ">":
        seqs.append(("".join(mylist[old_i:i])).strip())
        old_i = i+1
seqs.append("".join(mylist[old_i:])) #that for loop doesn't work for the last one
###This produces a list of strings with each sequence as an element
#print([len(i) for i in seqs])

#initialise the lists that will contain the number of each base across sequences
A_count = list()
C_count = list()
G_count = list()
T_count  = list()
cons = "" #will store the consesus sequence

#go through each position and find the highest
for x in range(0,len(seqs[0])): #this works because all sequences are of the same length
    base = [i[x] for [*i] in seqs] #produces a list of the xth element in each sequence
    A_count.append(base.count("A"))
    C_count.append(base.count("C"))
    G_count.append(base.count("G"))
    T_count.append(base.count("T"))
    cons_n = np.argmax([A_count[x],C_count[x],G_count[x],T_count[x]]) #pick the highest occurring base
    #this code will always give the same consensus sequence in case of even max values where the priority is A > C > G > T
    #therefore will overrepresent A in consensus sequences over Cs etc.

    if cons_n == 0:
        cons += "A"
    elif cons_n == 1:
        cons += "C"
    elif cons_n == 2:
        cons += "G"
    else:
        cons += "T"
    #maybe I could have used enumerate?

#Format the output as requested:
fin_out = cons+" \nA: "+ ' '.join(str(x) for x in A_count)+" \nC: "+ ' '.join(str(x) for x in C_count)+" \nG: "+' '.join(str(x) for x in G_count)+" \nT: "+' '.join(str(x) for x in T_count)
#print(fin_out)

#write file
f = open("outputs/rosalind_cons_output.txt", "w")
f.write(fin_out)
f.close()
