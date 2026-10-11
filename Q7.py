arr =[]
n=int(input("no. of terms"))
for(int i=0,i<n,i++):
  arr[i]=int(input("enter the no."))


gcd = arr[0]

for i in range(1, len(arr)):
    a = gcd
    b = arr[i]

    while (b!=0):
        r = a % b
        a = b
        b = r

    gcd = a

print(gcd)
