from urllib.request import urlopen
import re

file = open("/Users/anna/Desktop/Rosalind/rosalind_mprt.txt")
mylist = file.read()
file.close()

mylist = mylist.split("\n")
mylist = list(filter(None, mylist))


#For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
# N{P}[ST]{P}

#fasta = "MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK"
#x = re.findall("N(?![P])[A-Z][ST](?![P])[A-Z]",fasta)

#all_starts = [None] * len(mylist)
#starts = list()
#for i in range(0,len(fasta)-4):
#    start = None
#    start = re.search("N(?![P])[A-Z][ST](?![P])[A-Z]",fasta[i:i+4])
#    if start != None:
#        starts.append(start(i+1))

#starts = [str(i + 1) for i in range(len(fasta)-3) if is_N_glycosylation(i, fasta)]
   
#print(x)

for id in mylist:
    protid = id.split("_")[0]
    urlname = "http://www.uniprot.org/uniprot/"+protid+".fasta"
    page = urlopen(urlname)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    fasta = "".join(html.split("\n")[1:])
    #mot = re.finditer("N(?![P])[A-Z][ST](?![P])[A-Z]",fasta)
    #starts = [m.start(0)+1 for m in mot]
    starts = list()
    for i in range(0,len(fasta)-4):
        start = None
        start = re.search("N(?![P])[A-Z][ST](?![P])[A-Z]",fasta[i:i+4])
        if start != None:
            starts.append(i+1)
    if len(starts) > 0:
        print(id)
        print(*starts)


#Check at each and every position I have seen that many people are expressing their anguish.