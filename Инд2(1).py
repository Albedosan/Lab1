import math
print('введите чиса a,b,x')
a=float(input())
b=float(input())
x=float(input())
if(a>0):
    d=a*(math.e**(a**0.5))*math.cos(b*x/a)
    print(d)
else:
    print('недопустимое значение')

