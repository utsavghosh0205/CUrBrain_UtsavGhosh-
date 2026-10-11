
n = int(input())

prime = [1] * n

if (n > 0):
    prime[0] = 0
if (n > 1):
    prime[1] = 0

for i in range(2, n):
    if (prime[i] == 1):
        j = i * 2

        while (j < n):
            prime[j] = 0
            j = j + i

count = 0

for i in range(n):
    if prime[i] == 1:
        count = count + 1

print(count)
