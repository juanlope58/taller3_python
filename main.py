import QueueCollection as qc
import StackCollection as sc

#Queue
myQueue=qc.QueueCollection()

myQueue.add(3)
myQueue.add(4)
myQueue.add(7)
myQueue.add(9)
myQueue.add(1)

myQueue.printQueue()
#print(myQueue.find(5))
myQueue.printQueue()
# print(myQueue.remove(3))
myQueue.printQueue()

# #Stack
myStack=sc.StackCollection()

myStack.add(3)
myStack.add(4)
myStack.add(7)
myStack.add(9)
myStack.add(1)

myStack.printStack()
# print(myStack.remove(3))
myStack.printStack()
# print(myStack.find(3))
myStack.printStack()

