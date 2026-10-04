n = int(input("enter no."))
sign = 1
if (n<0):
    sign = -1
    n = -n
rev = 0
while (n>0):
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
rev=rev*sign
print(rev*2)
