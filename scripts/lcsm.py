
#open file
file = open("inputs/rosalind_lcsm.txt")
mylist = file.read().splitlines()
file.close()

#get sequences from fasta
seqs = list()
old_i = 1
##Join each group of lines that are part of thesequences and not headers
for i in range(1,len(mylist)):
    if mylist[i][0] == ">":
        seqs.append(("".join(mylist[old_i:i])).strip())
        old_i = i+1
seqs.append("".join(mylist[old_i:])) #that for loop doesn't work for the last one
###This produces a list of strings with each sequence as an element

csm = ["A","C","G","T"] #start with 1b long sequences
current_csm = []

#Keep adding bases when you find a match until you don't find anymore matches
while csm != current_csm:
    for m in csm: #for each possible common sequence
        #If every sequence contains the current common sequence+the next letter, store it in current_csm   
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
    if len(current_csm)>0: #If something has changed, update the csm to the latest version
        csm = current_csm
        current_csm = []
    else: #If nothing chances, print and exit the loop
        print(csm) 
        break #this is because by updating current csm at this point,  you never would exit the loop otherwise

