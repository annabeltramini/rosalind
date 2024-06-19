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

k = 2
N = 1
prob = 1/2 * 1/2
probnot = 1 - prob

finprob = ((2**k-N)*3/4)**(2**k)
print(finprob)


#gen 0 -> prob 1
#gen 1 -> prob 1/2
#gen 2 -> prob 1/2
#gen 3 -> prob 1/2


#pAa = 1/2 , pBb = 1/2
#pAaBb = 1/4 

# k <= 7
# N <= 2^k

#number of people 2^7
