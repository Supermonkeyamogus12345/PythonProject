print('Игра \'Хто хоче стати миліонером\'')
pod50=True
podzn=True
summa=0
n_summa=0
def dost_podskaszki():
    print('\t\t\t\tПоточна сума:',summa)
    print('\t\t\t\tДоступні підсказки:')
    if pod50 == True and podzn == True:
        print('\t\t\t\t**************')
        print('\t\t\t\t*50 на 50*')
        print('\t\t\t\t**************')
        print('\t\t\t\t*Допомога знавця*')
        print('\t\t\t\t**************')
    if pod50 == True and podzn == False:
        print('\t\t\t\t**************')
        print('\t\t\t\t*50 на 50*')
        print('\t\t\t\t**************')
    if pod50 == False and podzn == True:
        print('\t\t\t\t**************')
        print('\t\t\t\t*Допомога знавця*')
        print('\t\t\t\t**************')
    if pod50 == False and podzn == False:
        print('\t\t\t\t**************')
        print('\t\t\t\t*Доступних підсказок немаэ*')
        print('\t\t\t\t**************')

def podskazki(a,b):
    global pod50
    global podzn
    question = input('Хочете використати підказку?')
    if question == 'Да' or question == 'да' or question == 'ДА' or question == 'дА':
        if pod50 ==False and podzn == False and podzn == False:
            print('Доступних підсказок немає')
        elif pod50 == True and podzn == True:
            pods = input('50 на 50 або допомога знавця?')
        elif pod50 == True and podzn == True:
            pods = input('50/50?')
        elif pod50 == True and podzn == True:
            pods = input('допомога знавця?')
        if pods == '50 / 50':
            print('1.',a,'\t2.', b)
            pod50 = False
        elif pods == ('допомога знавця'):
            print('1.',b)
            podzn = False
        else:
            print("Некоректний вибір!")
def question(a, b, a1, a2, a3, а4):
            print("Bonpoc No" + str(a))
            print(b)
            print("1.", a1, "\t2.", a2)
            print("3.", a3, "\t4.", а4)
def loose(a):
    print("Шкода, але ви програли!")
    print("Ваш виграш складає", 'n_sumта', "грн")
Continue = True
Number = 0
begin = input("Хочете почати гру?")
if begin == "Да" or begin == "да" or begin == "ДА":

    ques="Який континент складається лише з однієї країни?"
    question(1,ques,'Європа','Азія,','Африка,','Австралія')
podskazki("Європа", "Австралія")
answer = input("Введіть відповідь: ")
if answer == "Австралія":
    print("Чудово! Ви дали правильнувідповідь!")
    summa = 500
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:

    ques = "Де ростуть соняшники?"
    question(2, ques, "На землі", "На сонці", "Нанебі", "Вводі")
    podskazki("На сонці", "На землі")
    answer = input("Дайте відповідь: ")
if answer == "На землі":
    print("Чудово! Ви дали правильнувідповідь!")
    summa = 1000
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:

    ques = "Яких грошей не буває?"
