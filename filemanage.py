def fastareader(strr,ty=1):
    with open(strr) as ifile:
        data=ifile.readlines()
    for d in data:
        if d=="\n":
            data.remove(d)
        d=list(d)
        while "\n" in d:
            d.remove("\n")
            d="".join(d)
    if ty:
        i=0
        ret =[]
        while i+1<len(data):
            temp=data[i].split(" ")
            pdbid={"PDB ID":temp[0].removeprefix(">")}  
            if temp[1].endswith("protein"):
                ret.append([pdbid,data[i+1]])
            i=i+2
        return ret   
    else:
        return data


def freader(file):
    ret=[]
    with open(file) as ifile:
        k=True
        
        while k:
            try:
                temp=ifile.__next__()
                temp=temp.split(" ")
                if "mol:protein" in temp:
                    pdbid={"PDB ID":temp[0].removeprefix(">")} 
                    ret.append([pdbid,ifile.__next__().strip()])
            except:
                ifile.close()
                k=False
    return ret