hpcity={"H":["A","I","L","M","F","V","P","G"],
     "P":("Q","N","H","S","T","Y","C","W","M","Y"),
     "N":("R","K","D","E")
     }

scstruct={
    "R":("F","H","W","Y","P"),
    "P":("P","7777")
}

polar={"U":("S","T","N","Q","Y","C"),#uncharged
       "P":("K","R"),#posit
       "N":("D","E"),#negat
       "O":("G","A","V","L","I","I","M","F","W","P")#non polar
       }

cclass={
     "A":("A","G","I","L","V"),#ALIPHATIC
     "C":("K","5555"),#cation
     "F":("R","5555"),#fixed cation
     "M":("N","Q"),#amide
     "N":("D","E"),#anion
     "T":("C","222"),#thiol
     "C":("H","2223"),#cationic
     "H":("M","1133"),#thioether
     "R":("F","W","Y"),#aromatic
     "D":("S","T"),#hydroxylic
     "Y":("P","63")#cylic
}

ab={"A":("D","E"),#ACIDIC
    "B":("A","R","N","D")}#BASIC

def transform(seq,key):
    p=""
    for s in seq:
        for ke,va in key.items():
            if s in va:
                p=p+ke 
            else:
                 p=p+"_"
                         
    return p 

def stransform(seq,key):
    p=""
    for s in seq:
        for ke,va in key.items():
            if s in va:
                p=p+ke 
            else:
                 p=p+"C"
                         
    return p

def dnaresolution(seq: str):
    seq=seq.lower()
    j={"a":"","c":"","g":"","t":""}
    for r in seq:
        for a in j.keys():
                if a!=r:
                    j[a]=j[a]+"_"
                else:
                    j[a]=j[a]+ r     
    return j

def resol(seq):
    ele,co={},0
    for r in seq:
        if r not in ele.keys():
            ele[r]=("_"*co)+r
            print(ele)
        else:
            for a in ele.keys():
                if a!=r:
                        ele[a]=ele[a]+"_"
                else:
                        ele[a]=ele[a]+ r  
        co=co+1
    return ele