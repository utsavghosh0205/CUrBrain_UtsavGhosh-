n = int(input())
n = abs(n)
if n==0:
    digits=1
else:
    digits=0
    while n > 0:
        digits+=1
        n//=10
if digits%2==0:
    print(True)
else:
    print(False)
