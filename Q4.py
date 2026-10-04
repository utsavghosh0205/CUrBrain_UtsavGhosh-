n=int(input("enter a no."))
sum=0
product=1
while (n>0):
    digit=n%10
    sum=sum+digit
    product=product*digit
    n//=10
print(product-sum)
