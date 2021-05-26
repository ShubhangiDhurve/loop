num=int(input("enter the number"))
i=1
while i<=1:
    if num%2==0 and (2<num<5):
        print("not weird")
    elif num%2==0 and (6<num<20):
        print(" weird")
    elif num%2==0 and num>=20:
        print("not weird")
    else:
        print("weird")
    i=i+1
