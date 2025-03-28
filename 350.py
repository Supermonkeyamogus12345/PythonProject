'''x=int(input('how many not counteble numbers u need'))
y=1
ponedelok=[y]
for i in range(x):
    y=y+2
    ponedelok.append(y)
print(ponedelok)'''








'''ponedelo = ['false', '0', 'undefined', 'cool', 'hi']
for i in ['false', '0', 'undefined']:
    ponedelo.remove(i)
print(ponedelo)'''


'''ponedelo=[False,0,9,7,4,1,None,""]
for i in ponedelo:
    if i==False:
        ponedelo.remove(False)
    elif i==None:
        ponedelo.remove(None)
print(ponedelo)'''



'''pon=[29,14,78,34,92,65,24,11,91,73]
y=0
o=0
x=len(pon)
    y=y+i
o=y//x
print(o)'''




'''pon=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
gg=[]
for i in range(len(pon)):
    pon[i] = pon[i] * -1
print(pon)
# for i in pon:
#     if i>0:
#         gg.append(i-(i*2))
#     elif i<0:
#         gg.append(i-(i*2))
# print(gg)'''




pon=[-1,2,-3,-5,-4,-6,-7,8,-9,10]
gg=[]
for i in range(len(pon)):
    if i>0:
            gg.append(i)

    print(i)
print(gg)

'''pon=[1,2,3,4,5,6,7,8,9,10]
gg=[]
for i in pon:
    if i%2:
        pon.remove(i)
        gg.append(i)
print(gg)
print(pon)'''
'''o=len([1,2,3,4,5,6,7,8,9,10])
pon=[1,2,3,4,5,6,7,8,9,10]
hh=[]
q=0
for i in pon:
    q=q+i
gg=q%o
for i in pon:
    if gg>=i:
        hh.append(i)
print(gg)
print(hh)'''

