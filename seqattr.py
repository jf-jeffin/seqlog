from collections import Counter
def seqwriter(seq):
    count ={} 
    for s in seq:
        if s in count.keys():
            count[s]=count[s]+1
        else:
            count[s]=1
    aco=Counter(seq)
                
    el=dict(sorted(count.items(),key=lambda item: item[1]))
   
    elePreSeq = "".join(el.keys())[::-1]
    
    if elePreSeq:
        return {
                "Element Precedence" : elePreSeq,
                "Length":len(seq),
                "Most repetited element" : {"Element":elePreSeq[0],"Count":el[elePreSeq[0]],},
                "Least repetited element" : {"Element":elePreSeq[-1],"Count":el[elePreSeq[-1]]},
                "Attribute Count":aco} 
    else:
        return 1


def blockfind(seq):#to find block
    i,block=0,[]
    while i <len(seq):
        jj,temp=seq[i],i
        while i <len(seq) and seq[i]==jj:
            i=i+1
        else:
            if (i-1)-temp>=2:
                block.append([jj,temp,(i-1)-temp],)
    print(block)
    if block:
        islStructure="-".join([x[0] for x in block ])
        islStructCard="-".join([str(x[2]) for x in block ])
        islStructLoc="-".join([str(x[1]) for x in block ])
        LargestIsl=sorted(block,key=lambda l:l[2], reverse =True)[0] 
        return {"Islands Profile": { "Block Element Structure":islStructure,
                                    "Block Cardinality":len(block),
                                    "Block Loction":islStructLoc,
                                    "Block Size":islStructCard,
                                    "Largest Block":LargestIsl,
                                    "Block List": block}}
    else:
         return {"Islands Profile": { "Block Element Structure":"-",
                                    "Block Cardinality":"-",
                                    "Block Loction":"-",
                                    "Block Size":"-",
                                    "Largest Block":"-",
                                    "Block List": "-"}}
    
def eleloci(seq: str,ele="C"):#C IS CYSTINE
    loci=[]
    ind=0
    for s in seq:
        if s==ele:
            ind=seq.index(s,ind)+1
            loci.append(ind)
    return {ele:loci}