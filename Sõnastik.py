from OmaModule import *
rus=[]
ang=[]
while True:
    v=int(input(": "))
    if v==1:
        rus=loe_failist_rus('rus.txt')
        for line in rus:
            print(line)
        print()
        ang=loe_failist_ang('ang.txt')
        for line in ang:
            print(line)
    elif v==2:
        rus=translate('rus.text')
        for line in rus:
            print(line)
            print()
        ang=translate('ang.text')
        for line in ang:
            print(line)