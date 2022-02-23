import random
while True:
    Message=int(input("Press 1 for execute and 0 for exit:"))
    if Message==1:
        n=int(input("Guess the number:"))
        r=random.randint(1,n)
        print(r)
        if n==r:
            print("The number is right")
        else:
            print("The number is wrong")
    elif Message==0:
        break
