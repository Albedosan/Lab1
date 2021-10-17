x=int(input())
y=int(input())
z=int(input())
if (x>=0) and(x<=11) and (y>=0) and(z<=59):
    s=12*x+y/2+z*(0.5/60)
    print(s)
else:
    print('ошибка ввода')