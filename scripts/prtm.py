file = open("inputs/rosalind_prtm.txt")
input = file.read().strip()
file.close()

file = open("inputs/weighted_aa.txt")
aa_weights = file.read().splitlines()
file.close()

#dictionary storing aa code and weight
aa_dict = {}
for w in aa_weights:
    aa_dict[w.split("   ")[0]] = float(w.split("   ")[1])

#Weight of the protein is equal to the sum of all its amino acids
P_weight = 0
for a in input:
    P_weight += aa_dict[a]

print(round(P_weight,3))