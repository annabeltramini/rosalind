import numpy as np
import re
#open file
file = open("/Users/anna/Desktop/Rosalind/rosalind_orf.txt")
fasta = file.read().splitlines()
file.close()

seq = "".join(fasta[1:]).strip()

file = open("codontable.txt")
cod = file.read().splitlines()
file.close()

cod_dict = {}
for i in cod:
    rnacode = i.split('\t')[0]
    cod_dict[rnacode] = i.split('\t')[1]

start_matches = re.finditer(r'(?=ATG)',seq)
starts = [m.start(0) for m in start_matches]

orfs = list()
for i in starts:
    prot = ""
    while (len(prot) == 0 or prot[-1] != "*")  and i+3 <= len(seq):    
    #seq[i:i+3] != "TAA" and seq[i:i+3] != "TA" and seq[i:i+3] != "TGA":
        prot += cod_dict[seq[i:i+3]]
        i = i+3
    if prot[-1] == "*":   
        orfs.append(prot[:-1])

revc = seq[::-1].replace("A","t").replace("T","a").replace("G","c").replace("C","g")
revc = revc.upper()

start_matches = re.finditer(r'(?=ATG)',revc)
starts = [m.start(0) for m in start_matches]

for i in starts:
    prot = ""
    while (len(prot) == 0 or prot[-1] != "*")  and i+3 <= len(revc):    
    #seq[i:i+3] != "TAA" and seq[i:i+3] != "TA" and seq[i:i+3] != "TGA":
        prot += cod_dict[revc[i:i+3]]
        i = i+3
    if prot[-1] == "*":   
        orfs.append(prot[:-1])

orfs = set(orfs)
[ print(orf) for orf in orfs ]

#I could have used a function
#I could have written them into files    
