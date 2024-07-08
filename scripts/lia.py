#Return probability that at least N AaBb organisms 
# will belong to the kth generation

#   AB   Ab   aB   ab
#AB AABB AABb AaBB AaBb
#Ab AABb AAbb AaBb Aabb
#aB AaBB AaBb aaBB aaBb
#ab AaBb Aabb aaBb aabb

#What happens in the first generation
#Tom is AaBb and mates with an AaBb and has two children

#prob = pAA * 1/2 + pAa * 1/2 + paa * 1/2
    # 1/2(pAA + pAa + paa) = 1/2 

#Probability of Aa = 1/2, and of Bb is 1/2 at any generation
import math
#Read file
file = open("inputs/rosalind_lia.txt")
inputs = file.read().strip()
file.close()
inputs = inputs.split(" ")

k = int(inputs[0]) #treat as integers
N = int(inputs[1]) #treat as integers
p = 1/4 #p(AaBb) = p(Aa)*p(Bb) = 1/2*1/2
q = 1 - p 

#Binomial distribution !
#"At least N organisms" means that I need to sum all the cases of N, N+1...2^k (tot population) successes
totprob = 0
for n in range(N,2**k+1):
    prob = math.comb(2**k,n)* p**n * q**(2**k-n) #prob of n successes !
    totprob += prob
print(round(totprob,3))

