
'''N=int(input('скільки разів ви хочите вивести число K'))
K=int(input('яке чило K'))
for i in range (N):
    print(K)'''

'''money=int(input('введіть цукерки в кіло'))
kg=int(input('введіть в деньгі'))
for i in range (1,kg+1):
    print(i/money)

a=1
for i in range (a+1):
    print(a+1)'''



'''a=int(input('введіть число а'))
b=int(input('введіть число b'))
summa=0
for i in range (a,b+1):
    summa=summa+i
print(summa)'''


'''money=int(input('введіть цукерки в кіло'))
kg=int(input('введіть в деньгі'))
for i in range (1,kg+1):
    print(i*money)'''

'''a=int(input('введіть перше число'))
b=int(input('введіть перше друге'))
for i in range (a,b+1):
    print(i*i)'''

'''S=int(input('введіть скільки гривень ви поклали у ощакасу '))
N=int(input('введіть скільки років лежить дипозит у банку '))
for i in range (1,N+1):
    S=(S*0.03)+S
    print(S)'''

'''a=int(input('введіть число а'))
b=int(input('введіть число b'))
summa=1
for i in range (1,b+1):
    summa=summa*i
print(summa)'''

'''N=int(input('скільки було сінокасфрок'))
m=int(input('скільки годин працювала перша сінокосарка'))
total=0
for i in range (1,N+1):
    total=m*1/6*i+m+total
    print(total)'''

'''number=0
while number<=30:
    print(number)
    number+=1
    if number==10:'''
'''number=0
while True:
    number+=1
    print()
    if number==10:
        break'''
number2=0
count=0
'''while True:
    number=int(input('введіть чиcло !!!!!!!!!!!!!!!!!! '))
    if number==0:
        print('гра закінчилася')
        break
    count=count+1
    number2 = number2 + number
print('кількість чисел',count)
print('загальна сума чисел',number2)'''

'''a = int(input('Введіть число:'))
number2=0
count=0
while a !=0:
    b = a% 10
    number2 += b
    a //=10
    count+=1
print('цифр в числі',count)
print('Сума Цифр',number2)'''


'''N = int(input('введіть число: '))
while N != 0:
    if N < 0:
        print('неправильно, зпробуйте ще раз')
    else:
        print(f'Квадрат числа {N} равен {N * N}')
    N = int(input('введіть число: '))'''


N = int(input('введіть число: '))
summa=0
if N <= 0:
    print('зпробуйте ще раз')
for i in range (1,N+1):
    print(2*i-1)
    summa+=(2*i-1)
print('сума чисел',summa)






A = int(input("Введите значение A: "))
N = int(input("Введите значение N: "))
total = 0
for i in range (1,N+1):
    total+=A**i
    print(total)





'''N = int(input('Введите число N: '))

found = False

while N > 0:
    if N % 10 == 2:
        found = True
        break
    N //= 10
print('True' if found else 'False')'''






