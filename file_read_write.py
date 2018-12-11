#file read and write

file1=open("abc.txt","a+")
file1.write("Hello world")

file1.close()

file=open("abc.txt","r+")
str=file.read()
print(str)
file.close()