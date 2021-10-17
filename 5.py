x=int(input())
s=1
while x>0:
    s=s*(x%10)
    x=x//10
print(s)