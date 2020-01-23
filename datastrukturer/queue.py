class Queue:

    def __init__(self):
        self.l = [0 for i in range(0,100)]
        self.head = 0
        self.tail = 0

    def enqueue(self, e):
        if self.queue_full():
            print('Queue full!')
            #pass
        else:
            self.l[self.tail] = e
            self.tail += 1
            if self.tail >= len(self.l):
                self.tail = 0

    def dequeue(self):
        if self.queue_empty():
            e = None
        else:
            e = self.l[self.head]
            self.head += 1
            if self.head >= len(self.l):
                self.head = 0
        return e

    def queue_empty(self):
        return self.head == self.tail

    def queue_full(self):
        #Randbetingelser?
        if self.tail > self.head:
            return self.tail-self.head+1 == len(self.l)
        else:
            return self.tail - self.head +1 == 0
