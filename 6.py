x=int(input())
reversed=0
while x>0:
    reversed=(reversed+x%10)*10
    x=x//10
reversed=reversed//10
print(reversed)