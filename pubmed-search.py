from sys import argv
from Bio import Entrez, Medline

# Needs to have a message for usage and error handling

Entrez.email = "aromeroc93@gmail.com"
Entrez.api_key = "510d2439a3c3615a6f94e14430a9e33a1c08"

handle = Entrez.esearch(db="pubmed", term=argv[1], reldate=argv[2])
record = Entrez.read(handle)
handle.close()
idlist = record["IdList"]

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle)

for record in records:
    print("title:", record.get("TI", "?"))
    print("authors:", record.get("AU", "?"))
    print("Journal:", record.get("SO", "?"))
    print("ID:", record.get("LID", "?"))
    print("")