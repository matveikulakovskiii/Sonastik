def loe_failist_rus(rus:str)->list:
    fail=open(rus,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def loe_failist_ang(ang:str)->list:
    fail=open(ang,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def translate(rus:str,ang:str)->list:
    sõna=input("Sisesta sõna mis sa tahad muuta: ")
    if sõna in rus:
        n=rus.count(sõna)
        for j in range(n):
               print(rus.index)
               print(ang.index)
    else:
        if sõna in ang:
            n=ang.count(sõna)
            for j in range(n):
               print(rus.index)
               print(ang.index)
    return rus, ang