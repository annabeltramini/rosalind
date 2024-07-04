import re

file = open("inputs/rosalind_revp.txt")
ref = file.read().splitlines()
file.close()

ref = "".join(ref[1:])

#The position and length of every reverse palindrome in the string having length between 4 and 12. 
#You may return these pairs in any order.

def revc(seq):
    revc = seq[::-1].replace("A","t").replace("G","c").replace("T","a").replace("C","g")
    revc = revc.upper()
    return revc

is_revp = False

revseq = revc(ref)
#print(revseq)
#position
#len

re_sites = []
re_len = []


#re.findall("XXX",mystring) #all the matches
    #BUT id does not find overlapping seq !
#prog = re.compile("regex_pattern")
#result = prog.match(mystring)
#is equivalent to result = re.match(pattern, string)



"""
for j in range(0,len(ref)-4):
    matches = re.finditer(revseq[j:j+4],ref)
    starts = [m.start(0) for m in matches if m.start(0)]
    for s in starts:
        re_sites.append(s+1)
        re_len.append(4)

re_fin = []
for i in range(len(re_sites)):
    re_fin.append((re_sites[i], re_len[i]))

print(set(re_fin))
"""

"""
re_identified = []
for i in range(12,3,-1):
    for j in range(0,len(ref)-i):
        matches = re.finditer(revseq[j:j+i],ref)
        starts = [m.start(0) for m in matches if m.start(0)]
        #ends = [m.end(0) for m in matches if m.end(0)]
        for s in starts:
            if s+1 not in re_sites:
                re_sites.append(s+1)
                re_len.append(i)
                #re_identified.extend(list(range(s+1,s+1+i)))
"""

for i in range(12,3,-2):
    for j in range(0,len(ref)-i+1):
        if ref[j:j+i] == revc(ref[j:j+i]):
            re_sites.append(j+1)
            re_len.append(i)


print(re_sites+re_len)
#print(sum(re_sites,re_len))
re_fin = []
for i in range(len(re_sites)):
    if re_len[i] % 2 == 0:
        re_fin.append((re_sites[i], re_len[i]))


for x in re_fin:
    print(x[0],x[1])

#I had definitely overcomplecated it