import random
import string
class Chainik:
    def __init__(self,obiem,stan,nazva,mode):
        self.obiem=obiem
        self.nazva=nazva
        self.stan=stan
        self.mode=mode
    def spuperchainik (self):
        h = random.randrange(0, 100)
        j = random.randrange(0, 100)
        '''k = random.choice(['a','l','f','h','o'])'''
        k=random.choice (string.ascii_letters)
        k=k.upper()
        p=random.choice (string.ascii_letters)
        p=p.upper()
        n = f'{h}{k}{j}{p}'
        print('stan-',self.stan,'nazva-',self.nazva,'obiem-',self.obiem,'id-',n,'mode-',self.mode)
    def on (self):
        if self.stan == 'on':
            print('chainik yze vkluchen')
        else:
            self.stan='on'
            print('vkluchili chainik')
    def off (self):
        if self.stan=='off':
            print('chainik yze vikluchen')
        else:
            self.stan = 'off'
            print('viklucheni chainik')



