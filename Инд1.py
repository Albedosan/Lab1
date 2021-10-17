import math
print('введите чиса a,b,x')
a=float(input())
b=float(input())
x=float(input())
if(math.sin(x/a)!=0):
    y=a*b*x*x-(a/math.sin(x/a))
    print(y)
else:
    print('недопустимое значение')

