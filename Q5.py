n = int(input())
digits = []
while (n>0):
    digit=n%10
    if (digit%2==0):
        digit=0
    digits.append(digit)
    n //= 10
digits.reverse()
print(digits)
