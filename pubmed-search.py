import sys
from sys import argv
from datetime import date
from Bio import Entrez, Medline
import pyperclip

def main():

    # Needs to have a message for usage and error handling
    if len(sys.argv) != 3:
        print("Usage: pubmed-search.py [query] [days]")
        sys.exit(1)
    
    Entrez.email = "aromeroc93@gmail.com"
    Entrez.api_key = "510d2439a3c3615a6f94e14430a9e33a1c08"

    handle = Entrez.esearch(db="pubmed", term=argv[1], reldate=argv[2])
    record = Entrez.read(handle)
    handle.close()
    idlist = record["IdList"]

    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    
    today = date.today()
    today = today.strftime("%Y%m%d")

    i = 1
    file = open("pubmed_searches.md", "a")
    file.write("## " + today + "\n\nFound " + str(len(idlist)) + " papers from query " + argv[1] + " in the last " + argv[2] + " days.\n\n")
    doi_list = []

    # Add some way to check how many results are already in the outpu file/check the last entry, and only consider the new entries.
    
    for record in records:
        title = record.get("TI", "?")
        authors = record.get("AU", "?")
        journal = record.get("SO", "?")
        doi = record.get("LID", "?")
        file.write("Result #" + str(i) + "\nTitle:" + title + "\nJournal:" + journal + "\nAuthors:")
        for author in authors:
            file.write(author + ",")
        file.write("\n\n")
        print("Result #", i, "\nTitle:", title, "\nAuthors:", authors, "\n")
        doi_list.append(doi)
        i += 1

    file.close()

    n = input("DOI to copy? ")
    print("Desired DOI:", doi_list[int(n)-1])

if __name__ == "__main__":
    main()
