print('ведите a1')
a1=float(input())
print('ведите а2')
a2=float(input())
print('ведите а3')
a3=float(input())
print('ведите b1')
b1=float(input())
print('ведите b2')
b2=float(input())
print('ведите b3')
b3=float(input())
print('ведите c1')
c1=float(input())
print('ведите c2')
c2=float(input())
print('ведите c3')
c3=float(input())
print('ведите d1')
d1=float(input())
print('ведите d2')
d2=float(input())
print('ведите d3')
d3=float(input())
op=a1*b2*c3+b1*c2*a3+c1*a2*b3-c1*b2*a3-a1*c2*b3-b1*a2*c3
if op!=0:
    op1=d1*b2*c3+b1*c2*d3+c1*d2*b3-c1*b2*d3-d1*c2*b3-b1*d2*c3
    op2=a1*d2*c3+d1*c2*a3+c1*a2*d3-c1*d2*a3-a1*c2*d3-d1*a2*c3
    op3=a1*b2*d3+b1*d2*a3+d1*a2*b3-d1*b2*a3-a1*d2*b3-b1*a2*d3
    x=op1/op
    y=op2/op
    z=op3/op
    print(x,y,z)
else:
    print('определитель равен 0')


