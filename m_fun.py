import random
import string

def varianti_len(fpath):
    with open(fpath, encoding="utf-8") as f:
        rindas = f.readlines()
        skaits=len(rindas)
        #print(skaits)
        return skaits
        

def varianti_saturs(fpath):
    with open(fpath, encoding="utf-8") as f:
        rindas = f.readlines()
        nrindas=[]
        #print(rindas)
        for line in rindas:
            n = line.strip()
            nrindas.append(n)
        #print(nrindas)
        return nrindas

def vec(kll):
    vecis=("\t |","\t |\n\t O","\t |\n\t O\n\t/","\t |\n\t O\n\t/|","\t |\n\t O\n\t/|\\","\t |\n\t O\n\t/|\\\n\t/ ","\t |\n\t O\n\t/|\\\n\t/ \\")
    if kll>6:
        kll=6
    if kll>=0:
        v1=vecis[kll]
        print("-------------\n",v1,"\n-------------")
    else:
        print("-------------\n-------------")
        




