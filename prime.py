# num=int(input("enter the number"))
# i=1
# count=0
# while i<=num:
#     if num%i==0: 
#         count=count+1 
#     i=i+1
# if count==1:
#     print(num,"prime number")
# elif count==2:
#     print(num,"prime number")
# else:
#     print("not prime")



# num=int(input("enter the number"))
# i=1
# n=0
# while i<=num:
#     if (num%n==0 and n%1==0):
#         if (n%2!=0 and n%3!=0):
#             print("prime number")
#     else:
#         print("it is not prime number")
#     i=i+1





i=1
while i<=100:
    if i%2!=0 and i%3!=0 and i%5!=0:
        print(i)
    i=i+1
