# n=int(input("enter the number"))
# temp=n
# rev=0
# while temp>0:
#     reminder=temp%10
#     rev=rev*10+reminder
#     rev=temp//10
# if rev==temp:
#     print("it is palindrome number",rev)
# else:
#     print("it is not palindrome number",rev)

n=int(input("enter the number"))
org=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
# print(rev)
if rev==org :
    print("palidrome",rev)
else:
    print("not",rev)