#For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
# N{P}[ST]{P}

from urllib.request import urlopen
import re

#Open the file
file = open("inputs/rosalind_mprt.txt")
mylist = file.read()
file.close()

mylist = mylist.split("\n")
mylist = list(filter(None, mylist)) #remove empty elements

for id in mylist:
    protid = id.split("_")[0] #In case of a specific protid, get only the first word and ignore the organism
    #Open the URL and get information from it
    urlname = "http://www.uniprot.org/uniprot/"+protid+".fasta"
    page = urlopen(urlname)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    fasta = "".join(html.split("\n")[1:])
    #Option 1 using finditer
    #mot = re.finditer("N(?![P])[A-Z][ST](?![P])[A-Z]",fasta)
    #starts = [m.start(0)+1 for m in mot]
    
    #Option 2 using search at each 4 bases of the sequence
    starts = list()
    for i in range(0,len(fasta)-4):
        start = None
        start = re.search("N(?![P])[A-Z][ST](?![P])[A-Z]",fasta[i:i+4])
        if start != None:
            starts.append(i+1)
    if len(starts) > 0:
        print(id)
        print(*starts)

#"N(?![P])[A-Z][ST](?![P])[A-Z]" is equivalent to N{P}[ST]{P}:
    #1st character is N
    #2nd character is any other capital letter other than P
    #3rd character is either S or T
    #4th character any other capital letter other than P