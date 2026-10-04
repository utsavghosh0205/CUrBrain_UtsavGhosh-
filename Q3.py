n=int(input("enter no."))
original=n
if (n<0):
    temp=-n
else:
    temp=n
rev=0
while (temp>0):
    digit=temp % 10
    rev=rev * 10 + digit
    temp//=10
if (n<0):
    rev=-rev
if (n>=0 and original==rev):
    print(original)
else:
    print(original + rev)
