file=open("file2.txt","w")
file.write("first\nsecond\nthird")
file.close()
file=open("File2.txt")
f=file.readlines()
f.pop()
f.append("fourth")
file.close()
file=open("file2.txt","w")
for i in f:
    file.write(i)
file.close()