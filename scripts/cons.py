import numpy as np

#open file
file = open("/Users/anna/Documents/Rosalind_git/inputs/rosalind_cons.txt")
mylist = file.read().splitlines()
file.close()

#get sequences from fasta
seqs = list()
old_i = 1
for i in range(1,len(mylist)):
    if mylist[i][0] == ">":
        seqs.append(("".join(mylist[old_i:i])).strip())
        old_i = i+1
seqs.append("".join(mylist[old_i:])) #that for loop doesn't work for the last one

#print([len(i) for i in seqs])

#mylist = [i for i in mylist.splitlines() if i[0] != ">"]
#mylist = [i for i in mylist.splitlines() if i[0] != ">"]
#print(mylist)
A_count = list()
C_count = list()
G_count = list()
T_count  = list()
cons = ""

#go through each position and find the highest
for x in range(0,len(seqs[0])):
    first = [i[x] for [*i] in seqs]
    A_count.append(first.count("A"))
    C_count.append(first.count("C"))
    G_count.append(first.count("G"))
    T_count.append(first.count("T"))
    cons_n = np.argmax([A_count[x],C_count[x],G_count[x],T_count[x]])
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
#print(cons)
#print(cons,"\nA:", *A_count,"\nC:", *C_count,"\nG:",
#       *G_count,"\nT:", *T_count,)

fin_out = cons+" \nA: "+ ' '.join(str(x) for x in A_count)+" \nC: "+ ' '.join(str(x) for x in C_count)+" \nG: "+' '.join(str(x) for x in G_count)+" \nT: "+' '.join(str(x) for x in T_count)
#print(fin_out)

#write file
f = open("/Users/anna/Documents/Rosalind_git/outputs/rosalind_cons_output.txt", "w")
f.write(fin_out)
f.close()
