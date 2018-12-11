#seek and tell functions.

f1=open('abc.txt','r+')
str=f1.read()
print('read string is:',str)

position=f1.tell()
print('current position is:',position)

position=f1.seek(0,0)
str=f1.read()
print('again read string is:',str)
