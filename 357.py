from CHAINIK import Chainik
number=0
ggj=[]
while True:
    print("-----menu----- 1)create a chainik 2)chek info abouth chainik 3)chose a chainik from list 4) on chainik 5) off chainik 6)Mode of working 7) Info abouth the all chainiks 8)Info abouth chainik 9) Exit Chose dija:")
    thing=int(input('oberit funkciu'))
    if thing==4:
        ggj[number].on()
    elif thing==5:
        ggj[number].off()
    elif thing==2:
        ggj[number].spuperchainik()
    elif thing==1:
        d=input('vvedit obiem')
        k = input('vvedit stan')
        h = input('vvedit nazvu')
        mn=input('vvedit mode')
        raftchainik=Chainik(obiem=d,nazva=h,stan=k,mode=mn)
        ggj.append(raftchainik)
        number=len(ggj)-1
        print(raftchainik.nazva,'your chainik')
    elif thing==6:
        print('1)mode-eazy')
        print('2)mode-normal')
        print('3)mode-abnormal')
        print('4)mode-superfast')
        odt=int(input('viberite nomer moda'))
        if odt==1:
            mode='eazy'
            print(mode)
        elif odt == 2:
            mode = 'normal'
            print(mode)
        elif odt == 3:
            mode = 'abnormal'
            print(mode)
        else:
            mode = 'superfast'
    elif thing==3:
        hhh=1
        for i in ggj:
            print(hhh,'nazva:',i.nazva)
            hhh=hhh+1
        number=int(input('pls print number of chainik'))-1
        print(ggj[number].nazva)
        print(ggj[number].mode)
        print(ggj[number].stan)
        print(ggj[number].obiem)
    elif thing==7:
        for i in ggj:
            print('nazva:',i.nazva)
            print('mode:', i.mode)
            print('stan:', i.stan)
            print('obiem:', i.obiem)
            print('_'*10,'\n','\n')