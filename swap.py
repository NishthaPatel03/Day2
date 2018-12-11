#Write a function to swap two values provided as arguments.

def swap(a,b):
    t=a
    a=b
    b=t
    print('After swapping, a:',a,'b:',b)

a=int(input('enter a:'))
b=int(input('enter b:'))
print('Before swapping, a:',a,'b:',b)
swap(a,b)
