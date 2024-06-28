file = open("/Users/anna/Documents/Rosalind_git/inputs/rosalind_prtm.txt")
input = file.read().strip()
file.close()

file = open("/Users/anna/Documents/Rosalind_git/inputs/weighted_aa.txt")
aa_weights = file.read().splitlines()
file.close()

aa_dict = {}

for w in aa_weights:
    aa_dict[w.split("   ")[0]] = float(w.split("   ")[1])

P_weight = 0
for a in input:
    P_weight += aa_dict[a]

print(round(P_weight,3))