import random
print("If you can guess right lucky number three times you will be our lucky winner")
i=0
count=0
while i<10:
    num=int(input("Guess the number:"))
    r=random.randint(1,5)
    i+=1
    if num==r:
        count+=1
    print("Lucky number:",r)
    if count==3:
        print("Congratulation you are lucky winner")
        break
if count<3:
    print("Sorry try again later")
