from seqattr import *
from seqequ import *
from dbint import connection

#hpcity, ab, cclass,polar,scstruct
print("Initializing....")
SeqCatologue=connection("Protlog")
print("Connected tp SeqLog Database")
print("Initializing Data Extraction....")
ii=True
with open("pdbseq.txt") as ifile:
    k=True
    ord=1      
    while k:
        try:
            temp=ifile.__next__()
            temp=temp.split(" ")
            if "mol:protein" in temp:
                seqdoc={"PDB ID":temp[0].removeprefix(">"),"Seqord":ord} 
                seq=ifile.__next__().strip()
                hseq=transform(seq,hpcity)
                cseq=transform(seq,cclass)
                aseq=transform(seq,ab)
                sseq=stransform(seq,scstruct)
                pseq=transform(seq,polar)
                Sequence={
                    "Sequence":seq,
                    "Hydrophobicity ":hseq,
                    "Chemical Group ":cseq,
                    "Side Chain Structure ":sseq,
                    "Polarity":pseq,
                    "Acidicity":aseq
                }
                seqdoc.update(Sequence)
                for k in Sequence.keys():
                    seqfeat=seqwriter(Sequence[k])
                    seqdoc.update(Sequence)
                    seqblock=blockfind(Sequence[k])
                    seqdoc.update(Sequence)
                while ii:
                    print("Initiating Insertion")
                    ii=False
                inse=SeqCatologue.insert_one(seqdoc)
            ord=ord+1
        except:
            ifile.close()
            print("Finished Extraction and Insertion")
            k=False

print("Protlog Is Constructed")
