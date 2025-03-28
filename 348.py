while True:
    print('оберіть функцію')
    print('1 сумма')
    print('2 різниця')
    print('3 добуток')
    print('4 часне')
    print('5-faktorial')
    print('6 1/x')
    print('7-stupin')
    print('8 korin')
    print('9 leave')
    x=input('оберіть дію')
    print('you take diia number')
    if x=="1":
        number1=int(input('введіть перше число'))
        number2=int(input('введіть друге число'))
        totalnumber=number1+number2
        print('result=',totalnumber)
    if x == "2":
        number3 = int(input('введіть перше число'))
        number4 = int(input('введіть друге число'))
        totalnumber = number3 - number4
        print('result=', totalnumber)
    if x == "3":
        number3 = int(input('введіть перше число'))
        number4 = int(input('введіть друге число'))
        totalnumber = number3 * number4
        print('result=', totalnumber)
    if x == "4":
        number3 = int(input('введіть перше число'))
        number4 = int(input('введіть друге число'))
        totalnumber = number3 / number4
        print('result=', totalnumber)
    if x== '5':
        number3 = int(input('введіть число'))
        number4 = 1
        for i in range(1,number3+1):
            number4 *= i
        print(number4)
    if x== '6':
        number3 = int(input('введіть число'))
        totalnumber = number3 * 0.1
        print('result=',totalnumber)
    if x== '7':
        number3 = int(input('введіть число'))
        number4 = int(input('множне'))
        totalnumber=number3**number4
        print('your number',totalnumber)
    if x== '9':
        print('you leave')
        break
    if x== '8':
        number3 = int(input('введіть число'))
        totalnumber = number3 * number3
        print('result=',totalnumber)