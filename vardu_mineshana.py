import random
import string
import m_fun
       
x=(random.randint(0, m_fun.varianti_len("varianti.txt")-1)) #ģenerē gadījuma skaitli variantam        
dotais=(m_fun.varianti_saturs("varianti.txt"))[x] #atrod vārdu, kurš būs jāmin

atbilde=[]
minu=[]
kl=[]
dotais=list(dotais)
garums=len(dotais)
for i in range (garums): # aizpilda sarakstu ar _
    atbilde.append("_")

x=y=0
while x==y: # atrod divus atsedzamos burtus
    x=(random.randint(0, garums-1))
    y=(random.randint(0, garums-1))
z1=dotais[x]
z2=dotais[y]

for b in range(garums): #atsedz 2 burtus
    if dotais[b]==z1:
        atbilde[b]=z1
    if dotais[b]==z2:
        atbilde[b]=z2
print("\nTavs atminamais vārds:\t", atbilde)

def jautajums(): #ievada burtu, salīdzina ar doto vārdu
    burts=input("Ievadi burtu ")
    if burts in atbilde:
        kl.append("1")
    if burts in dotais:
        for j in range (garums):
            if dotais[j]==burts:
                atbilde[j]=burts
    else:
        print("Tāda burta vārdā nav")
        minu.append(burts)
        kl.append("1")          
    print(m_fun.vec(len(kl)))
    print(f"Tavs atminamais vārds ir {atbilde}")
    if len(minu)!=0:
        print("Tu jau pārbaudīji ", minu)
   
    if not "_" in atbilde or len(kl)==(garums-1):
        rezultats()

def rezultats(): #paziņo rezultātu
    if "_"in atbilde:
        print(f"Tu zaudēji \n Atbilde bija {dotais} ")
    else:
        print(f"Tu atminēji\n Atbilde bija {dotais}")

while len(kl)<(garums-1) and "_"in atbilde: #izsauc funkciju minēšanai
    jautajums()




  
