#print fibonacci series using recursion.

def fibo(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        return fibo(number-1)+fibo(number-2)
        

number=int(input('Enter a number:'))
for i in range(number):
    print(fibo(i))

