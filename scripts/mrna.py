from collections import Counter

file = open("inputs/rosalind_mrna.txt")
mrna = file.read().strip()
file.close()

file = open("inputs/codontable.txt")
cod = file.read().splitlines()
file.close()

###CODE USEFUL IN GENERAL
###BUT NOT NOW
#cod_dict = {}
#for i in cod:
#    rnacode = i.split('\t')[0].replace("T","U")
#    cod_dict[rnacode] = i.split('\t')[1]

cod_num = [i.split('\t')[1] for i in cod]
cod_num = Counter(cod_num)

mrna = list(mrna)
mrna.append("*")
mrna_c = Counter(mrna)

aa = list(cod_num.keys())

totcomb = 1
for a in aa:
    comb = (cod_num[a]**mrna_c[a]) % 1000000
    totcomb *= comb
totcomb = totcomb%1000000

print(totcomb)


