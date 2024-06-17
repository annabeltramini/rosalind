#the expected value of X is E(X)=∑nk=1k×Pr(X=k)

#X is a uniform random variable with minimum possible value a
#and maximum possible value b, then E(X)=a+b2

#Inputs: Six nonnegative integers, each of which does not exceed 20,000
#The integers correspond to the number of couples in a population possessing 
# each genotype pairing for a given factor.

#Open the file
file = open("inputs/rosalind_iev.txt")
probs = file.read().split()
file.close()

#Store as integers instead of characters
probs = [int(p) for p in probs]
print(probs)

# Num of offspirng with dominant phenotype if each couple has two offspring

dom_off = 2*(probs[0] * 1 + probs[1] * 1 + probs[2] * 1 + probs[3] * 3/4 + probs[4] * 1/2 + probs[5] * 0)
print(dom_off)