import numpy as np
import re
#open file
file = open("inputs/rosalind_orf.txt")
fasta = file.read().splitlines()
file.close()

#store the sequence as a string (removing the header)
seq = "".join(fasta[1:]).strip()

file = open("inputs/codontable.txt")
cod = file.read().splitlines()
file.close()

#Create a dictionary codon_triplet:amino_acid
cod_dict = {}
for i in cod:
    rnacode = i.split('\t')[0]
    cod_dict[rnacode] = i.split('\t')[1]

#Find any start codon within the sequence
#"?=" allows for overlapping finds
start_matches = re.finditer(r'(?=ATG)',seq)
starts = [m.start(0) for m in start_matches]

#Translate the mrna sequences into AA seq from start codon to stop codon
orfs = list()
for i in starts:
    prot = ""
    while (len(prot) == 0 or prot[-1] != "*")  and i+3 <= len(seq):    
    #seq[i:i+3] != "TAA" and seq[i:i+3] != "TA" and seq[i:i+3] != "TGA":
        prot += cod_dict[seq[i:i+3]]
        i = i+3
    if prot[-1] == "*": #when you reach the stop codon append the prot sequence  
        orfs.append(prot[:-1])

#Now check the opposite strand !

#Create reverse complement
#I use lowercase to avoid double replacing bases, and transform back to uppercase for convention
#[::-1] reverses the sequence
revc = seq[::-1].replace("A","t").replace("T","a").replace("G","c").replace("C","g")
revc = revc.upper()

#Repeat the analysis on this strand
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

#Print all unique orfs found
orfs = set(orfs)
[ print(orf) for orf in orfs ]

#IMPROVEMENTS:
#I could have used a function so I didnt copy and paste for revc

