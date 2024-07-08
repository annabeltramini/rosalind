from itertools import permutations
import math

file = open("inputs/rosalind_perm.txt")
input = int(file.read().strip())
file.close()

#Total number of possible permutations
total = math.factorial(input)

#Create the different combinations starting from an ordered list
ordered = [i for i in range(1,input+1)]
perm = permutations(ordered) #calculates and stores all permutations as tuples

#Save the number of permutations in a file
f = open("outputs/rosalind_perm_output.txt", "w") #w so it's a new one each time
f.write(str(total)+"\n")
f.close()

f = open("outputs/rosalind_perm_output.txt", "a") #a to append to the file just created
#Print the permutations as simple A B C D instead of as tuples with () and ,
for i in perm:
    p = str(i)+"\n"
    p = p.replace("(","").replace(")","").replace(",","")
    f.write(p)
f.close()

#IMPROVEMENTS
#I really wanted to get this to work without using itertools.permutations(), so I might want to try again
