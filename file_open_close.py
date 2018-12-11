#file open and close

#open_the_file
f1=open("abc.txt","w+")

print('file_name:',f1.name)
print('mode:',f1.mode)
print('closed?',f1.closed)

#close the file
f1.close()
print('closed?',f1.closed)

