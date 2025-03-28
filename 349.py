number1=0
number2=0
def yu (count=1):
    global number1,number2
    number1=int(input('vvedit perze sheslo'))
    if count==2:
        number2=int(input('vvedit druzoe sheslo'))
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
    print('you take diia number',x)
    if x=="1":
        yu (count=2)
        totalnumber=number1+number2
        print('result=',totalnumber)
    if x == "2":
        yu (count=2)
        totalnumber = number1 - number2
        print('result=', totalnumber)
    if x == "3":
        yu (count=2)
        totalnumber = number1 * number2
        print('result=', totalnumber)
    if x == "4":
        yu (count=2)
        totalnumber = number1 / number2
        print('result=', totalnumber)
    if x== '5':
        yu (count=1)
        for i in range(1,number1+1):
            number2 *= i
        print(number2)
    if x== '6':
        yu(count=1)
        totalnumber = number1 * 0.1
        print('result=',totalnumber)
    if x== '7':
        yu (count=2)
        totalnumber=number1**number2
        print('your number',totalnumber)
    if x== '9':
        print('you leave')
        break
    if x== '8':
        yu(count=1)
        totalnumber = number1 * number1
        print('result=',totalnumber)



