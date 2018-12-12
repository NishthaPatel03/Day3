global queue,size
queue=[]
size=int(input('Enter length of queue:'))

class Queue:
    

    def enque(self,x):
        if(len(queue) == size):
            print("Full !")
            return
            queue.append(x)

    def deque(self):
        if(len(queue) == 0):
            print("Empty !")
            return
        print("Removed : %d"%queue[0])
        queue.pop(0)

Q=Queue()
Q.enque(1)
print(queue)
Q.enque(2)
Q.deque()

