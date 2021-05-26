i=1
while i<=10:
    user=int(input("enter the number"))
    if user==4:
         print(user,"waah!,you are guessing number")
         break
    elif user<4:
        print(user,"your number is small,so try again")
    elif user>4:
        print(user,"your number is big, so try again")
    i=i+1
    # if user==4:
    #     print(user,"waah!,you are guessing number")
