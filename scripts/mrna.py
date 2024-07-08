from collections import Counter

file = open("inputs/rosalind_mrna.txt")
mrna = file.read().strip()
file.close()

file = open("inputs/codontable.txt")
cod = file.read().splitlines()
file.close()

#create a list with each AA code
cod_num = [i.split('\t')[1] for i in cod]
cod_num = Counter(cod_num) #each AA and the number of times it appears in the table

mrna = list(mrna) #convert to list for Counter
mrna.append("*") #Add a stop codon at the end of the mrna sequences
mrna_c = Counter(mrna) #number of times each  aa is encoded in the mrna seq

aa = list(cod_num.keys()) #list of all the amino acid codes for iterating

#Calculate total number of combinations
totcomb = 1
for a in aa: #loop through each amino acid
    comb = (cod_num[a]**mrna_c[a]) % 1000000 #modulo 1mil to handle smaller numbers
    totcomb *= comb
totcomb = totcomb%1000000

print(totcomb)


