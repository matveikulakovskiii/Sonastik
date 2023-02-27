def isrus(x:str):
    alphRL=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    alphRU=[x.upper() for x in alphRL]
    alphR=alphRL+alphRU
    xkop=list(x)
    for i in range(len(xkop)):
        if xkop[i] not in alphR:
            return False
        return True

def isest(x:str):
    alphEL=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphEU=[x.upper() for x in alphEL]
    alphE=alphEL+alphEU
    xkop=list(x)
    for i in range(len(xkop)):
        if xkop[i] not in alphE:
            return False
        return True

def finl(fail):
    spisok=[]
    with open(fail,'r',encoding="utf-8-sig") as f:
        for line in f:
            spisok.append(line.strip())
            return spisok

def sav(x,fail):
    for i in range(len(x)):
        x[i]=x[i]+"\n"
    with open(fail,"w",encoding="utf-8-sig") as f:
        f.writelines(x)


def loe(x:str)->str:
    with open(x,"r",encoding="utf-8-sig") as f:
        jarjend=[]
        for rida in f:
            jarjend.append(rida.strip())
            return jarjend

def tolk(rus,est):
    sona=input("Kirjutage sõna, mida soovite tõlkida ")
    while sona.isdigit():
        sona=input("Kirjuta õige sõna")
    if sona not in rus and sona not in est:
         print("Seda sõna pole sõnastikus ")
         vale=input("Kas soovite selle sõna sõnaraamatusse lisada? (jah või ei) ").lower()
         while vale not in ["jah","ei"]:
              vale=input("Kirjuta ainult jah või ei ")
         if vale=="jah":
              if isrus(sona)==True:
                    rus.append(sona)
                    tolke=input("Kirjutage sõna tõlge ")
                    while tolke.isdigit():
                          tolke=input("Kirjuta õige sõna ")
                    est.append(tolke)
              else:
                    rus.append(sona)
                    tolke=input("Kirjutage sõna tõlge ")
                    while tolke.isdigit():
                         tolke=input("Kirjuta õige sõna ")
                    est.append(sona)
         else:
              print("Olgu, hüvasti")
    for i in range(len(rus)):
        if sona==rus[i]:
             print(f"{rus[i]} - {est[i]}")
             heli(est[i],"et")
        elif sona==est[i]:
             print(f"{est[i]} - {rus[i]}")
             heli(rus[i],"ru")
        sav(rus,'rus.txt');sav(est,'est.txt')

def paranda(fail1:str,fail2:str):
    rus,est=finl(fail1,fail2)
    indv=input("Millist sõna soovite parandada? ")
    while indv not in rus and indv not in est:
        indv=input("Kirjutage õige sõna ")
    ind=rus.index(indv)
    if ind==None:
        ind=est.index(indv)
    parasona=input("Kirjutage parandatud sõna ")
    while parasona.isdigit():
        parasona=input("Kirjutage õige sõna ")
    if isrus(indv)==True:
        rus.pop(ind)
        rus.insert(ind,parasona)
    else:
        est.pop(ind)
        est.insert(ind)
    sav(rus,'rus.txt');sav(est,'est.txt')



