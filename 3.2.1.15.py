class QueueError(IndexError):
    pass
    
class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue)>0 :
            elem - self.queue[0]
            del self.queue[0]
            return elem
        
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print ("1")
    print ("perro")
    print ("false")
    print("Error de Cola")
