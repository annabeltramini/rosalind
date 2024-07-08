import re

file = open("inputs/rosalind_revp.txt")
ref = file.read().splitlines()
file.close()

ref = "".join(ref[1:]) #store sequence, remove FASTA header

#The position and length of every reverse palindrome in the string having length between 4 and 12. 
#You may return these pairs in any order.

#Create reverse complement of a sequence
def revc(seq):
    #[::-1] to get the reverse and use lowercase to avoid altering the sequence
    revc = seq[::-1].replace("A","t").replace("G","c").replace("T","a").replace("C","g")
    revc = revc.upper() #for convension
    return revc
revseq = revc(ref)

re_sites = [] 
re_len = []

#For each possible length of seq between 12 and 4 (even only)
for i in range(12,3,-2):
    #For each position in the reference seq
    for j in range(0,len(ref)-i+1): 
        if ref[j:j+i] == revc(ref[j:j+i]):
            re_sites.append(j+1)
            re_len.append(i)

#Final filtering and formatting of the findings
re_fin = []
for i in range(len(re_sites)):
    if re_len[i] % 2 == 0: #rev palindromes are by definition even length
        re_fin.append((re_sites[i], re_len[i]))

for x in re_fin:
    print(x[0],x[1])

