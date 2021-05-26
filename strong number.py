i=int(input("enter the number"))
b=i
sum=0
while i>0:
    a=1
    f=1
    rem=b%10
    while b<=rem:
        f=f*b
        a=a+1
        sum=sum+f
        b=b//10
if sum==i:
        print("strong number")
    else:
        print("no")

   