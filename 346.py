import random
'''a=random.randrange(1,100,6)
print(a)
b=int(input('abv'))
if a==b:
    print('you win')
else:
    print('you lose')'''

'''import random
a=random.random()
print(a)'''

'''x=random.randrange(10,13,2)
print(x)
y=random.randrange(5,101,5)
print(y)'''


'''x=int(input('введіть межі діапазону чисел менше'))
y=int(input('введіть межі діапазону чисел більше'))
q=int(input())
b=random.randrange(x,y)'''


'''x=int(input('введіть межу для числа'))
result=random.random()*x
print(result)'''


'''x=random.randrange(10,99,2)
print(x)'''


'''x=int(input('ведіть найменшу межу'))
y=int(input('ведіть найбільшу межу'))
v=random.randrange(x,y)
sproby=0
while True:
    sproby=sproby+1
    e = int(input('введіть число в межах яких ви завдали'))
    if v==e:
        print('you win')
        print(sproby, 'count of sproby')
        break
    else:
        print('you lose')'''



'''x=int(input('ведіть найменшу межу'))
y=int(input('ведіть найбільшу межу'))
v=random.randrange(x,y)
sproby=3
while True:
    sproby=sproby-1
    e = int(input('введіть число в межах яких ви завдали'))
    if v==e:
        print('you win')
        break

    print('not yet')

    if sproby !=0:
        print(f"You have {sproby} left")
    elif sproby==0:
        print('you dont have sproby')
        break'''


def y(qwerty):
    if qwerty == 2:
        print('You have 2 attempts left.')
    elif qwerty == 1:
        print('You have 1 attempt left.')
    elif qwerty == 0:
        print('You lose.')

        return True

number1=0
number2=0
number3=0
def codepingvin (count=1):
    global number1,number2,number3
    number1=int(input('vvedit perze sheslo'))
    if count==2:
        number2=int(input('vvedit druzoe sheslo'))
codepingvin(count=2)
v=random.randrange(number1,number2)
o=150
p=random.randrange(3,6)
sproby=3
while True:
    sproby=sproby-1
    e = int(input('введіть число в межах яких ви завдали'))

    if v == e and sproby == 2:
        print('you win and you have bals 500')
        o = o + 5000

    if v == e and sproby == 1:
        print('you win and you have bals 300')
        o = o + 3000

    if v == e and sproby == 0:
        print('you win and you have bals 150')
        o = o + 1500




    if y(sproby):
        break
    print('Did you whant buy a clue?')
    print('or more sproby?')
    a = input(' clue Yes or Not: ')
    if a == 'no':
        print('Okay')
    elif a == 'yes':
        if o < 150:
            print('you dont have enouth balls')
            o-150
            number1 = v + p
            number2 = v - p
        else:
            print('then now you have smaller limits', number1, number2)
    b = input('sproby yes or not')
    if b=='no':
        print('np')
    elif b=='yes':
        if o < 100:
            print('you dont have enouth bals')
        else:
            sproby = sproby + 1
            print('you have', sproby)