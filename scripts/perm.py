from itertools import permutations
import math

file = open("/Users/anna/Documents/Rosalind_git/inputs/rosalind_perm.txt")
input = int(file.read().strip())
file.close()

total = math.factorial(input)

ordered = [i for i in range(1,input+1)]

perm = permutations(ordered)

f = open("/Users/anna/Documents/Rosalind_git/outputs/rosalind_perm_output.txt", "w")
f.write(str(total)+"\n")
f.close()

f = open("/Users/anna/Documents/Rosalind_git/outputs/rosalind_perm_output.txt", "a")
for i in perm:
    p = str(i)+"\n"
    p = p.replace("(","").replace(")","").replace(",","")
    f.write(p)
f.close()

#I really wanted to get this to work without using itertools.permutations(), so I might want to try again
