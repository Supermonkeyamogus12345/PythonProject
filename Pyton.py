'''age=7*2
if age>14:
    print('you can take passport')
elif age==14:
    print("You can have passport")
else:
    print('you cannot take a passport')
    print('lol')'''

'''number=int(input('введіть число  '))
if number>0:
    print('yes',number+1)
else:
    print('no', number)'''

'''number1=int(input('введіть перше число '))
number2=int(input('введіть друге число '))
number3=int(input('введіть third число '))
kont=0
if number1>0:
    kont=kont+1
if number2>0:
    kont=kont+1
if number3>0:
    kont=kont+1
print('число правильних відповідей ',(kont))'''

'''number1=int(input('введіть перше число '))
number2=int(input('введіть друге число '))
number3=int(input('введіть third число '))
kont=0
if number1<0:
    kont=kont+1
if number2<0:
    kont=kont+1
if number3<0:
    kont=kont+1
print('число неправильних відповідей ',(kont))'''








'''number1=int(input('введіть число '))
if number1==0:
     number1=number1+10
if    number1>1:
    number1 = number1 + 1
if number1<-1:
    number1 = number1-2
print(number1)'''







'''def change_number(number):

  if number > 0:
    return number + 1
  elif number < 0:
    return number - 2
  else:
    return 10

user_number = int(input("Введите число: "))

result = change_number(user_number)
print("Результат:", result)'''



'''scores=int(input('введіть ваши бали  '))
if scores==1:
    print('0 балів ухти')
elif scores<=15:
    print('2 балів ухти')
elif scores<=25:
    print('3 балів ухти')
elif scores<=35:
    print('4 балів ухти')
elif scores<=45:
    print('5 балів ухти')
elif scores<=55:
    print('6 балів ухти')
elif                 scores<=65:
    print('7 балів ухти')
elif scores<=75:
    print('8 балів ухти')
elif scores<=85:
    print('9 балів ухти')
elif scores<=95:
    print('прекрасно 10 балів')'''

age=int(input('введіть свій вік: '))
if age>=121:
    print('ви хто?')
elif age>=61:
    print('ви літня людина')
elif age>=21:
    print('ви доросла людина')
elif age>=16:
    print('ви підліток')
elif age>=6:
    print('ви дитина')
elif age>=0:
    print('ви немовля')
