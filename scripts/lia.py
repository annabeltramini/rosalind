#Return probability that at least N AaBb organisms 
# will belong to the kth generation

#   AB   Ab   aB   ab
#AB AABB AABb AaBB AaBb
#Ab AABb AAbb AaBb Aabb
#aB AaVV AaBb aaBB aaBb
#ab AaBb Aabb aaBb aabb

#What happens in the first generation
#Tom is AaBb and mates with an AaBb and has two children

#prob = pAA * 1/2 + pAa * 1/2 + paa * 1/2
    # 1/2(pAA + pAa + paa) = 1/2 

#Probability of Aa = 1/2, and of Bb is 1/2
import math

file = open("/Users/anna/Documents/Rosalind_git/inputs/rosalind_lia.txt")
inputs = file.read().strip()
file.close()

inputs = inputs.split(" ")
k = int(inputs[0])
N = int(inputs[1])
p = 1/4
q = 1 - 1/4

totprob = 0
for n in range(N,2**k+1):
    prob = math.comb(2**k,n)* p**n * q**(2**k-n)
    totprob += prob
print(round(totprob,3))



#gen 0 -> prob 1
#gen 1 -> prob 1/2
#gen 2 -> prob 1/2
#gen 3 -> prob 1/2


#pAa = 1/2 , pBb = 1/2
#pAaBb = 1/4 

# k <= 7
# N <= 2^k

#number of people 2^7