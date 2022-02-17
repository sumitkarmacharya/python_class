n=3
file=open("line.txt","w")
file.write("this is first line\nthis is second line\nthis is third line")
file.close()
file=open("line.txt","r")
for i in range(n):
    print(file.readline())
file.close()
