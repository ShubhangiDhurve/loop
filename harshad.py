num=int(input("enter the number"))
i=1
while i==1:
    a=num%10
    b=num//10%10
    c=num//10//10
    d=a+b+c
    i=i+1
    if num%d==0:
        print("harshad  number")
    else:
        print("not")
# i=i+1
    
