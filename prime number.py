n=int(input("Enter the number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Number is not prime number")
            break
    else:
        print("Number is prime number")
else:
    print("Number is prime number")




