import itertools 

#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).#

#Read in input file
f = open("inputs/rosalind_lexf.txt","r")
inputs = f.readlines()
f.close()

A = inputs[0].strip().split() #first line, remove whitespace, turn into list
n = int(inputs[1]) #second line, treat as integer

#Store the solutions
sols = []

########################################
#I generated this code with chatgpt so I want to go trhough it
########################################
#Essentially I really struggle with recursive functions
#I had the right idea but could not execute it
def permute(lst, r):
    result = []

    # Base case: if the current length is the desired length, return it
    if r == 0:
        return [[]]
    
    for i in range(len(lst)):
        # Choose the current element
        elem = lst[i]
        # Remaining list after removing the current element
        remaining_list = lst[:i] + lst[i+1:]
        # Recursively generate permutations of the remaining list with length r-1
        perms = permute(lst, r-1)
        
        # Append the chosen element to each of the generated permutations
        for perm in perms:
            result.append([elem] + perm)

    return result

# Example usage:
lst = [1, 2, 3]
r = 2
solutions = permute(A, n)
#[print("".join(sol)) for sol in solutions]

###Alternative: Method with itertools

#for p in itertools.product(A,repeat=n):
#    print(''.join(p))