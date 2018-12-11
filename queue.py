global data,size
queue=[]
list_size=3
def enque(x):
    if(len(queue) == list_size):
        print("Full !")
        return
    queue.append(x)

def deque():
    if(len(queue) == 0):
        print("Empty !")
        return
    print("Removed : %d"%queue[0])
    queue.pop(0)


enque(12)
print(queue)
enque(30)
print(queue)
enque(45)
print(queue)
enque(15)
print(queue)
deque()
print(queue)

        
