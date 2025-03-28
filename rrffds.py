'''class ARa:
    def __init__(self,name):
        self.name=name
    name="Agent 2"
    ege=99
    stat='idk'
    def hello (self):
        print('privi',self.name)'''

'''class SODA:
    def __init__(self,ingradient='ba'):
        self.ingradient=ingradient
    def showmydrink (self):
        if self.ingradient:
            print(self.ingradient,'це газована вода')
        else:
            print('це звичайна вода')
k=SODA(ingradient='apelsin')
k.showmydrink()
j=SODA('')
j.showmydrink()
'''

u=int(input('vvedit pervoe chislo '))
e=int(input('vvedit vtoroe chislo '))
d=int(input('vvedit tretie chislo '))
class TRIKUTNIK:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def istrigle (self):
        if self.a>0 and self.b>0 and self.c>0:
            if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                print('norm')
            else:
                print('iz etogo nichego ne viidet')
        else:
            print('s negative shislami nichego ne viidet')
kurkuma=TRIKUTNIK(a=u,b=e,c=d)
kurkuma.istrigle()



