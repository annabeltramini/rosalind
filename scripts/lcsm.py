
#open file
file = open("/Users/anna/Documents/Rosalind_git/inputs/rosalind_lcsm.txt")
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

csm = ["A","C","G","T"]
current_csm = []
while csm != current_csm:
    for m in csm:   
        #if (None in [re.search(m+"A",s) for s in seqs]) == False:
        if all(seq.find(m+"A") >= 0 for seq in seqs):
            current_csm.append(m+"A")
        #if (None in [re.search(m+"C",s) for s in seqs]) == False:
        if all(seq.find(m+"C") >= 0 for seq in seqs):
            current_csm.append(m+"C")
        #if (None in [re.search(m+"T",s) for s in seqs]) == False:
        if all(seq.find(m+"T") >= 0 for seq in seqs):    
            current_csm.append(m+"T")
        if all(seq.find(m+"G") >= 0 for seq in seqs):
            current_csm.append(m+"G")
    if len(current_csm)>0:
        csm = current_csm
        current_csm = []
    else:
        print(csm)
        break

