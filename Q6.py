n = int(input())
a = int(input())
b = int(input())
count_a = 0
count_b = 0
if (n==0):
    if a == 0:
        count_a = 1
    if b == 0:
        count_b = 1
while n > 0:
    digit = n % 10
    if digit == a:
        count_a += 1
    if digit == b:
        count_b += 1
    n //= 10
difference = count_a - count_b
if (difference<0):
    difference=-difference
print(difference)
