global data,size
stack=[]
list_size=3
def push(x):
    if(len(stack) == list_size):
        print("Stack overflow !")
        return
    stack.append(x)

def pop():
    if(len(stack) == 0):
        print("Stack underflow !")
        return
    print("Poped : %d"%stack[-1])
    stack.pop()


push(12)
print(stack)
push(30)
print(stack)
push(45)
print(stack)
push(15)
print(stack)
pop()
print(stack)

        
